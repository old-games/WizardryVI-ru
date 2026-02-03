import enum


def decompress(data: bytes) -> bytes:
    result = bytearray()
    i = 0
    data_len = len(data)
    while i < data_len:
        x = data[i]
        i += 1
        if i % 0x1000 == 0:
            # Padding.
            continue
        if x < 0x80:
            if i + x > data_len:
                raise ValueError(f'Unexpected end of data at {i} for literal run of {x} bytes.')
            result.extend(data[i:i+x])
            i += x
            continue
        if x != 0:
            if i >= data_len:
                raise ValueError(f'Unexpected end of data at {i} for RLE run.')
            o = data[i:i+1]
            i += 1
            result.extend(o * (0x100 - x))
        if x == 0:
            # Terminator.
            break
    return bytes(result)


def normalize_compressed(data: bytes, is_original: bool) -> bytes:
    '''
    Last control byte in each 0x1000 page is ignored by the decompressor.
    '''

    # Encoder-style normalization policy:
    # - A control byte is ignored by the decompressor iff the input index becomes
    #   a multiple of 0x1000 immediately after reading it.
    # - Those ignored control bytes can be "garbage" filler in original assets.
    # - However, once we have evidence that at least one 4K output block's last
    #   byte (offset 4095) is written by a real token byte (ctrl or payload) rather
    #   than garbage filler, we treat subsequent block-end bytes as deterministic
    #   and do not normalize further ignored controls.
    #
    # Practically, we detect this "deterministic" moment when we ever observe a
    # byte at file offset ...FFF that is reached as a normal ctrl/payload byte.
    # (Not by the ignored-control rule.)

    result = bytearray(data)
    i = 0
    data_len = len(data)
    seen_deterministic_block_end = False
    last_block_index = None
    prev_block_index = None
    while i < data_len:
        ctrl_off = i
        x = data[i]
        i += 1

        if i % 0x1000 == 0:
            # This control byte is ignored.
            if is_original and not seen_deterministic_block_end:
                result[ctrl_off] = 0xff
            continue

        # If this *non-ignored* ctrl itself lives at ...FFF, we have a deterministic block end.
        if ctrl_off % 0x1000 == 0x0fff:
            seen_deterministic_block_end = True

        if x == 0:
            # Terminator.
            continue

        last_block_index, prev_block_index = i - 1, last_block_index
        if x < 0x80:
            # Literal payload.
            if i + x > data_len:
                raise ValueError(f'Unexpected end of data at {i} for literal run of {x} bytes.')
            # If the last literal payload byte lands at ...fff, that's a deterministic block end.
            end_payload = i + x - 1
            if end_payload % 0x1000 == 0x0fff:
                seen_deterministic_block_end = True
            i += x
        else:
            # RLE payload (1 byte).
            if i >= data_len:
                raise ValueError(f'Unexpected end of data at {i} for RLE run.')
            # If the RLE value byte lands at ...FFF, that's a deterministic block end.
            if i % 0x1000 == 0x0fff:
                seen_deterministic_block_end = True
            i += 1

    assert result[-1] == 0x00, 'Normalized compressed data should end with a terminator (0x00).'

    if is_original:
        # Try our best to merge the last two blocks.
        if last_block_index is not None:
            if result[last_block_index] < 0x80:
                len_last_run = result[last_block_index]
                if len_last_run > 1 and result[last_block_index + len_last_run] == result[last_block_index + len_last_run - 1]:
                    tail_count = 2
                    for i in range(last_block_index + len_last_run - 2, last_block_index, -1):
                        if result[i] == result[last_block_index + len_last_run]:
                            tail_count += 1
                        else:
                            break
                    tail_consume = min(128, tail_count)
                    if tail_consume >= 3:
                        result[last_block_index] -= tail_consume
                        result[last_block_index + len_last_run + 1 - tail_consume:last_block_index + len_last_run + 1] = [(0x100 - tail_consume) & 0xff, result[last_block_index + len_last_run]]
                        if result[last_block_index] == 0:
                            del result[last_block_index:last_block_index + 1]
            elif prev_block_index is not None and result[last_block_index] >= 0x80:
                len_last_run = 0x100 - result[last_block_index]
                if result[prev_block_index] >= 0x80:
                    len_prev_run = 0x100 - result[prev_block_index]
                    # Merge 2 RLE runs.
                    if result[last_block_index + 1] == result[prev_block_index + 1]:
                        len_combined_head = min(128, len_last_run + len_prev_run)
                        len_combined_tail = len_last_run + len_prev_run - len_combined_head
                        result[prev_block_index] = (0x100 - len_combined_head) & 0xff
                        if len_combined_tail > 0:
                            result[last_block_index] = (0x100 - len_combined_tail) & 0xff
                        else:
                            del result[last_block_index:last_block_index + 2]
                    elif len_last_run == 1:
                        result[last_block_index] = 1
                elif len_last_run <= 2:
                    len_prev_run = result[prev_block_index]
                    # Merge literal and RLE run.
                    if result[prev_block_index + len_prev_run] == result[last_block_index + 1]:
                        tail_count = 1
                        for i in range(prev_block_index + len_prev_run - 1, prev_block_index, -1):
                            if result[i] == result[last_block_index + 1]:
                                tail_count += 1
                            else:
                                break
                        tail_consume = min(128, tail_count + len_last_run)
                        result[last_block_index] = (0x100 - tail_consume) & 0xff
                        if len_prev_run == tail_consume:
                            del result[prev_block_index:prev_block_index + len_prev_run + 1]
                        else:
                            result[prev_block_index + len_prev_run + 1 - tail_consume:prev_block_index + len_prev_run + 1] = []
                            result[prev_block_index] -= tail_consume
                    elif len_prev_run + len_last_run <= 127:
                        result[prev_block_index] = (len_prev_run + len_last_run) & 0xff
                        result[last_block_index:last_block_index + 2] = result[last_block_index + 1:last_block_index + 2] * len_last_run
                    elif len_last_run == 1:
                        assert len_prev_run == 127
                        result[last_block_index] = 1

    return bytes(result)


