import os
import time

from PIL import Image
import pyautogui
import cv2
import numpy as np

import controller
import definition
import maze

experience_by_index_by_time = [[], [], [], [], [], []]


def review(character_index=0, pictures_dir="pictures", precision=0.95):
    characters = maze.get_number_of_characters(pictures_dir=pictures_dir, precision=precision)
    print(f"Number of characters: {characters}")

    # Step 1: Find reviewwho.png and click below it (height/4)
    reviewwho_path = os.path.join(pictures_dir, "reviewwho.png")
    pos = controller.find_image(reviewwho_path, precision=precision)
    if pos[0] == -1:
        print("reviewwho.png not found")
        return

    review_who_lines = 1
    reviewwho_img = Image.open(reviewwho_path)
    w, h = reviewwho_img.size
    click_x = sum((
        pos[0],
        w // 4,
        w // 2 * (character_index % 2),
    ))
    click_y = sum((
        pos[1],
        h,
        h // review_who_lines * (2 - review_who_lines),
        h // review_who_lines // 2,
        (character_index // 2) * (h // review_who_lines),
    ))
    pyautogui.moveTo(click_x, click_y, duration=0.05)
    time.sleep(0.05)
    pyautogui.click(click_x, click_y)
    time.sleep(0.2)

    # Step 2: Wait for exp.png to appear
    exp_path = os.path.join(pictures_dir, "exp.png")
    start_time = time.time()
    timeout = 10
    exp_pos = (-1, -1)
    while time.time() - start_time < timeout:
        exp_pos = controller.find_image(exp_path, precision=precision)
        if exp_pos[0] != -1:
            break
        time.sleep(0.1)
    if exp_pos[0] == -1:
        print("exp.png not found")
        return

    # Step 3: Screenshot area to the right of exp.png till end of window
    left, top, right, bottom = controller.window_region()
    exp_img = Image.open(exp_path)
    region_left = exp_pos[0] + exp_img.width
    region_top = exp_pos[1]
    region_width = right - region_left
    region_height = exp_img.height
    screenshot = pyautogui.screenshot(region=(region_left, region_top, region_width, region_height))

    # Split screenshot into 11 columns and OCR each (up to 10th)
    exp_number = ""
    col_width = region_width // 11
    for i in range(10):  # Only up to 10th column
        x1 = i * col_width
        x2 = x1 + col_width
        digit_img = screenshot.crop((x1, 0, x2, region_height))

        # Pad digit_img with 10% space on each side
        pad_w = int(0.1 * digit_img.width)
        pad_h = int(0.1 * digit_img.height)
        new_w = digit_img.width + 2 * pad_w
        new_h = digit_img.height + 2 * pad_h
        digit_img_padded = Image.new("RGB", (new_w, new_h), (0, 0, 0))
        digit_img_padded.paste(digit_img, (pad_w, pad_h))
        digit_img = digit_img_padded

        # Check if column is not empty (not all white)
        if digit_img.getbbox() is not None:
            # Print digit_img as pseudo graphics
            ascii_chars = "@%#*+=-:. "
            if not "debug":
                img_small = digit_img.convert("L")
                for y in range(img_small.height):
                    line = ""
                    for x in range(img_small.width):
                        pixel = img_small.getpixel((x, y))
                        line += ascii_chars[int(pixel * len(ascii_chars) // 256)]
                    print(line)
                print("-" * img_small.width)

            # Instead of tesseract, match against digit templates using OpenCV
            best_digit = None
            best_score = None
            digit_img_cv = np.array(digit_img.convert("L"))
            for d in range(10):
                digit_name = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][d]
                digit_path = os.path.join(pictures_dir, "digit", f"{digit_name}.png")
                if not os.path.exists(digit_path):
                    continue
                template = Image.open(digit_path).convert("L")
                template_cv = np.array(template)
                img_cv = np.array(digit_img.convert("L"))

                # Use normalized cross-correlation for location
                res = cv2.matchTemplate(img_cv, template_cv, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                top_left = max_loc
                score = max_val

                # print(f"Score for {d} ({digit_name}): {score}")
                if best_score is None or score > best_score:
                    best_score = score
                    best_digit = str(d)
            if best_digit is not None:
                exp_number += best_digit

    print("Scanned EXP number:", exp_number)
    try:
        exp_number = int(exp_number)
        experience_by_index_by_time[character_index].append((time.monotonic(), exp_number))
        if len(experience_by_index_by_time[character_index]) >= 2:
            t0, exp0 = experience_by_index_by_time[character_index][0]
            t1, exp1 = experience_by_index_by_time[character_index][-1]
            dt = t1 - t0
            dexp = exp1 - exp0
            if dt > 0:
                avg_speed = dexp / dt  # EXP/sec
        else:
            avg_speed = 0.0
        print(f"Average EXP gain speed: {avg_speed*3600:.2f} EXP/hour")
        for cls in [definition.Class.PRIEST, definition.Class.THIEF, definition.Class.PSIONIC, definition.Class.MAGE]:
            current_level = definition.get_level_by_experience(cls, exp_number)
            next_level_exp = definition.get_level_experience(cls, current_level + 1)
            exp_to_next = next_level_exp - exp_number
            eta = exp_to_next / avg_speed if avg_speed > 0 else float('inf')
            if eta == float('inf'):
                eta_str = "∞"
            else:
                eta_int = int(eta)
                days = eta_int // 86400
                hours = (eta_int % 86400) // 3600
                minutes = (eta_int % 3600) // 60
                eta_parts = []
                if days:
                    eta_parts.append(f"{days}d")
                if hours:
                    eta_parts.append(f"{hours}h")
                if minutes or not eta_parts:
                    eta_parts.append(f"{minutes}m")
                eta_str = " ".join(eta_parts)
            print(f"{cls.name.title()}: {exp_to_next} EXP to next level ({current_level+1}: {next_level_exp}), ETA: {eta_str}")

    except ValueError:
        print("Failed to parse EXP number:", exp_number)

    # Click exit.png at the end
    exit_path = os.path.join(pictures_dir, "exit.png")
    exit_pos = controller.find_image(exit_path, precision=precision)
    if exit_pos[0] != -1:
        exit_img = Image.open(exit_path)
        w, h = exit_img.size
        click_x = exit_pos[0] + w // 2
        click_y = exit_pos[1] + h // 2
        pyautogui.moveTo(click_x, click_y, duration=0.05)
        time.sleep(0.05)
        pyautogui.click(click_x, click_y)
        print("Clicked exit.png")
    else:
        print("exit.png not found")
