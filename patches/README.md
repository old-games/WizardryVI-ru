# Patches

## Mass attack spells bug

```
seg000:9405                 push    bp
seg000:9406                 mov     bp, sp
seg000:9408                 add     sp, 0FFF4h
seg000:940B                 push    di
seg000:940C                 push    si
seg000:940D                 mov     bx, [bp+caster_ptr]
seg000:9410                 mov     al, [bx+1Fh]
seg000:9413                 sub     ah, ah
seg000:9415                 mov     [bp+target_group], ax
seg000:9418                 mov     al, [bx+20h]
seg000:941B                 sub     ah, ah          ; removed (NO-OP)
seg000:941D                 mov     [bp+target], ax
seg000:9420                 mov     ds:word_5116, 0
seg000:9426                 push    [bp+power_level]
seg000:9429                 push    [bp+spell_code]
seg000:942C                 call    sub_7816
seg000:942F                 add     sp, 4               ; add:
seg000:942F                                             ; cmp     byte ptr [bp+target_group], 0FFh
seg000:942F                                             ; jz      short loc_9452
seg000:9432                 push    ax
seg000:9433                 mov     ax, 2Ch
seg000:9436                 imul    [bp+target]
seg000:9439                 mov     si, ax
seg000:943B                 mov     ax, [bp+target_group]
seg000:943E                 shl     ax, 1
seg000:9440                 mov     bx, ax
seg000:9442                 mov     bx, [bx+43A8h]
seg000:9446                 mov     dx, [bx+si]         ; removed; this and following changes are NO-OP:
seg000:9448                 mov     bx, [bp+caster_ptr] ; removed
seg000:944B                 mov     cx, [bx]            ; removed
seg000:944D                 sub     cx, dx              ; removed
seg000:944F                 pop     ax                  ; add:
seg000:944F                                             ; sub     ax, [bx+si]
seg000:944F                                             ; mov     bx, [bp+caster_ptr]
seg000:9450                 add     ax, cx              ; add     ax, [bx]
seg000:9452                 mov     [bp+resistance_adjustment], ax ; We don't process groups' resistance here, which is a bug of the patch.
seg000:9455                 mov     ax, [bp+arg_2]
seg000:9458                 jmp     loc_B014
```

### Author's post

LAST EDITED ON May-17-10 AT 05:53 AM (Pacific)<br>
I may have discovered the source of the spell bug that causes monsters to resist the 7th level “attack all” spells. I’m working on seeing if there is an in-game fix or a way to patch the problem.

Here’s what I’ve got:

When a caster casts a spell on a target, the game rolls a saving throw for the target:
```
If(1d100-1 <= target_resistance – resistance_adjustment)
{
target resists spell
}
```
• target_resistance is the resistance % shown in Mad God’s editor<br>
• resistance_adjustment = (caster_level – target_level + caster_bonus)<br>
o caster_level is the caster’s level (or hit dice for monsters)<br>
o target_level is the target’s level (or hit dice for monsters)<br>
o caster_bonus = 3*(spell_level + power_level – 2)<br>
 power_level is the power level selected (1-6)

EDIT: I just discovered Mad God has a new version of his editor up that allows spell editing. What he calls "spell efficiency" is the same as what I called "resistance_adjustment"

The “spell bug” occurs when the game attempts to determine target_level. it tries to do an array lookup, which in c-code is essentially struct battle_participant** BATTLE_PARTICIPANTS{target_group}{target}.<br>
• BATTLE_PARTICIPANTS is an array of pointers located at 1110:43a8<br>
o index 0 is the party,<br>
o index 1 is monster group 1,<br>
o and so on, so that<br>
o BATTLE_PARTICIPANTS{0}{x} corresponds to individual x in the party (x=0 is upper left, x=1 is upper right, etc.)<br>
o BATTLE_PARTICIPANTS{1}{x} corresponds to individual x in monster group 1,<br>
o etc.<br>
• battle_participant is a 0x2C-byte wide struct,<br>
o offset 0x00 of which is the participant’s level or hit dice,<br>
o offset 0x20 of which is the index in BATTLE_PARTICIPANTS of the group that participant is targeting that round, and<br>
o offset 0x1F of which is the index in BATTLE_PARTICIPANTS{target_group} of the individual in target_group that participant is targeting that round

So if the party member in the upper right cast energy blast on monster 3 in monster group 1,
```
*( ((char*)BATTLE_PARTICIPANTS{0}{1})+0x1F)==1 //corresponding to monster group 1, and
*( ((char*)BATTLE_PARTICIPANTS{0}{1})+0x20)==3 //corresponding to individual monster 3
```