class EntryType(enum.Enum):
    LITERAL = 1
    RLE = 2
    PADDING = 3


def decompress_debug(data: bytes) -> list[tuple[EntryType, bytes]]:
    '''
    Decompress data like `decompress`, but return a list of (count, bytes) tuples
    representing the decompressed runs for debugging purposes.
    '''

    result = []
    i = 0
    data_len = len(data)
    while i < data_len:
        x = data[i]
        i += 1
        if i % 0x1000 == 0:
            # Padding.
            result.append((EntryType.PADDING, b'\x00'))
            continue
        if x < 0x80:
            if i + x > data_len:
                raise ValueError(f'Unexpected end of data at {i} for literal run of {x} bytes.')
            literal = data[i:i + x]
            result.append((EntryType.LITERAL, literal))
            i += x
            continue
        if x != 0:
            if i >= data_len:
                raise ValueError(f'Unexpected end of data at {i} for RLE run.')
            o = data[i:i + 1]
            i += 1
            run = o * (0x100 - x)
            result.append((EntryType.RLE, run))
    return result


def compress(data: bytes) -> bytes:
    '''Compress bytes using the inverse of the simple RLE used in `decompress`.

    Encoding rules (compatible with `decompress`):
    - A control byte x < 0x80 indicates a literal run of length x, followed by x literal bytes.
    - A control byte x in [0x80..0xff] indicates an RLE run: the next single byte 'o' is
      repeated (0x100 - x) times.
    - The value 0x00 as a control is a no-op in `decompress` and should not be emitted.

        The compressor uses a greedy strategy intended to match the original
        asset-encoder behavior reasonably well:
        - Emit RLE for runs of length >= 3 (up to 128), split longer runs.
            (This matches the observed original asset tokenization better.)
        - Otherwise emit literals up to 127 bytes.

    The decompressor has a special-case: after reading each control byte, if the
    compressed-stream read index becomes a multiple of 0x1000, that control byte is
    treated as padding and produces no output.

    To match that convention (and the original files), the compressor ensures that
    if we're about to start a token with only 1 byte left in the current 0x1000 page,
    we emit a single padding control byte. The decompressor ignores that byte.
    '''

    n = len(data)
    i = 0
    out = bytearray()
    lit_buf = bytearray()

    def _space_in_page() -> int:
        '''
        How many bytes we can still write in the current 0x1000 page.
        '''

        return 0x1000 - (len(out) % 0x1000)

    def emit_bytes(bs: bytes | bytearray) -> None:
        out.extend(bs)

    def last_byte_of_previous_page() -> int:
        """Return the last byte of the previous 0x1000-byte output page.

        Some original-style encoders appear to write a stale byte into the last
        position of a 4K block when they need a dummy control byte. The simplest
        model is: reuse the last byte of the previous output page.
        """

        cur_page_start = len(out) - (len(out) % 0x1000)
        prev_page_start = cur_page_start - 0x1000
        if prev_page_start < 0:
            return 0xff
        return out[cur_page_start - 1]

    def emit_padding_if_needed() -> None:
        '''
        Ensure we never start a token when only 1 byte remains in the page.

        Any real token is at least 2 bytes (control + 1 payload byte for RLE;
        or control + >=1 literal byte). If we're at offset 0xfff within a page,
        we'd have 1 byte left; the original format places a padding control (0x00)
        there, which `decompress` ignores.
        '''

        if _space_in_page() == 1:
            # Value is semantically irrelevant (decoder ignores it), but to
            # mimic an encoder that reuses a stale byte from the previous 4K
            # output block, copy the last byte of the previous page.
            out.append(last_byte_of_previous_page())

    def emit_literal_prefix(literal: bytes | bytearray) -> int:
        '''
        Emit *at most one* literal token prefix from `literal`.

        Returns how many bytes from `literal` were emitted.

        Important: if `literal` doesn't fit in the current 0x1000 page, we emit
        only the part that fits and leave the remainder to be deferred in
        `lit_buf` so it can merge with future literals.
        '''

        if not literal:
            return 0

        emit_padding_if_needed()

        # Need at least 2 bytes to emit anything (control + 1 literal byte).
        space = _space_in_page()
        if space < 2:
            # Should be unreachable due to `emit_padding_if_needed()`.
            out.append(0x00)
            return 0

        max_payload_by_page = space - 1
        payload_len = min(127, max_payload_by_page, len(literal))
        out.append(payload_len & 0x7f)
        emit_bytes(literal[:payload_len])
        return payload_len

    def emit_rle_token(value: int, run_len: int) -> None:
        '''
        Emit a (possibly split) RLE run.
        '''

        rem = run_len
        while rem > 0:
            emit_padding_if_needed()

            # RLE token is always 2 bytes.
            space = _space_in_page()
            if space < 2:
                out.append(0x00)
                continue

            chunk = min(rem, 128)
            ctrl = (0x100 - chunk) & 0xff
            out.append(ctrl)
            out.append(value & 0xff)
            rem -= chunk

    def flush_literal_buf() -> None:
        nonlocal lit_buf
        if not lit_buf:
            return

        # We may be flushing because we encountered an RLE-run (>=3) and need
        # to close pending literals. However, if the *only* reason we need to
        # split is a 4K page boundary, do not emit the remainder immediately.
        # Keep it buffered so it can merge with subsequent literal bytes.
        while lit_buf:
            emitted = emit_literal_prefix(lit_buf)
            if emitted <= 0:
                # Can't make progress (shouldn't happen), avoid infinite loop.
                break
            lit_buf = lit_buf[emitted:]

            # If we had to split due to page space, defer the remainder.
            # We detect that by: remainder exists AND the current page doesn't
            # have room for at least another minimal token (2 bytes).
            # In practice, this happens when we just filled the page.
            if lit_buf and _space_in_page() < 2:
                break

    while i < n:
        # Detect run length at `i`.
        run_len = 1
        while i + run_len < n and data[i + run_len] == data[i] and run_len < 128:
            run_len += 1

        if run_len >= 3:
            # Flush any pending literals first.
            if lit_buf:
                flush_literal_buf()
            emit_rle_token(data[i], run_len)
            i += run_len
        else:
            # Accumulate literal.
            lit_buf.append(data[i])
            i += 1
            # Don't flush just because we reached 127 bytes.
            # The encoder can split literals when needed (emit_literal_prefix
            # emits at most 127 bytes). Keeping a larger buffer lets us merge
            # later-adjacent literal fragments and match the original token
            # boundaries more closely.

    if lit_buf:
        flush_literal_buf()

    # Emit a terminator control (0x00). Original files typically end with this.
    # Note: if we are at the last byte of a page, emit_padding_if_needed() will
    # insert a padding byte first, then we emit the terminator.
    emit_padding_if_needed()
    out.append(0x00)

    return bytes(out)
