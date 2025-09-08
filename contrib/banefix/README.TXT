   http://members.aol.com/formula73/webpg/cheats.htm   (The Cheat Page)

Well fellow adventurers here it is, abet in a primitive form, a utility to
assist you in editing the standard character data on your awesome team of
heroes trekking thru the latest Sir Tech production, Bane of the Cosmic Forge.

Like it's predecessor (BANEPRINT), this utility doesn't recognize any
Health-Related Maladies - my team are all the picture of perfect health and
thus it's hard to spot any imperfections - nor does it worry about the 
equipment and swag junk you're carrying around.  I would hope to be able to 
get the health related malady isolated just by taking a group into back into
the dungeon and letting them get poisoned, stoned, blinded or killed off - so
look for an update sometime in the future.  The inventory situation is a
little more tricky.  Initial analysis that each item is identified by eight
bytes of data, and decrypting that amount of information will take time and it
is Christmas Eve after all!

Ok enough of the boring editorial stuff.  To get this utility out quickly I
bypassed including a lot of trivial code of that would ask you where and what
the name of the savegame.dbs or backup.copy is located and what file you
wanted to save the modified characters under - you know all those questions
about which drive, sub-directory and filename - and any checks to confirm that
the file exists and room (52,448bytes) is available on the selected save
drive.  Thus also not included were any warning messages about problems like
incorrect drive, sub-directory or file not found.  So you're asking how do I 
run this utility, and when will we get to the important stuff?

  C>banefix d:\sub-directory\filename.ext d:\sub-directory\filename.ext <cr>

  Since the latest backup of my super-heroes is on floppy drive B:, and
located in sub-directory SAVE6 and I wanted to save it to the same directory
with the name of modheros, I would use the following command:

  C>banefix b:\save6\savegame.dbs  b:\save\modheros.dbs <cr>

(assuming banefix.exe is in the current directory of drive C:, please ensure
that the second file name is different from the first or things could
really get messed up; BUT THEN YOU ARE PERFORMING THIS EDITING ON A COPY OF
YOUR SAVE GAME FILE?)

Once the command is entered, correctly, typically the drive will spin
typically for about 28 seconds on a 3.5" disk drive, 24 seconds on a 5.25"
disk drive, and 10 seconds on a hard disk before the screen will display a
list of 6 names (hopefully the six in your party), and the options to
finish/exit and abort program.

From there you use the UP/DOWN arrow keys to highlight a character to
modify.   Once the desired character is highlighted hit the carriage return
to view his/her stats and see what you want to change.

On the char stat page you use the LEFT/RIGHT arrows to select a grouping
of values to  adjust.  Again, once desired grouping is highlighted use the
return to edit those groups.  On the grouping page you will use the UP/DOWN
arrows to move a stat value up or down and the LEFT/RIGHT arrows to move
between stats.  When finished use the return key to exit back to the char
stat page.   The changes will appear on the char stat page as it's 
redisplayed.   When finished use the EXIT <cr> return option to get back to
the character selection menu.

   When finished with adjusting all character's values, use the FINISHED
option to write the new game data file to disk.

   The ABORT option exits without writing to disk, a safety valve for terrible
mistakes.


  Programming decison dicussion:

     Why didn't I worry about changing things like the race, sex, profession 
of the character.  Well there are complicated interactions between the
player's inventory and race, sex, and profession. Sure I can hard code that 
Valkyrie Female into a Valkyrie Male for example; but what effects will that
have on the +2Stuffed Bra she was wearing for body armor?  Much more detailed
analysis would have been necessary to make those changes and the program would
have been delayed for possibly days or weeks.

The one option you have is to change the player's attributes to all 18, and 
then ask the program to legally let you switch professions.  Save that game
and then come back and pump up the expierence points so you'll be right back 
where you were to begin; but with proper adjustments for equipment

    The one other item I could handle would have been enabling you to give
your magic user anyone of the 77 spells.  But the size of that page and the
bit manipulation would have added several days to the programming effort and
effectively you can accomplish the same task but either pumping up experience
or changing professional classes and then pumping up experience.

   While the cost of this utility is marginal, I will support corrections and
or improvements as needed.  This little utility has been brought to you free
of charge by the efforts of GEMail: AGNARI.

    http://members.aol.com/formula73/webpg/cheats.htm   (The Cheat Page)