So for a party member casting a spell, the game attempts to determine the resistance_adjustment by doing the following:

NOTE: battle_participant* caster_ptr = &(battle_participants{0}{x}), where x is the index of the caster (0=upper left, 1=upper right, etc.)

```
function cast_spell(battle_participiant* caster_ptr, int spell_code, int power_level, …)
{
int target_group=(int) ( caster_ptr->target_group ); //executed as *( ((char*)caster_ptr)+0x1F);
int target=(int) ( caster_ptr->target ); //executed as *( ((char*)caster_ptr)+0x20)

register int caster_bonus=calculate_caster_bonus(int spell_code, int power_level);

resistance_adjustment = *caster_ptr – *(BATTLE_PARTICIPANTS{target_group}{target}) + caster_bonus;
//SHOULD == caster_level – target_level + caster_bonus. But it doesn’t always! See below for why this is.
…

}
```

The problem is that for character x casting an “attack all” spell, the game sets BATTLE_PARTICIPANTS{0}{x}.target_group==(char) (-1) == (int) 255

So, when the game does BATTLE_PARTICIPANTS{target_group}, this takes it to a random point in memory past the end of BATTLE_PARTICIPANTS (it happens to be the 5th-8th hex digits of the upper right character’s experience points). It then casts the result as a pointer and tries to index into it 0x2C*target bytes, which is another random point in memory. If the result is a large positive integer, target_level will be large and positive, and so resistance_adjustment will be large and negative. This makes the monster’s resistance effectively extremely high! While target_group is consistently 0xFF, target is inconsistent. It is usually 0x00, but it is occasionally 0x02.

You can test this easily. Just have the upper-right character change classes so his/her experience is zero. This should fairly consistently work, but not always, since target is sometimes 0x02. (*0x0000 == 0, but *(0x2c*2) is not necessarily == 0).

In fact, you can often avoid the bug if the 5th and 6th hex digits of your experience points are even and less than 0x56 or so (the numbers in *0x0000-*0x0056 seem to always be 0xff or less. So, divide the upper right character’s experience points by 65536 (decimal) and round down. If the result is even and less than 86 (decimal), your spells should usually work.

---

Here are some notes for others who want to verify. All memory addresses are what I got using dosbox to debug, and are only valid in the middle of a battle after you’ve selected “start fighting” and the animations have begun (I’m not sure which overlay this is in).

0138: b3e1 calls 0138: 9405 (the function described above). In this function,<br>
• caster_ptr is at bp+4,<br>
• spell_code is at bp+6,<br>
• power_level is at bp+8,<br>
• target is at bp-8,<br>
• target_group is at bp-6,<br>
• calculate_caster_bonus starts at 0138: 7816 (the return is stored in ax and pushed on the stack),<br>
• resistance_adjustment is at bp-0x0a<br>
Eventually 9405 calls 0138: 861e (call at 0138: 96ad). In 861e, resistance_adjustment is at bp+0x0e.<br>
Eventually 861e calls 0138: 8149 (call at 0138: 864d). In 8149, resistance_adjustment is at bp+0x10.<br>
• NOTE: 8149 is called once for each group targeted by a spell; this is where they should have calculated resistance_adjustment. I haven’t looked to see if there is any code in there that is somehow failing to overwrite the resistance_adjustment incorrectly calculated above<br>
Eventually 8149 calls 0138: 7ddc (call at 0138: 81c2). In 7ddc, resistance_adjustment is at bp+0x10.

In 7ddc, at 0138: 7e66, the game does
```
If(rnd(0 to 99) <= target_resistance – resistance_adjustment)
{
//target resists spell
}
```

Additional note about the function calculate_caster_bonus at 0138: 7816:<br>
This function does:
```
{
register int spell_level=*( ((char*)0xDF) + 6*spell_code)
return 3*(spell_level + spell_power – 2);
}
```

Where does the 0xFF come from?<br>
When you select “spell” when choosing a command, the game sets 0xFF as a default value for target_group at 0138: 7b86. This is overwritten for spells that have a group or individual target at 0138: 6f9a. However, this is never executed for spells that don’t have a group or individual target as a result of a jump to 0138: 6f9d at 0138: 6f64. Note that 0xFF is the target_group for more than just the “attack all” spells. Fire/ice/air shield, blink, create life/illusion/conjuration, and haste all have target_group==0xFF, and usually target==0x00. Enchanted blade, armorplate, and magic screen have target_group==0xFF, and target==0xFF.
