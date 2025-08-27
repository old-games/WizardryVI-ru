# Miscellaneous Facts and Spoilers

Version 1.41 - December 21, 2013<br>
by Stephen S. Lee (ssjlee@rawbw.com)

You may distribute this file freely, so long as you give proper credit to me.<br>
This was derived from the PC version; I make no guarantees about applicability
  to other platforms.<br>
Please feel free to e-mail me with corrections or suggestions.

## TABLE OF CONTENTS

1. Preliminary metagaming stuff<br>
   A. What this FAQ covers<br>
   B. Finding and playing a copy of Wizardry VI<br>
   C. Other sources of information<br>
   D. Wizardry VI bugs<br>
   E. Game difficulty<br>
   F. Early, middle, and late game
2. Character creation and development<br>
   A. Things set in stone at party creation<br>
   B. The power of class changing<br>
   C. Training and allocating skill points<br>
   D. Important spells to learn<br>
   E. Miss chance<br>
   F. Other things that rise with level<br>
   G. Places of note for developing characters<br>
   H. Notable NPCs that sell gear<br>
   I. Notable items that cannot be purchased
3. Character races<br>
   A. Human<br>
   B. Elf<br>
   C. Dwarf<br>
   D. Gnome<br>
   E. Hobbit<br>
   F. Faerie<br>
   G. Lizardman<br>
   H. Dracon<br>
   I. Felpurr<br>
   J. Rawulf<br>
   K. Mook
4. Character classes<br>
   A. Fighter<br>
   B. Mage<br>
   C. Priest<br>
   D. Thief<br>
   E. Ranger<br>
   F. Alchemist<br>
   G. Bard<br>
   H. Psionic<br>
   I. Valkyrie<br>
   J. Bishop<br>
   K. Lord<br>
   L. Samurai<br>
   M. Monk<br>
   N. Ninja
5. Suggested ways to build a party<br>
   A. Preplanned party for the entire game<br>
   B. General optimal party construction
6. Transferring to Wizardry VII<br>
   A. Statistics and skills that transfer to Wizardry VII<br>
   B. Items that transfer to Wizardry VII<br>
   C. Acquiring extra Diamond Rings and a bonus Cameo Locket<br>
   D. Using my party in Wizardry VII
7. Combat tips for certain monsters

## Preliminary metagaming stuff

### SECTION 1A - What this FAQ covers

There already exist excellent walkthroughs that will help you get through the
game.  This FAQ aims to provide more in-depth coverage of game mechanics and
correct errors, with a focus on helping you develop characters, while also
keeping walkthrough spoilers to a minimum; the advice herein should suffice to
beat the game kept on Expert level throughout.  Combat in this game can be very
difficult, and here you can also find advice on how to prepare your characters
for Wizardry VII and VIII.

The main two walkthroughs out there may be found at:<br>
http://www.gamefaqs.com/pc/564807-wizardry-vi/faqs/2008<br>
http://www.the-spoiler.com/RPG/Sir-Tech/wizardry.6.1/WIZ6.HTM

The latest version of this FAQ is always first uploaded to www.gamefaqs.com.

### SECTION 1B - Finding and playing a copy of Wizardry VI

Wizardry VI has been released as freeware on computer gaming CDs, although it
is in principle still copyrighted.  If you want a printed manual, or just want
to stay absolutely legal, you can always resort to eBay.  Be sure to include
the Ultimate Wizardry Archives in your search; it is a suite of the first seven
Wizardry games.

Wizardry VI has the most obnoxious copy protection scheme I have ever seen in
decades of gaming.  The Ultimate Wizardry Archives copy has this properly
patched out, but many copy protection patches do not properly bypass the copy
protection.  Any such crack will appear to work at first, but you will be
unable to ever hit a foe in melee, and the monsters will hit you especially
hard in return.

If you are running the game on a computer that isn't very old, I strongly
recommend using DOSBox to run the game.  It's more convenient, less prone to
bugs, should still be blazing fast, and allows you to play the game on any
modern computer platform.  The Web site for this excellent emulator is:
http://www.dosbox.com/

### SECTION 1C - Other sources of information

The best available utility to go with Wizardry VI is undoubtedly Mad God's
Cosmic Forge editor, which is a game editor and statistics viewer for Wizardry
VI, VII, and VIII.  It does not let you edit your characters, but it is
otherwise powerful enough to make full-blown game mods if you wish.  It is
still being actively developed; the latest version is 4.16.  Much of the
information in this document is drawn from that program.  The current main Web
page for Cosmic Forge is:
http://www.mad-god.webs.com/

Cosmic Forge includes exhaustive detail on every monster and item in the game
that no other source provides; this FAQ therefore will only describe monsters
and items of particular note.

### SECTION 1D - Wizardry VI bugs

Apart from the copy protection, here are several bugs that you should know
about.

#### (1) Carrying Capacity Bug
The Carrying Capacity Bug is arguably not really a bug, but most people believe
it is.  The carrying capacity of your characters is set at game start, and does
not change with increases in strength or class changes, as it does in Wizardry
VII.  If you want a fix for this, Mike Marcelais has made one available at:
http://www.the-spoiler.com/RPG/Sir-Tech/wizardry.6.1/FIXCC.ZIP

#### (2) Level 7 Spell Bug
The Level 7 Spell Bug will haphazardly render monsters immune to the four level
7 spells which damage all monsters: Nuclear Blast, Word of Death, Mind Flay,
and Deadly Air.  A patch for this bug may be downloaded here:
http://www.zimlab.com/wizardry/zip/w6wmexe.zip

Warning: this patch will cause Mad God's editor to not be able to properly read
the spell list or edit spells.

#### (3) Cannot Leave Loot Bug
Some items are flagged by the game as essential, and the game will not let you
refuse them or drop them (even you no longer have any use for them!)  If your
party's inventory is completely full and you are confronted with one of these
items, you have no recourse but to reboot the game.

If you always want to be able take items the game presents to you, you need to
have at least 7 free inventory slots.  Even with 144 total inventory slots,
this becomes limiting later in the game, as there is no place to stash items,
and you will accumulate a few dozen items you are not allowed to drop.

This bug can be exploited to gain extra copies of certain items.  See section
6C for details.

#### (4) Cannot Leave Skill Screen Bug
If a character gets a level, and has all skills maxed out, you will be unable
to distribute any skill points and be stuck in the skill point screen unless
you reboot.  This is similar to the bug in the original Wizardry VII before it
was patched.  This was probably not noticed in Wizardry VI because here, there
is no danger of this happening unless you do a truly ungodly amount of skill
training, class switching, and level grinding.  If you are particularly afraid
of this bug, you can just avoid actively training less useful skills like Axe,
Sling, Throwing, and Shield.

#### (5) Cursed Items Bug
Items which identify as Cursed may be bad, but they don't stick to your body as
they are supposed to.  This makes the Remove Curse spell useless, other than as
a way to gain some more Magic spell points.

#### (6) Maximum Level Bug
Wizardry VI does keep track of the highest level each character has ever
achieved, which it does to control level-up hit point gains, magic point gains,
and miss chance reduction (see section 2E and 2F for details).  However, it
sometimes doesn't do this properly; how and when this happens isn't clear.  It
may be as simple as the game only keeping track of the most recent level
change, but I have not fully tested this.

#### (7) Mass Status Condition Bug
Occasionally while in combat, the first character in your party will suddenly
lose a lot of hit points and stamina, and also get hit with a wide variety of
status conditions that typically do not include Stoned or Dead, but often does
include Hypnotized.  I'm not sure what causes this.

#### (8) Things which appear to be bugs, but are not

* If you cannot ever hit any monster in melee at all, you didn't crack the
  game's copy protection correctly.  (See section 1B.)

* The game should be very fast on either a IBM PC or compatible that is no
  older than a 286, or running DOSBox on any computer made since 2000.  The
  likely reason why the game may not appear to run fast is sound; the sound
  capability in this game is very primitive and causes a lot of slowdown.  It
  can be turned off; you won't be missing much.

* A lot of people believe that the lockpicking/chest interface represents some
  kind of timed videogame puzzle.  It's not; the red and green flashes only
  give you a rough idea of how good of a chance you have to bypass the lock or
  trap.  If the game is running properly, the red and green squares will flash
  too quickly to deliberately time manually, even on a very ancient computer.
  If you artifically slow down the game to time opening a lock or chest, you
  are not only cheating, you may also be one of those people who will then
  complain that Wizardry VI includes an action game element.  If you don't want
  that in Wizardry VI, then don't add it to the game!

### SECTION 1E - Game difficulty

You can change the game difficulty any time you can access the Disk option
screen.  Difficulty levels are Easy, Normal, and Expert.  Difficulty level only
affects combat, unlike in Wizardry VIII; it does not affect which particular
monsters show up either.  I believe game difficulty affects the ability of
monsters to hit you, and their resistance to magic.

It definitely affects the number of monsters that appear.  At Easy, each
monster group has one fewer monster, to a minimum monster group size of one
monster.  At Expert, each monster group has one more monster, to a maximum
monster group size of nine monsters.  This includes boss monsters; you will be
fighting two of each boss at Expert level!

### SECTION 1F - Early, middle and late game

Here's a rough definition of "early", "middle", and "late" game, and what they
entail.

* Early game: this encompasses all of the Castle: the ground floor, second
  floor, basement, and all seven of its towers including the Belfry.  This also
  includes the Hazard Area adjoining the Castle Basement.  The early game
  encompasses basic outfitting and your characters learning not to be hopeless
  in combat, and learning some facts about this apparently deserted castle that
  isn't actually deserted.

* Mid game: this comes in two major stages that comprise about half of the
  game.  The first major stage starts in Giant Mountain and the Dwarf Mines,
  and continues into the Amazulu Pyramid.  This includes the first magic-
  restoring fountain; your party starts to approach higher levels and starts
  acquiring powerful magical items.

  The second major stage revolves around the River Styx, and includes all the
  adjoining new areas: the Tomb of the Damned, the Hall of the Dead, and the
  Swamplands.  Potent tier 4 weapons and armor start showing up at the end of
  this second stage.  This stage and the midgame end with the second encounter
  with the King in the Hall of the Dead.  This critical point marks both the
  branchpoint for the various possible endings, and is a Point of No Return:
  you will be unable to return to any of the early or midgame areas until you
  win the game.

  It is, incidentally, totally unclear that this point is a branchpoint for the
  various possible endings.  Without spoilers, you not only have to figure out
  that someone is completely lying to you, you then have to somehow refuse
  assistance from that source when it's not clear this is possible at all.

* Late game: this starts with your escape from the prisons underneath the
  Temple of Ramm, continues with a tour of the Enchanted Forest, and ends with
  an assault on the Temple of Ramm.  Your characters' levels will rise to about
  the high teens or low 20s by the end, and there are many difficult combats.

  One last point: even with spoilers, many people (including the people who
  ported this game into Japanese on the Super Nintendo) cannot figure out who
  the truly evil opponents in the game actually are.  NPCs will drop hints that
  while the King is killing lots of things, your party is doing that too.  Keep
  in mind that you're invading the realm of beings that keep to themselves.
  While this can't be (and isn't) really faulted since the place seems deserted
  at first, not to mention that the game deliberately doesn't make clear who is
  evil anyway, you should give the implications of this some thought.

## Character creation and development

### SECTION 2A - Things set in stone at party creation

Regardless of what your long-term plans for your party are, there are many
things which are impossible or very hard to change after you create your party.
Statistics (other than karma), hit points, spell points, skill points, and
spells can always be gained, and the same goes for many items.

#### (1) Race

There is no way to change race in this game; you can only change race in later
games by outright replacing a character.  An overview of races, including
considerations of transferring characters to later games, may be found in
Section 3.

#### (2) Sex

There are no girdles of opposite gender or equivalent anywhere in Wizardry VI
or its two sequels.  A female character will get -2 Strength, +1 Personality,
and +1 Karma at the start of the game.  The Strength and Personality modifiers
do not apply to subsequent class changes and are thus only relevant early in
the game, unless you apply the bug fix for the Carrying Capacity Bug in Section
1D(1).

Female characters have many advantages over male characters: (a) Karma is by
far the hardest statistic to increase; while it doesn't have much effect, and
in fact in a few cases you may want a lower Karma score, until you reach the
Wizardry VII late game there is no easy, reliable way to increase Karma.  (b)
There are many pieces of equipment, some powerful, that only females can use;
this extends into Wizardry VII and VIII as well.  There are only two items in
all three games restricted to males, and the only one in Wizardry VI and VII is
found only in the Wizardry VI endgame.  (c) The powerful Valkyrie class is only
available to females; not only is it a good class in its own right, it is an
excellent intermediate class for class-changing.

For these reasons, an optimized party includes no more than 1-2 male
characters. The single male-only item is potent and transfers to Wizardry VII
freely, but you can only ever get one.  The only other reason to include male
characters in your party is ...

#### (3) Carrying Capacity

Starting carrying capacity (CC) is determined by your starting Strength and
Vitality.  Each point of Strength allows 9.0 pounds of CC; each point of
Vitality allows 4.5 pounds of CC.  Faeries additionally get a 1/3 penalty to
CC.

CC is not a big deal for a majority of the game.  However, as you gather quest
items that cannot be dropped (some heavy) and heavy gear, this starts to become
a serious limitation, and you will probably find that you will start taking AC
penalties for carrying around too much stuff by the late game.

You may consider CC not changing to be a bug; to fix this, see Section 1D(1).
If you do not, then you will want to put as many starting points into Strength
and Vitality as you can to improve your carrying capacity.  The -2 Strength
penalty females get at the game start is a significant liability in this case.

You will generally want as many non-faeries possible in your party to have a CC
of at least 200 pounds (equivalent to 15 Strength and 15 Vitality) on average.
Section 5B describes my recommended way of achieving this.

#### (4) Mana regeneration

The rate of mana regeneration is VERY low in this game; even a complete
uninterrupted rest will not restore very many magic points!  Fountains that
increase magic points are therefore highly treasured; all such fountains are
noted in section 2G.

One way of dealing with this is to hack the game to artificially increase mana
regeneration.  Mad God's Cosmic Forge utility will allow this.

Regardless of whether you apply this hack or not, your characters' base mana
generation rates are set in stone at game start.  Each of the six magic realms
has its own regeneration rate.  In the order Fire, Water, Air, Earth, Mental,
and Magic, they are as follows for the class that a character starts as:

|            | Fi | Wa | Ai | Ea | Me | Ma |
| ---------- | -- | -- | -- | -- | -- | -- |
| Mage       |  3 |  3 |  2 |  2 |  2 |  3 |
| Priest     |  2 |  2 |  3 |  3 |  2 |  3 |
| Alchemist  |  3 |  2 |  3 |  3 |  2 |  2 |
| Psionic    |  2 |  2 |  2 |  2 |  4 |  2 |
| Bishop     |  1 |  1 |  1 |  1 |  3 |  3 |
| All others |  1 |  1 |  1 |  1 |  1 |  1 |

- Faeries get a +1 bonus to each of the six realms.
- Lizardmen get a -1 penalty to each of the six realms.  This cannot cause
  regeneration to drop below 1, but it is still a reason not to have a
  Lizardman in your party!
- A high starting Vitality (requires at least 16) grants a +1 bonus to each of
  the six realms.
Note that regeneration rates are different in Wizardry VII.

Thus, in order for all characters to have a decent mana regeneration rate, all
characters need to start as either faeries, as one of the pure spellcasting
classes, or have high starting Vitality.

#### (5) Equipment

Your starting class also grants you equipment.  Most of this equipment is very
rapidly superseded by more powerful weaponry and armor; if you know where to
go, you can both afford and purchase superior equipment within 5 minutes of
starting a new game.  However, there are some notable starting bits of
equipment that are not so superseded:

* Mitre - the Bishop starts with this helmet that is -2 to AC, and for a Priest
  or Bishop it's hard to improve on.  There is only a single place to find
  another Mitre in the game; it's a possible random item in one of the chests
  in the Hazard Area adjoining the Castle Basement.  The Mitre is not too big a
  deal, though, and better equipment is considerably easier to come by in
  Wizardry VII.

* Ninja armor - the Ninja starts out with a Ninja Cowl, Ninja Garb (U), Ninja
  Garb (L), and Tabi Boots, each of which can only be equipped by a Ninja and
  provides -3 AC.  For the most part, this is the best the Ninja can ever
  equip, though the Ninja relies mostly on Ninjutsu and high Dexterity and
  Speed to provide AC.  Ninja enemies late in the game also have a good chance
  of dropping a piece of ninja armor, so starting with ninja armor isn't that
  big a deal.

* Shadow Cloak - the Psionic starts out with it; it may be equipped by Thieves,
  Bards, and Ninja, but oddly not Psionics themselves.  It provides -1 to base
  AC, but no other bonuses.  It's not a particularly strong item, but it takes
  a while for miscellaneous equipment to definitively pass it by, and there is
  only one place after party creation where you can find a Shadow Cloak.

* Lute - the Bard starts out with the Lute (the same as the Poet's Lute in the
  sequels).  This is an unending source of Sleep spells that only Bards can
  use; it is extremely powerful in the early and mid game.  The only way to get
  another Lute in Wizardry VI is as a random drop from a Miner Dwarf or Major
  Dwarf; in either case, the probability is only 1 in 580.  This rare
  opportunity also doesn't come until you reach the midgame; you will thus want
  to start out with at least one Bard for this reason.  The Lute also transfers
  to Wizardry VII and VIII.

### SECTION 2B - The power of class changing

Class changing is a powerful way of enormously empowering your characters in
Wizardry VI and VII.  If you don't do it at all, you will probably find the
late game challenging even at Normal difficulty.

When you change class, a character will immediately drop to zero experience
points.  Statistics will drop to the minimum possible for the race/class
combination, though Karma will not be changed.  Hit points, spell points, skill
point investments, miss chance (section 2E), and spells are all retained.

The major losses upon class changing are:

* Statistics, other than Karma.

* The ability to use any equipment the old class could that the new class
  cannot.

* Multiple physical attacks.  You gain extra physical attacks and the ability
  to attack with an off-hand weapon as you gain levels; this all vanishes with
  a class change and must be re-earned.  This is what causes the biggest hit in
  physical combat effectiveness after a class change.

* Resistances from level.  Higher levels grant you additional magical
  resistances; both class-based and level-based resistances are reset upon a
  class change.

* The ability to cast spells at higher power levels.  Casting a spell of spell
  level X at power level Y requires you to be at least level X+Y-1, if Y>1.

* Casting a spell that requires Oratory is less likely to be effective if you
  switch to a class that does not have Oratory as a native class skill.  This
  makes classes that use Alchemy less useful than you may think.

However, you gain the following benefits:

* Experience points drop to zero.  Since the number of experience points needed
  to gain a level increases exponentially before level 12, this gives you the
  opportunity to gain multiple additional level-ups.  As an example, you might
  think that a Bishop would be a good class, but it really isn't as good as it
  appears; you can train a Priest to 10th level, switch class to Mage, and
  train back up to 10th level before a Bishop can reach 11th level; see next
  point for why this is such a large advantage.

* Each new level so gained will give you 4+1d6 (5 to 10) new skill points, and
  in most cases a chance at learning a new spell.  Some skills and a majority
  of spells can in fact only be learned in this way.

* You will be able to learn spells from all four schools this way, although the
  Psionic school doesn't have many unique spells to offer.  You can also have
  everyone in your party learn the very useful Ninjutsu and Kirijutsu combat
  skills; once you have a single point put into them, you will then be develop
  those skills as any class.

* The rapid level-ups mean you will rapidly re-gain statistics and most of the
  benefits that were lost upon class change.

* Both weaponry skill and miss chance (see section 2E for full explanation) are
  unchanged, so accuracy in physical combat is not much affected.  This can be
  a liability if you are changing from a pure spellcaster to a front-line
  fighter!

Even one or two class changes per character will grant you a number of skills
and spells that you would otherwise not be able to get.  Each additional class
grants you still more power.

You will want to avoid the Fighter and Thief classes in class changes, as they
cannot learn spells.  You probably also want to avoid classes like Mage and
Priest that have low barriers to entry, as these low barriers to entry make
subsequent class changes harder to attain.  Alchemists, Psionics, Bishops, and
all hybrid fighter/casters are reasonable-to-strong choices for switching to.

You will generally want to have at least one Bard in your party at a time until
you reach the late game.  Only Bards are able to use instruments; having the
Music skill is not enough, unlike in Wizardry VII or VIII.

Once you have reached the point where you are choosing classes for the long
haul, it's best to choose exclusively hybrid fighter-casters.  This is because
once you have improved your magic skills enough, hybrids are almost as good at
casting spells as pure spellcasters.  In exchange, hybrids get the ability to
equip better weapons and armor, more hit points, better miss chance
improvement, and better magic resistance, making them a superior choice
overall.

If you are having a hard time switching to a desired target class, it may be
easier to switch to a different class first and start again from level 1.  The
Ranger and Valkyrie classes do not require you to have any stat above 11, and
it should not be hard to become eligible for these classes as any race.  These
classes require moderate scores in most stats, making a subsequent switch to a
class requiring high stats for a given race easier.

When to make class changes is a personal preference, but I would wait until at
least level 5 (except for the initial level 1 class change described in section
5B), but also before level 11 at the latest, since that is when levels start
requiring a lot of experience.

The major difficulty with multiple class changes is making sure your statistics
get high enough for another class change to another decent class.  This will
require a good deal of saving and reloading to get good level-ups (unless you
hex-edit your save files).  The boredom associated with this is the best reason
not to make more than a few class changes.  In particular, once everyone is
guaranteed access to Ninjutsu, Kirijutsu, and the best spells listed in section
2D, the practical benefit of further class changing drops dramatically.

### SECTION 2C - Training and allocating skill points

The maximum number of total starting skill points is 18; this includes points
that are automatically distributed to primary skills.

All weapon skills, excluding Shield, will train rapidly simply from constant
use in combat; they actually train rapidly enough that they shouldn't be more
than a minor factor in weapon selection.  There isn't much point to manually
placing skill points into weapons skills.  (A minor exception applies to
Faeries in warrior classes that you plan to transfer to Wizardry VII.  Faeries
cannot train Axe or Shield skills by practice, so if you want to max out the
number of skill points transferred, you have to add such points manually.)

Shield skill will train in combat for any shield-equipped character who gets
attacked.  The skill will train much faster if the character Blocks instead of
attacking or Dodging.  Shield skill is only of any use at low level, before you
have enough weapon speed to attack with an off-hand weapon; once you can get an
attack with an offhand weapon you should equip one.

Scouting will not go up unless level-up skill points are devoted to it.  The
Detect Secret spell functions as if your party has someone with Scouting 100,
and if you're paying attention it's often clear enough where buttons and places
you can search to find more things are anyway, so this is not a skill you
should prioritize for development even if you are playing without a
walkthrough.

Music will go up fairly quickly for a Bard that plays instruments regularly in
combat, which any Bard should be doing anyway.  It is not however of any use in
Wizardry VI to non-Bards, although it is a very nice skill to have on multiple
characters if you transfer them to Wizardry VII.

Oratory will train up quickly enough on its own for any caster using Mage,
Priest, or Psionic spellbooks.  Only spells cast in combat count, although
low-level spells cast at power level 1 are all you need to train by practice.
You will eventually need 75+ Oratory to reliably cast higher-level spells in
combat at a good power level.

Legerdemain will never train by practice and requires allocation of level-up
skill points.  However, you don't need many skill points in it to make Stealing
from NPCs reasonably effective.  20-25 or so is plenty to be able to steal with
some reliability from Mai-Lai.  Don't forget to add at least 1 point to it for
every character that can, as that way you'll still have it available for adding
to even if you class change away.  When Stealing from NPCs, you must have space
for any stolen items in your main inventory, not your Swag Bag; failure to have
such inventory space will silently cause all attempts to steal items to fail.

Skulduggery can train from practice, but it will only go up from practice if
the character using it has Skulduggery as a native class skill.  However, it
does so rather slowly as you can only train it on locked doors and trapped
chests, and there is a finite supply of these in the game.  It is possible to
back up your save game, try to open a door, check for a skill increase, and
then restore from backup if you jammed the lock.  If you're disarming a chest
to train Skulduggery, you can just reload if you trigger the trap or
successfully open the chest.  This process is tedious enough that you may want
to manually add points to Skulduggery, especially early in the game when locked
doors and chests are most abundant.  Examining a chest for traps will not train
Skulduggery, unfortunately, even though Skulduggery does increase the
effectiveness of doing so.  In any case, you don't need more than about 40
Skulduggery, even in the late game.  You can get by with even less; the Knock-
Knock and Divine Trap spells are reasonable substitutes once you can cast them
at higher levels without missing the spell points too badly.

Ninjutsu can train from hiding in combat; it can go up from practice even if
the character using it does not have Ninjutsu as a native class skill, as long
as the character has at least 1 point of Ninjutsu to begin with.  Hiding in
combat naturally makes the character much harder to hit, so it's a useful skill
to train on all of your characters.  High levels of Ninjutsu will also improve
the base AC of Monks and Ninja.

Artifacts skill trains from using items with magical powers in combat.  Unlike
in Wizardry VII and VIII, it does not help you to identify items, nor is there
any way to recharge items, so it's not a very useful skill.  It is, however,
useful and fairly easy to train up for characters destined for transfer to
Wizardry VII.  The easiest way to do this is to use magic stix (sparklers,
icicles, firecrackers, etc.); be sure to Use them as spellcasting items rather
than Throw them as thrown weapons.  This will train Artifacts skill fairly
rapidly, and is a good reason to keep the Caterpillar around, as he is a good
source of magic stix.

Mythology skill trains very slowly on its own.  Knowing exactly what you are
fighting is useful, but not so useful that it's worth putting skill points into
Mythology.  You can usually tell that you're fighting a more powerful version
of a local monster by the fact that there aren't as many of them.  The biggest
problem is distinguishing between Skeletons and Skeleton Lords in the Hall of
the Dead; the former aren't so bad, the latter can be deadly.  Mythology skill
also does not transfer to Wizardry VII.

Scribe skill only helps you use scrolls, which is nearly useless.  You can
still train this in combat (even with scrolls useless in combat like Knock-
Knock); you can always obtain scrolls from Queequeg if you need a source of
scrolls to train with.  The skill does transfer to Wizardry VII, but it's not
worth the hassle just for Wizardry VI.  Even in Wizardry VII, Scribe is mostly
useful because it contributes to Artifacts skill transfer to Wizardry VIII.

The magical skills (Alchemy, Theology, Theosophy, Thaumaturgy) cannot be
trained and can only ever go up with level-up skill points.  These skills are
generally the best place to invest level-up skill points.  Learning Level 2
spells requires 18 skill; Level 3, 36; Level 4, 54; Level 5, 72; Level 6, 90;
and Level 7, 98.  Reaching 36 skill is top priority for any character that can
cast spells.  Most of the really important spells only require this level of
investment; additionally, level 3 spells are the highest level spells that can
transfer to Wizardry VII.

Kirijutsu cannot be trained on its own; it requires manual allocation of skill
points.  Each point in Kirijutsu adds 0.2% chance to critical hit chance, up to
20% at 100 skill.  This stacks additively with any Critical ability that your
weapons may have.  Ninja have an additional bonus to this as a class ability.
Monsters with Death resistance (see section 2F) resist critical hits.  Any
class able to do so should prioritize putting at least one point here, as once
you do so you will be able to add points here as any class.  After magical
skills, this is the best place to put skill points.

Other notes on training skills:

* All classes other than Fighter have one or two skills that may automatically
  be allocated skill points upon level-up.  These skills are listed under
  "Primary Skills" in section 4 by class.  This automatic allocation can occur
  if the skill in question is below 51; it will take a random number of skill
  points from the normal 4+1d6 level-up skill points for this purpose.  As this
  automatic allocation may prevent you from assigning skill points to where you
  wish, you may wish to train these skills by practice to reduce or prevent it.
  Primary skills that are weapon skills are thus a priority to train to 51 by
  practice, as it is otherwise a waste of precious level-up skill points.

* It is perfectly possible to practice skills in combat, then run away from the
  opposition before you kill the last monster so that you gain no experience.
  You may want to do this if you want to train skills up to 51 for preventing
  automatic redirection of level-up skill points to Primary Skills.  The only
  drawback is that it can be very tedious and time-consuming.

### SECTION 2D - Important spells to learn

Here is my opinion on which spells are best to learn.  Any spell may be learned
with an appropriate level-up and sufficient magical skill.  It is best not to
take a spell that is easy to acquire from a spellbook purchased from an NPC;
these are listed in Section 2H.  Spells that can be learned from a spellbook
that cannot be purchased from an NPC are listed in Section 2I.

Learning spells from a spellbook requires the spellbook to be usable by that
particular class; this normally means any caster or hybrid able to eventually
learn that spell, excluding Ninja, although several exceptions exist.  The
requirement for learning a spell from a book is different.  Magical skill is
not what is checked; instead, you must have a character level of a minimum of
twice the spell level.

It should be noted that status inflicting spells are very potent in the
Wizardry series compared to other CRPGs.  Spells that inflict and cure these
are thus much higher priority.  Pure damage spells are lower priority than you
might expect, partly because of the effectiveness of status inflicting spells,
and partly because physical combat becomes very strong starting around halfway
through the game.

Spell desirability is also mediated by which realm it is in, since spellcasting
uses six independent pools of magic points.  The Magic (yellow) realm is by far
the most versatile, with the game's only healing spells and a wide variety of
utility spells; Magic spell points are precious right from the start of the
game.  Fire (red) has the best offense, with Water (dark blue) and Air (purple)
also being of considerable use.  In the long run, the other two realms of Earth
(green) and Mental (light blue) are the ones you are most likely to have a
surplus of spell points in.

#### BEST SPELLS (as many characters as possible should get these):
* Heal Wounds - duh.  Any character that can learn this should take it as soon
  as possible, as there isn't a spellbook that can teach it, and you want to
  get growth in Magic spell points going as soon as you can.
* Cure Paralysis - getting paralyzed happens frequently enough for this to be
  valuable to learn for your whole party.
* Cure Lesser Condition - this will fix nausea, sleep and blindness, all of
  which happen frequently, all of which can hit multiple characters in a single
  monster action, and all of which are highly debilitating.
* Sane Mind - getting hit by insanity is particularly nasty; this is the
  countermeasure.  This isn't a concern early in the game, so this isn't a
  spell you need to hurry to get, but you do want to make sure you have it by
  the second half of the game.  (This will NOT work on characters that are
  hypnotized; there's no cure for that I know of, other than waiting it out.)
* Dispel Undead - you can start to encounter undead once you start exploring
  beyond the castle.  Undead tend to be nasty, and this spell has a good chance
  of working even on powerful undead and bosses.  It can dispatch entire groups
  of zombies and Skeleton Lords, both of which can be very nasty if you don't
  get rid of them fast; it's quite possible to meet 5 groups of zombies or
  Skeleton Lords, so ideally you will eventually have at least 5 characters who
  can cast this.  You generally only need to cast this at a level sufficient to
  affect all undead in a group; more power does increase the chance of the
  spell working, but it's not by much relative to the cost of doing so.
* Astral Gate - this high-level spell isn't of any use until you reach the
  River Styx, but from that point on it's effectively Dispel Undead for demons
  and devils.  Higher-level demons tend to resist it, but even low-level
  demons are very dangerous if you let them cast spells.
* Blinding Flash - this is cheap, is relatively unlikely to be resisted, does
  an excellent job of neutralizing monsters that only have physical attacks,
  and sometimes makes even a spellcaster fumble.  This spell is also very
  effective against your party!
* Silence - this will often prevent enemy spellcasters from ruining your day.
  Just keep in mind that it won't stop enemy Alchemists, though it IS effective
  against alchemical spells cast by non-Alchemist enemies.
* Sleep - early on, a Bard is often enough to cause all opposition to fall
  asleep, so you don't need to learn this right away.  However, in the midgame,
  having multiple people with this spell becomes very useful, and it's still
  modestly effective even in the endgame.
* Anti-Magic - unlike Silence, this debuff cannot be resisted by monsters, so
  it's a great way to prevent a nasty spellcasting group of monsters from
  wasting you.  It's a pity that's it's too expensive to cast in every single
  combat late in the game!  It's also a level 5 spell found only in the Mage
  spellbook, so it's a pain to learn for more than a few characters.  It is
  easily the best spell of 4th level or higher, on the other hand; make a point
  of learning it before you hit the late game.
* Enchanted Blade (only need 1 character with it) - combat buffs that can be
  cast outside of combat are good to have.
* Armorplate (only need 1 character with it) - ditto.
* Magic Screen (only need 1 character with it) - ditto; particularly good to
  cast before major fights.  Once you hit the late game, you will want this
  active all of the time.

#### GOOD SPELLS (not as high priority as above, but still nice):
* Level 7 damaging spells (Nuclear Blast, Word of Death, Mind Flay, Deadly Air)
  — should be self-explanatory, but a few notes.  First note the Level 7 Spell
  Bug in Section 1D(2); this can randomly prevent these spells from working at
  all if you don't patch it.  These spells also don't work completely reliably
  at power level 6, even at high levels with maxed out skills and stats; having
  multiple characters cast these spells at power levels 4 or 5 is a lot more
  reliable.  These spells also require a huge investment in skill points to be
  learned; they don't provide the best return on investment compared to the
  better spells above, or a good selection of the lower-level group damage
  spells.  Also note that Mind Flay does not actually inflict insanity on
  monsters, contrary to what the manual claims, and unlike the lower-level
  Mental attack spells.
* Energy Blast / Chilling Touch - there is little difference between these two
  spells early in the game when they're most useful.  Your party will struggle
  with physical weapon accuracy early in the game, so these are nice to have
  for key fights until your melee fighters become buff.  Take Energy Blast
  first to build up those scarce Fire spell points, and also because it can't
  be learned from a book unlike Chilling Touch.
* Fireball - cheap and effective Fire group damage spell; inflicts good damage
  for its cost.  As many characters as possible should learn either this or
  Fire Bomb, as a utility group damage spell.
* Iceball - very effective Water group damage spell for the price.  It's the
  only Water group damage spell, which makes it desirable for as many people as
  you can learn it for.  This spell and Fireball are generally the best group
  damage spells for dispatching whole groups of vulnerable enemies.
* Deep Freeze - this is a good spell against single tough targets, notably
  fire-based bosses.
* Stink Bomb / Toxic Vapors / Noxious Fumes - the nausea these spells can
  inflict makes them good combination blow spells.  They're expensive for a
  good reason!
* Poison / Poison Gas / Deadly Poison - poison is often an effective way to
  inflict continuous damage on even tough monsters or bosses.  Deadly Poison in
  particular is a potent albeit costly way to dispatch vulnerable single foes.
* Blades - this isn't as effective as other group damage spells, but it's a
  good way to put all those extra Earth magic points to use.  As many
  characters as possible will want either this or Acid Bomb, as an Earth group
  damage spell.
* Acid Splash / Acid Bomb - monsters tend to have poor acid resistance.  In
  some cases, it's the only spell damage type that works at all.
* Mental Attack / Psionic Blast - inflicting both damage and insanity sounds
  really nice, and it is.  However, monsters tend to have higher resistance to
  mental attack compared to other damage types, and you have to invest in the
  Psionic spellbook for these; that is a spellbook that doesn't have all that
  much to offer.  On the other hand, you will tend to have a surplus of Mental
  magic points.
* Stamina - you can generally just rest anywhere to restore depleted stamina
  rapidly, so this isn't as useful to have as Heal Wounds.  Combat is sometimes
  protracted enough that characters can have reduced combat effectiveness or
  flat-out drop from exhaustion, though, so you'll want to have this around.
* Cure Poison - poison doesn't usually debilitate characters in combat, making
  this lower priority compared to other condition cure spells.  You do still
  want to be able to cast this in combat on anyone who gets hit by a Deadly
  Poison spell and survives, as that level of poison can cause dozens of damage
  per round.
* Conjuration / Illusion / Create Life - summons help that not only attacks the
  enemy, but takes blows that so your party doesn't.  Good against bosses and
  in many endgame combats.  Generally, Conjuration gives you better added
  offense, and Create Life gives you better meat shields; Illusion isn't quite
  as good as the other two, if you are gauging how much to invest in Theosophy.
* Fire Shield - there are enough monsters that use fire attacks to make the
  turn and spell points needed for this useful.  These monsters include
  high-level demons and devils, and many boss monsters.
* Haste - a good spell to throw in major battles to make sure you have the
  initiative in later rounds.
* Missile Shield - note that this not only blocks thrown daggers, shuriken, and
  arrows, but it even blocks thrown boulders, making it effective against
  giants, Rocks of Rumble, the Guardian of Rock, etc.
* Air Pocket - protects against enemies that cast nasty cloud spells (mostly
  Alchemist spells, but also Firestorm).
* Purify Air - removes those nasty cloud spells cast on you by your foes.
* Armor Shield - cheap; at power level 6, it can provide enough protection to
  drastically reduce or eliminate outright physical damage threats to one
  character.  Particularly useful to cast on front-line Samurai later in the
  game.
* Bless - cheap, and provides a good party-wide boost to both ability to hit
  monsters and Armor Class.  The only thing keeping this spell from being
  must-have is that there is a guaranteed Bard instrument that can cast it.
* Armormelt - a useful debuff, since it can't be resisted.
* Hold Monsters - a better version of Sleep, but it's more expensive; regular
  Sleep magic is often plenty adequate.
* Detect Secret - nice to have if you're playing unspoiled and don't want to
  invest a lot in Scouting.  Pointless if you're playing with a walkthrough.

#### NOT SO GOOD SPELLS (at least they aren't useless)
* Prismic Missile - its randomness can be fun, but is also unreliable.  This is
  resisted by Light resistance and not Fire resistance, however; perhaps that
  could give it a good use somewhere?
* Lightning - Fireball is a much better use of Fire spell points.  Better than
  nothing for a pure Priest spellbook user, though.
* Firestorm - rather expensive and does damage over time, and doesn't inflict
  any condition like other such spells; there's usually a better use for Fire
  spell points.  It can be tempting to take just to increase maximum Fire spell
  points, since those are the hardest to come by.
* Whirlwind - expensive and rather ineffective for a group damage spell; even a
  pure Priest spellbook user probably wants to use Air spell points for other
  purposes.
* Make Wounds / Magic Missile - Unlike elemental spell points, Magic spell
  points are too valuable to spend on mundane damage spells.  You may want to
  take Magic Missile just to jump-start Magic spell point growth, however.
* Ice Shield - there aren't many monsters in the game that use cold attacks and
  where combat lasts long enough that this is worth a turn casting.  You're
  generally better off just throwing Fireball or Sleep spells.
* Blink - the protection is nice, but somewhat random, and burns up valuable
  Magic spell points.  You can duplicate much of the effect by instead Hiding,
  which doesn't cost any spell points.
* Slow - not as strong as other debuffs, and Haste on your own party is a
  better way of making sure you have the initiative.
* Paralyze / Web - reasonably reliable, it's just that it only affects one
  target!
* Itching Skin - unlike other mass debuff spells, this one doesn't have a
  strong effect.
* Charm - not of much use, unless you are the type who both doesn't like to
  reload saved games and wants to steal from NPCs.
* Death Wish - this uses a huge number of valuable Magic spell points, it is
  difficult to cast at a high power level, and most really nasty foes are
  unlikely to be hit by it.  This spell works better for monsters, since they
  don't have to worry about spell costs, and it's hard for you to get Death
  resistance.
* Death - this isn't unreliable, but it's expensive and single-target, and
  generally not as effective as Deep Freeze or Deadly Poison.  It also does not
  work well against later bosses.
* Lifesteal - again, not that unreliable, but it is expensive for a single-
  target spell, and it uses valuable Magic spell points.  This is another spell
  more effective in the monsters' hands.  Like Death, it does not work well
  against later bosses.
* Levitate - there aren't many places where this does much good, and there's an
  alternative in the one notable place where it's useful in the midgame.
* Identify - this does give you a lot of information about an item, if you're
  not reading a strategy guide or using Mad God's utility.  In Wizardry VI, it
  never needs to be cast above power level 1.
* Mindread - this spell will let you know a subject an NPC will chat about.
  It's not that useful if you either have a walkthrough, or pay close attention
  to clues and NPCs.  It's most useful in the end game, if you can't figure out
  where to go next; cast it on the Queen of Faeries to get on the right track.

#### USELESS SPELLS (well, at least learning them increases max MP)
* Resurrection - raising a dead character reduces Vitalty by 1 permanently.
  Even if you choose to resurrect rather than restore a saved game, items that
  cast Resurrection aren't hard to come by.
* Cure Stone - same as for Resurrection.
* Locate Object - if this does anything useful at all, it completely eludes me!
* Remove Curse - useless owing to the bug described in section 1D(5).

### SECTION 2E - Miss Chance

Miss chance is an influential statistic, but it is neither documented nor ever
shown in the game.  You will need to use Mad God's utility to see this.  It is
the largest contributor to accuracy in physical combat, and is actually
somewhat more important than weapons skill.  It does not affect number of
attacks or damage; those are primarily mediated by character level, Dexterity
and Speed (number of attacks), and Strength (damage).

Miss chance works like THAC0 from AD&D 1st and 2nd edition, except that the
important die roll uses a 100-sided die, not a 20-sided die.  Miss chance for
every class starts at 100 for every character, regardless of race or class.  It
is modified by weapon skill, the to-hit modifier of the weapon used, the
specific attack mode you employ, and the effects of status conditions like
Irritated.  +1 to hit appears to be the equivalent of -5 to miss chance.  Like
THAC0, the lower your miss chance is, the more likely you are to hit a monster
in combat.

Miss chance can go down if a character gains a level, but only if the following
three criteria are met: (a) The level attained is not higher than 20; once a
character reaches 21st level, that character is forever barred further miss
chance reductions. (b) The level attained is not lower than the highest level
the character has ever achieved. (c) Base miss chance may not drop below 0.

Example: You create a brand new.  At level 1 she starts with a miss chance of
100 like everyone else.  You advance her to level 8; at each level-up, she gets
a reduction in miss chance (1d4+1 from being a Valkyrie). You then switch her
class to Psionic.  While her level drops to 1, her miss chance remains
100-7d4-7.  You then advance her to level 11.  Her miss chance does not change
until level 8, when she gets a second level 8 miss chance reduction (1d3 for
being a Psionic).  The level-ups from 9 to 11 also each reduce her miss chance
by 1d3, making her miss chance at the end of all this equal to 100-7d4-4d3-7.

If you are minmaxing your characters by changing class multiple times, this

ability to double-dip miss chance reductions at maximum achieved level is
something to keep in mind: if you are doing many class changes you should try
to do so at exactly the highest level that character has achieved.  This target
can go upward as you reach new areas that give more experience.  The game
however sometimes messes up keeping track of what your highest level achieved
is, which makes getting miss chance reductions easier (the bug described in
section 1D(6)).

Miss chance reduction by class is given in section 4, but to summarize here:

| Class                                   | Miss chance reduction at level-up |
| --------------------------------------- | --------------------------------- |
| Mage, Alchemist, Psionic, Bishop        | 1d3 (1 to 3)                      |
| Priest, Thief, Bard                     | 1d4 (1 to 4)                      |
| Fighter, Ranger, Valkyrie, Lord, Monk   | 1d4+1 (2 to 5)                    |
| Samurai, Ninja                          | 1d4+2 (3 to 6)                    |

Note that all of this means that a pure spellcaster suddenly class-changed to a
front-line fighter will not be all that great at it even after catching up in
level!  Such a character does catch up in hit points, which can be misleading.
This is another reason not to use pure spellcasters past the very early game.

It is also not obvious that Samurai and Ninja have superior accuracy compared
to the other warrior classes, nor that Bishops are worse fighters than pure
Priests (another strike against the Bishop).

### SECTION 2F - Other things that rise with level

* Hit points: at every level up, if you are a higher level than you have ever
  been before, you gain the number of hit points indicated in section 4, with a
  bonus for a Vitality of 15+.  If you are not, then the game rolls for a
  number of hit points as if you had always been your current class and with
  the Vitality you currently have.  If this number is greater than your maximum
  hit points, then it becomes your maximum hit points; otherwise, you gain 1
  hit point.  This means that you do not have to worry about hit points while
  class switching temporarily, as hit points are self-correcting below your
  maximum level ever attained.  Note bug described in section 1D(6) however.

* Spell points: a class/level combination capable of learning spells can get
  maximum spell point increases in all realms where at least one spell is
  already known.  This works similarly to how hit point increases work, except
  that Piety is the stat that gives bonuses.  The number and cost of spells you
  know in a realm also have some impact on how many spell points you gain.  If
  you learn a large number of spells, Fire spell points tend to lag behind, as
  that realm has the fewest spells available.

* Statistics: the game will randomly pick a statistic other than Karma and
  increase it by 1.  If the chosen statistic is already 18 or higher, nothing
  happens.  The game will then flip a coin and stop half the time; otherwise it
  repeats for a different statistic.  You cannot gain more than 1 point per
  statistic per level-up.  The upshot is that the chance of stat gains are:

  | Stat boosts | Probability |
  | ----------- | ----------- |
  | 1           | 1 in 2      |
  | 2           | 1 in 4      |
  | 3           | 1 in 8      |
  | 4           | 1 in 16     |
  | 5           | 1 in 32     |
  | 6           | 1 in 64     |
  | 7           | 1 in 64     |

  Other than meeting minimum stat requirements for a class change, stats will
  do the following when increased:

  - Strength: Increases melee damage, especially with the Bash attack mode.
    Increases CC if you use the fix in section 1D(1).  Increases chance to
    force open doors.
  - Intelligence: Does NOT appear to affect accrual of skill points, as it does
    in later games!  Does appear to increase effectiveness of spellcasting.
  - Piety: Increases the number of spell points gained with level-ups if at 15+.
    Does NOT enhance spell point regeneration, contrary to what the manual
    states and contrary to what happens in later games.
  - Vitality: Increases the number of hit points gained with level-ups if at 15+.
    Increases CC if you use the fix in section 1D(1).
  - Dexterity: Lowers AC starting at 15.  Increases the number of swings you get
    in a single attack.
  - Speed: Lowers AC starting at 15.  Improves initiative in combat.  Increases
    number of attacks per round.
  - Personality: as you may have guessed, this is worthless other than for class
    changing.

* Melee attacks: the numbers of melee attacks you get increases with character
  level; this is more likely with high Dexterity (for number of swings in a
  single attack) and Speed (for number of attacks per round).

* Resistances: at every level up, you will gain a few points in 12 of the 13
  resistances.  This is listed by class in section 4.  These points gained are
  not permanent; they will all disappear upon a class change and will need to
  be re-earned.  This is thus a progression that you need to worry about only
  for classes you choose long-term.  Four resistances are the same for every
  class; they are Fire, Cold, Missile, and Acid resistance.  The maximum for
  any resistance is 125%, both for your characters and the monsters.

  - Acid resistance applies against acid breath, and the Acid Splash, Acid Bomb,
    and Itching Skin spells.  This is both the hardest resistance to increase
    (apart from the special case of Death resistance), and the resistance that
    monsters generally have the lowest resistance to outside of Death.
  - Air resistance applies to the noxious vomit attack of monsters such as
    zombies; sonic attacks that deliver damage, such as that used by Giant
    Wyrms; and the Stink Bomb, Whirlwind, Toxic Vapors, Noxious Fumes,
    Asphyxiation, and Deadly Air (but see section 1D(2)) spells.
  - Cold resistance is used to resist Slow and Weaken spells, in addition to cold
    breath and the Chilling Touch, Iceball, and Deep Freeze spells.
  - Lifeforce resistance is used to resist instant death spells, such as the
    Death spell itself, that do not have a clear-cut other resistance that
    would apply against it.  Such spells also check Death resistance (see
    below).  Lifeforce resistance also applies against the Word of Death spell.
    For monsters, Dispel Undead and Astral Gate similarly check both Lifeforce
    and Death resistance.
  - Light resistance is used to resist Blinding Flash and Prismic Missile spells,
    but does not apply against anything else, making it the least useful
    resistance in Wizardry VI.  (It's much more useful in Wizardry VII.)
  - Magic resistance is the primary resistance against only a few spells, notably
    the Silence spell, but it also has a minor impact on resistance to all
    magic.  (A Fireball gets resisted primarily by Fire resistance, but Magic
    resistance also has some effect.)
  - Missile resistance applies primarily to physical missiles, notably boulders,
    but it also applies against the Blades spell.

  There is one other kind of resistance, Death resistance.  All characters
  normally have no Death resistance; you can only get it by equipping either a
  Clove of Garlic (which provides 35% resistance) or a Rock of Reflection
  (which provides the maximum 125% resistance).  Death resistance provides
  resistance to the special hypnosis attacks of Dracula and Rebecca; to
  critical hits; and to all instant death spells.  These are all serious
  threats in the endgame, enough that you may want to forego offhand weapons
  for Rocks of Reflection.  Many monsters, including most midgame and all
  endgame bosses, have good Death resistance themselves.

### SECTION 2G - Places of note for developing characters

Unless you want to make a class change before reaching level 2 (section 5B has
an explanation for why), you should at least solve all the early-game puzzles
up to finding the Altar of Ramm before starting serious class changing in
earnest.  By the time you finish these early-game puzzles your characters will
around level 5-6.

The easiest place to train a level 1 character that has just gone through a
class change is on the top level of the Belfry.  If you choose to HOLD ROPE AND
JUMP INTO THE BELFRY, you will initiate combat with Vampire Bats and some
additional bats and rats, worth several hundred experience points.  This combat
will always be available, and if your other characters are level 5+ it is
trivially easy to win.

Not only is this a guaranteed combat, this is a good way to gain only one level
at a time; the idea is to control level-ups so that you can reload for multiple
stat increases upon gaining a level.

Not too far away from the Belfry is the Altar of Ramm, on the second floor of
the castle.  The fountain just to the northeast will restore hit points and
stamina.

The next good base can be found on the lower levels of the Dwarf Mines; in the
dark areas on the lower floors there is a fountain that will restore all of hit
points, stamina, and magic points.  If you are having a hard time at this point
in the game, this is a very good base of operations to reach.  You can continue
to level grind here by "spinning" on the spot, free to use all the magic you
want.  You can also readily return to the Belfry if you wish.

The third good base can be found soon after starting to explore the River Styx.
Defeating the Mino-Daemon and unlocking the nearby chamber with the Key of
Minos leads to two fountains; one restores hit points and stamina, the other
spell points.  The ability to burn spell points freely makes this difficult
area much easier.

The last good base is found in the Hall of the Dead.  On the south side of the
Hall, just outside of the Queen's Tomb, there is a fountain that restores hit
points, stamina, and spell points, as well as fixes multiple conditions.

You should complete all your class changes and finish major gear purchases
before moving on from the Hall of the Dead; the trigger for this is the second
meeting with the vampire King.  Once you pass this checkpoint, there is no
going back to earlier areas in the game until you win the game.  This
checkpoint is also the checkpoint for the game's multiple endings.  There are
no major gear purchases to be made past this, and no fountains that restore
magic, not to mention that combat difficulty takes another great leap upward.
High levels in this late game stage are much more useful than any marginal gain
that can be made by switching classes, particularly since it will be difficult
both to keep low level characters alive and get good level-ups for them.

Once you can get into the main Temple of Ramm, all of the non-boss combats will
regenerate if you leave the Temple and return.  This is of use if you want to
level grind in the late game, particularly if you want to increase everyone's
level to 20 for transferring to Wizardry VII.

### SECTION 2H - Notable NPC's that sell gear

You can always freely regenerate a NPC's inventory by leaving and returning.

* Queequeg - found in one of the barracks in the Castle Basement.  He can be
  reached right after beginning the game.  He is a very useful source of gear
  throughout the game, and is useful even after winning if you want to transfer
  to Wizardry VII, so don't kill him.  You will want to buy one Mystery Oil,
  but more than one is not useful; the Mystery Oil is a quest item and you will
  be unable to drop extras.  Queequeg has low-level scrolls, potions including
  Resurrection potions and Stink Bombs, tier 1 weaponry, tier 1 armor, and
  spellbooks of Knock-Knock, Direction, and Detect Secret.  If you are having
  trouble against early game or midgame enemies, Stink Bombs work well to tilt
  the odds in your favor.  The best way to fund very early purchases from
  Queequeg is to sell the Amulet of Life found near the castle entrance.

* Smitty - found in the Dwarven Mines.  He has tier 1 and tier 2 weaponry for
  sale, as well as the occasional Vulcan Hammer, which is a tier 3 weapon. It's
  worth the trouble to get a Vulcan Hammer for any front-line fighter who can
  equip it; I recommend investing some skill points into Legerdemain to steal
  your way towards a Vulcan Hammer or two.  One other weapon easy to miss: the
  Bec de Corbin, which is oddly an offhand weapon (a good one) and not a
  polearm as in Wizardry VIII and in real life.

* Kuwali Kubona - found at the top of the Amazulu Pyramid, if you properly keep
  the Amazulu Queen happy.  She carries spellbooks of Chilling Touch, Blinding
  Flash, Weaken, Slow, Poison, Fire Shield, Armorplate, Cure Lesser Condition,
  and Sleep.  Take care not to upset the Amazulu Queen until you're done with
  spellbook purchases from here.  On the other hand, fighting the Amazulu Queen
  is the only way to get the Spear of Death and Bone Necklace.

* Mai Lai - found on one of the islands on the River Styx.  She has tier 3
  weaponry and tier 3 armor for sale.  Note that it is possible to win the game
  without giving her the claim information.  If you do that, you will still be
  able to get equipment from Mai Lai even after winning the game; some of this
  gear can transfer freely to Wizardry VII.  Mai Lai's gear is expensive, but
  she actually isn't hard to steal from if you put some points into
  Legerdemain.  The most notable weapon Mai Lai sells is the Cat'O Nine Tail,
  which is a good Extended weapon that any non-Faerie that isn't a Priest,
  Bishop, or Samurai can use.

* Caterpillar - He is a good source of magic stix.  Note that you do not need
  to give the Caterpillar the Hookah Pipe from Mai Lai to win the game; doing
  so will cause him to vanish from the game (and if you got the Hookah Pipe,
  you've probably caused Mai Lai to vanish from the game as well, which is
  worse).

* Queen of Faeries - She is found in the Enchanted Forest outside of the
  endgame Temple of Ramm.  She is the only NPC you can buy and sell things from
  in the late game.  Her goods include potions; Golden Rods that can be
  equipped by Priests and Bishops for +1 regeneration; the Rod of Sprites, a
  good offhand weapon for Faeries only which transfers to Wizardry VII; Cloves
  of Garlic which are one of only two ways to get Death resistance; and Magic
  Cookies that can restore spell points.  Spend all of your money here, as you
  will soon lose it all anyway.

### SECTION 2I - Notable gear that cannot be purchased

* Tier 2 armor cannot be purchased; this includes most chain and plate armor,
  along with ninja garb, the Round Shield, and the Heater Shield.  All of this
  gear freely transfers to Wizardry VII, where it mostly can be eventually
  purchased.  Of particular note are the Plate Mail, Plate Greviere, and
  Solleret.  These all provide -10 to AC, usable by Fighters, Valkyries, and
  Lords, and all freely transfer to Wizardry VII; you may want to make a point
  of getting and holding onto at least one of each if you plan to move your
  party to Wizardry VII.  Tier 2 armor that isn't ninja garb can be found as
  random treasure in many treasure chests, or occasionally as random drops from
  Miner Dwarves, Major Dwarves, Skeletons, and Skeleton Lords.

* Other than at game start, ninja armor can only be found randomly in one
  specific chest in the Hazard Area adjoining the Castle Basement (the same
  chest that can have a Mitre), or as a 1 in 2 drop from Ninja, Assassins, or
  Chunin (which are all endgame monsters that appear in the Enchanted Forest
  and the Temple of Ramm).

* A list of tier 4 weapons, their powers, and where they can be found (unless
  specified, all of these can transfer to Wizardry VII):
  - Blades of Aesir - 2-handed axe that can be wielded by Fighters, Valkyries,
    and Lords; does 2d12 damage at +2 to hit and +5% Critical chance, has a 5%
    chance of knocking a monster unconscious, and can be Meleed for double
    damage; also provides 50% Cold and 50% Paralysis resistance.  Available
    only as a 1 in 500 drop from Pit Fiends, Greater Demons, and Wraith Lords.
  - Demon's Tooth - dagger that can be used offhand, by Thieves and Bards only;
    does 3d4+4 damage at +3 to hit, and has a 15% chance to paralyze a monster.
    Available only as a 1 in 60 drop from Defenders.  Does not transfer to
    later games.
  - Diamond Eyes - mace that can be used offhand, by Fighters, Valkyries, Lords,
    Priests, and Bishops; strongest offhand weapon in the game, does 3d4+4
    damage at +2 to hit, has a 20% chance to paralyze a monster, and also
    provides 25% Magic resistance.  Available only as a 1 in 500 drop from Pit
    Fiends, Greater Demons, and Wraith Lords.
  - Elven Bow - strongest bow in the game, usable only by Elves; provides +4 to
    hit and +5% Critical chance.  Guaranteed drop from Robin Windmarne; 1 in
    500 drop from Pit Fiends, Greater Demons, and Wraith Lords.
  - Estoc of Olivia - sword only usable by Rangers; does 2d7+4 damage at +3 to
    hit and +5% Critical chance; also provides 80% Lifeforce resistance.
    Available only as a 1 in 500 drop from Pit Fiends, Greater Demons, and
    Wraith Lords.
  - Excaliber - strongest two-handed weapon, usable by Fighters, Valkyries, and
    Lords; does 4d8+4 damage at +4 to hit and +5% Critical Chance, has a 25%
    chance of turning an enemy to stone, and can be Meleed for double damage;
    also provides +1 regeneration and 75% Light resistance.  Available only as
    a 1 in 500 drop from Pit Fiends, Greater Demons, and Wraith Lords.  (There
    is a decades-old rumor that this can drop from dinosaurs.  It's only a
    rumor.)
  - Fang - sword usable by Fighters, Valkyries, and Lords; does 2d8+8 damage at
    +2 to hit and +10% critical chance; also provides 50% Hypnosis resistance.
    Available only as a guaranteed drop from Bela.  The only way to get Fang in
    in Wizardry VII is to transfer the one from VI.
  - Faust Halberd - 2-handed polearm that can be wielded by Fighters, Valkyries,
    and Lords; does 4d4+2 damage at +2 to hit and +5% Critical chance, and has
    a 5% chance to paralyze a monster; also provides 50% Air resistance.
    Available only as a 1 in 500 drop from Pit Fiends. Greater Demons, and
    Wraith Lords.  Transfers to Wizardry VII, but gets -3 regeneration there.
  - Maenad's Lance - powerful Valkyrie-only Extended weapon, does 2d12 damage at
    +3 to hit and +10% Critical chance; also provides +1 regeneration, and 50%
    Hypnosis and 50% Psionic resistance.  Guaranteed drop from Brigerd Woltan;
    1 in 500 drop from Pit Fiends, Greater Demons, and Wraith Lords.
  - Muramasa Blade - potent weapon usable only by Samurai; does 3d7+4 damage at
    +4 to hit and +15% Critical chance, and can be Meleed for double damage.
    Also provides 25% Fire, 25% Cold, 25% Air, and 25% Missile resistance.
    Guaranteed drop from Haiyato Daikuta; 1 in 500 drop from Pit Fiends,
    Greater Demons, and Wraith Lords.
  - Peacemaker - potent arrows that do 6d6+6 damage at a +20% Critical chance.
    Guaranteed drop from Brigerd Woltan; 1 in 20 drop from Drow Elves and
    Highlanders.
  - Rammbus Staff - 2-handed Extended staff usable only by Priests and Bishops;
    somewhat better than the Tier 3 Holy Basher; does 2d4+4 damage at +2 to hit
    and has a 15% chance of knocking a monster unconscious; also provides 50%
    Magic resistance.  Available only as a 3 in 20 drop from Priests of Ramm.
    Transfers to Wizardry VII, but gets -1 regeneration there.
  - Saint Bastard - sword usable only by Fighters, Valkyries, and Lords; does
    2d4+5 damage at +2 to hit, and has a 5% chance of knocking a monster
    unconscious.  Available only as a 1 in 60 drop from Defenders.
  - Spear of Death - 1-handed Extended spear usable by Fighters, Rangers,
    Valkyries, Lords, Samurai, Monks, and Ninja; does 1d5+4 damage at +1 to hit
    and +2% Critical chance, and also has a 15% chance of poisoning a monster.
    Available only as a guaranteed drop from the Amazulu Queen.  The only way
    to get a Spear of Death in Wizardry VII is to transfer the one from VI.
  - Sword of Hearts - sword usable only by Thieves, Rangers, and Bards; does
    1d7+4 damage at +2 to hit and +2% Critical chance.  Available only as a 1
    in 60 drop from Defenders.
  - The Avenger - powerful sword usable only by Fighters, Valkyries, and Lords
    that does 3d8+4 damage at +3 to hit and +10% Critical chance; also provides
    50% Fire and 50% Light resistance.  Guaranteed drop from the Black Knight;
    1 in 500 drop from Pit Fiends, Greater Demons, and Wraith Lords.
  - Wakizashi +1 - strongest offhand weapon usable by Samurai or Ninja; does
    1d9+1 damage at +1 to hit and +2% Critical chance.  Available only as a
    guaranteed drop from Haiyato Daikuta.  Does not transfer to later games,
    even though it exists there.
  - Zatoichi Bo - potent Extended staff only usable by Samurai and Monks; does
    3d6+6 damage at +4 to hit and +5% Critical chance, with a separate 15%
    chance of causing paralysis and a 15% chance of knocking a monster
    unconscious; also provides 50% Hypnosis and 50% Psionic resistance.
    Available only as a 1 in 500 drop from Pit Fiends, Greater Demons, and
    Wraith Lords.

* A list of the good tier 4 armor, their powers, and where they can be found:
  (unless specified, all of these can transfer to Wizardry VII)
  - Ebony Heaume - strongest helmet in the game, usable only by Fighters,
    Valkyries, and Lords; provides -14 AC, and 25% Fire, 25% Cold, 25% Air, 25%
    Missile, and 35% Acid resistance.  Available only as a guaranteed drop from
    the Black Knight.
  - Ebony Plate (U) - strongest torso armor in the game, usable only by Fighters,
    Valkyries, and Lords; provides -14 AC, and 25% Fire, 25% Cold, 25% Air, 25%
    Missile, and 35% Acid resistance.  Available only as a guaranteed drop from
    the Black Knight.
  - Ebony Plate (L) - strongest leg armor in the game, usable only by Fighters,
    Valkyries, and Lords; provides -14 AC, and 25% Fire, 25% Cold, 25% Air, 25%
    Missile, and 35% Acid resistance.  Available only as a guaranteed drop from
    the Black Knight.
  - Glass Slippers - footwear usable by all females; provides -8 AC, and 100%
    Hypnosis and Psionic resistance; permanently increases Karma by 1 when
    invoked.  Available only as a 1 in 60 drop from Pit Fiends, Greater Demons,
    and Wraith Lords.  Does not transfer to later games.
  - Hi-Kane-Do (U) - strongest torso armor for Samurai only; provides -12 AC, and
    30% Fire, 30% Missile, and 30% Acid resistance.  Available only as a
    guaranteed drop from Haiyato Daikuta.
  - Hi-Kane-Do (L) - strongest leg armor for Samurai only; provides -12 AC, and
    30% Fire, 30% Missile, and 30% Acid resistance.  Available only as a
    guaranteed drop from Haiyato Daikuta.
  - Mantis Boots - strongest footwear in the game, usable only by Fighters,
    Valkyries, and Lords; provides -14 to AC, and 50% Paralysis, 25% Acid, and
    25% Psionic resistance.  Available only as a guaranteed drop from Brigerd
    Woltan.
  - Mantis Gloves - strongest gloves in the game, usable only by Fighters,
    Valkyries, and Lords; provides -14 to AC, and 50% Light, 75% Poison, and
    50% Hypnosis resistance.  Available only as a guaranteed drop from Brigerd
    Woltan.
  - Mordecai's Cone - strongest helmet usable by Mages, Alchemists, and Psionics;
    provides -7 AC, and 50% Hypnosis, 50% Psionic, 50% Lifeforce, and 50% Magic
    resistance.  Available only as a 1 in 60 drop from Priests of Ramm.  Does
    not transfer to later games.
  - Robe of Enchant (U) - strongest torso robe in the game; provides -6 AC and
    50% Magic resistance.  Available only as a guaranteed drop from Xorphitus.
  - Robe of Enchant (L) - strongest leg robe in the game; provides -6 AC and 50%
    Lifeforce resistance.  Available only as a guaranteed drop from Xorphitus.
  - Rock of Reflection - offhand item that provides 125% Death resistance, and is
    one of only two ways for your characters to get Death resistance at all.
    Available only at a specific location in the Enchanted Forest.  Does not
    transfer to later games.
  - Sacred Slippers - strongest footwear usable by Priests and Bishops; provides
    -6 AC, and 35% Lifeforce resistance.  Available only as a 1 in 60 drop from
    Priests of Ramm.  Does not transfer to later games.

* A list of powerful miscellaneous equipment, their powers, and where they can
  be found (unless specified, all of these can transfer to Wizardry VII):
  - Bone Necklace - usable only by Fighters, Priests, Valkyries, and Bishops;
    provides -2 to base AC and 35% Lifeforce and 35% Magic resistance.
    Available only as a guaranteed drop from the Amazulu Queen.  Does not
    transfer to later games.
  - Cameo Locket - usable by males of any class; provides -4 to base AC, +1
    regeneration, and 100% Lifeforce resistance.  Available only as a
    guaranteed drop from Bela.
  - Cape of Hi-Zen - usable only by Monks; provides -3 to base AC, +1
    regeneration, and 70% Hypnosis, 70% Psionic, 70% Lifeforce, and 70% Magic
    resistance.  Available only as a 1 in 60 drop from Pit Fiends, Greater
    Demons, and Wraith Lords.  Does not transfer to later games.
  - Diamond Ring - usable by females of any class; provides -5 to base AC, +3
    regeneration, and 100% Lifeforce resistance.  Available only from the final
    confrontation with Rebecca if you have performed a certain specific action
    hinted at by the game long before.
  - Displacer Cloak - can be equipped by everyone; provides -4 to base AC, and
    can cast Blink without ever running out of charges.  Available only as a
    guaranteed drop following the final confrontation with Dracula and Rebecca.
  - Forest Cape - usable only by Rangers; provides -3 to base AC, and 30% Cold,
    30% Air, and 30% Acid resistance.  Available only as a guaranteed drop from
    Brigerd Woltan.
  - Jade Figurine - usable only by Monks; provides -2 to base AC, and 20%
    Hypnosis and 20% Psionic resistance.  Available only as a set treasure in
    the Enchanted Forest.  Does not transfer to later games.
  - Medicine Bag - usable only by Alchemists; provides -2 to base AC and +1
    regeneration.  Available only as a 1 in 40 drop from Grandfathers.
  - Mempo of Death - usable only by Samurai; provides -3 to base AC, and 50%
    Lifeforce and 35% Magic Resistance; permanently increases Karma by 1 when
    invoked.  Available only as a 1 in 20 drop from Lord Daimyo.  Does not
    transfer to later games.
  - Midnight Cloak - usable only by Thieves, Bards, and Ninja; provides -2 to
    base AC.  Available only as a 1 in 40 drop from Grandfathers.
  - PK Crystal - usable only by Psionics; provides -4 to base AC, +2
    regeneration, and 90% Hypnosis and 90% Psionic resistance.  Available only
    as a 1 in 20 drop from Keepers of Crystal.
  - Ring of Stars - can be equipped by everyone; provides -4 to base AC, +1
    regeneration, and 50% Hypnosis and 50% Psionic resistance.  Available only
    as a guaranteed drop following the final confrontation with Dracula and
    Rebecca.
  - Scarab Necklace - usable only by Priests and Bishops; provides -2 to base AC,
    and 35% Fire, 35% Light, 25% Air, 25% Poison, 25% Hypnosis, 25% Psionic,
    25% Lifeforce, and 25% Magic resistance.  Available only as a 1 in 20 drop
    from Radames.  Does not transfer to later games; there is a Scarab Necklace
    in Wizardry VII, but it is a completely different item there.
  - Tora Maedate - usable only by Samurai; provides -2 to base AC and 35%
    Lifeforce resistance.  Available only as a 1 in 20 drop from Daisho
    Masters.  Does not transfer to later games.

* The following items are defined by the game, but cannot actually be found
  naturally in-game and thus require hex-editing to acquire: Basso Lyre, Wrist
  Rocket, Devil Stone, Siege Arbalest, Lightning Bolt, Cuckoo Call, Lyre of
  Cakes, Faerie Cap, Mitre de Sanct, Heaume, Garland of Roses.

* Spellbooks for the following spells are available as random finds from chests
  or monsters, but cannot be purchased from NPCs: Air Pocket, Anti-Magic,
  Armormelt, Charm, Conjuration (Mages/Priests/Bishops only), Deadly Poison
  (notable in that Ninja can use it), Ice Shield, Identify (Psionics/Bishops
  only), Levitate, Missile Shield, Sane Mind, Silence, Stamina.  As random
  treasure, some of these are hard to find; the better spells are still worth
  considering using a spell pick on.

## Character races

### SECTION 3A - Character race: Human

Statistics:
```
Wizardry VI/VII STR  9, INT  8, PIE  8, VIT  9, DEX  9, SPD  8, PER  8 ( 59)
Wizardry VIII   STR 45, INT 45, PIE 45, VIT 45, DEX 45, SPD 45, SEN 45 (315)
```

Resistances:
```
Wizardry VI/VII +20% Lifeforce
Wizardry VIII   None
```

Humans aren't saddled with the abysmal Piety scores they had in earlier
Wizardry games, but they still aren't a very exciting choice for your party,
given their lack of resistances.  The extra stat points they get in Wizardry
VIII won't be of much use for two reasons.  First, a character transferred from
the earlier games will get about 10 extra stat points anyway.  Second, you will
have much less control over where bonus stat points go during the transfer
process, which is the sole but significant liability transferred characters
have in Wizardry VIII.

### SECTION 3B - Character race: Elf

Statistics:
```
Wizardry VI/VII STR  7, INT 10, PIE 10, VIT  7, DEX  9, SPD  9, PER  8 ( 60)
Wizardry VIII   STR 35, INT 50, PIE 50, VIT 35, DEX 50, SPD 45, SEN 40 (305)
```

Resistances:
```
Wizardry VI/VII +20% Hypnosis
Wizardry VIII   +10 Air, +20 Mental
```

Other:
```
Wizardry VI     can equip Elven Bow; may not equip very large weapons
Wizardry VII    can equip Elven Bow; may not equip very large weapons
Wizardry VIII   can equip Elven Bow; may not equip very large weapons
```

The Elf's strong magical aptitudes and unique ability to use the Elven Bow make
the Elf a reasonable addition to any party.  Note that the Elven Bow isn't that
good in Wizardry VI, but gets considerably better with each successive sequel.
The only very large weapon in Wizardry VI is the Giant Sledge, which isn't a
noteworthy weapon.

### SECTION 3C - Character race: Dwarf

Statistics:
```
Wizardry VI/VII STR 11, INT  6, PIE 10, VIT 12, DEX  7, SPD  7, PER  7 ( 60)
Wizardry VIII   STR 55, INT 30, PIE 50, VIT 60, DEX 35, SPD 35, SEN 35 (300)
```

Resistances:
```
Wizardry VI/VII +20% Poison, +15% Magic
Wizardry VIII   +VIT/5 Fire
```

Other:
```
Wizardry VI     None
Wizardry VII    None
Wizardry VIII   Physical damage resistance
```

Dwarves have good stats and resistances in all three games, and are the ideal
choice for a frontline melee tank.

### SECTION 3D - Character race: Gnome

Statistics:
```
Wizardry VI/VII STR 10, INT  7, PIE 13, VIT 10, DEX  8, SPD  6, PER  6 ( 60)
Wizardry VIII   STR 35, INT 50, PIE 40, VIT 50, DEX 50, SPD 35, SEN 45 (305)
```

Resistances:
```
Wizardry VI/VII +15% Magic
Wizardry VIII   +10 Earth, +VIT/5 Mental
```

Other:
```
Wizardry VI     may not equip very large weapons
Wizardry VII    may not equip very large weapons
Wizardry VIII   may not equip very large weapons
```

Gnomes in Wizardry VIII have a very different stat distribution compared to the
earlier games.  They still have good enough resistances and stats overall to
make them good spellcasters in any of the three games, and reasonable hybrids.

### SECTION 3E - Character race: Hobbit

Statistics:
```
Wizardry VI/VII STR  8, INT  7, PIE  6, VIT  9, DEX 10, SPD  7, PER 13 ( 60)
Wizardry VIII   STR 40, INT 40, PIE 30, VIT 45, DEX 55, SPD 50, SEN 50 (310)
```

Resistances:
```
Wizardry VI/VII +10% Poison, +10% Magic
Wizardry VIII   +VIT/5 Earth
```

Other:
```
Wizardry VI     may not equip very large weapons
Wizardry VII    may not equip very large weapons
Wizardry VIII   may not equip very large weapons
```

The weighting of stats towards Personality makes Hobbits less than optimal in
Wizardry VI and VII, though their relatively high stat total and good
resistances make them a solid choice if Wizardry VIII enters the picture.

### SECTION 3F - Character race: Faerie

Statistics:
```
Wizardry VI/VII STR  5, INT 11, PIE  6, VIT  6, DEX 10, SPD 14, PER 12 ( 64)
Wizardry VIII   STR 25, INT 55, PIE 35, VIT 30, DEX 50, SPD 60, SEN 45 (300)
```

Resistances:
```
Wizardry VI/VII +25% Paralysis, +25% Missile, +25% Psionic, +25% Lifeforce,
                +25% Magic
Wizardry VIII   +15 Air, +15 Earth, +15 Mental, +15 Divine
```

Other:
```
Wizardry VI     may not equip most weapons and armor; may equip special Faerie
                equipment; -2 bonus to base AC; 1/3 penalty to CC; +1 bonus to
                mana regeneration
Wizardry VII    may not equip most weapons and armor; may equip special Faerie
                equipment; begins with special Faerie equipment; -2 bonus to
                base AC; 1/3 penalty to CC; +1 bonus to mana regeneration
Wizardry VIII   may not equip most weapons and armor; may equip special Faerie
                equipment; begins with special Faerie equipment; +2 bonus to
                base AC; 1/3 penalty to CC; faster mana regeneration
```

Faeries come with excellent resistances and the ability to use special Faerie
equipment, making one an excellent addition to the party in any of the games.
Of particular note is that only they can equip the famed Cane of Corpus found
in VII and VIII.  They make good Mages, Alchemists, Psionics, Monks, and Ninja
in all three games.  They can equip almost all of the equipment available to
those classes, rendering the equipment limitations largely moot.  Faeries can
also switch between Thief and Bard freely in Wizardry VI and VII, making it a
good way to get skill points and Mage spells if you don't want to deal with
reloads upon gaining a level.  There is no other race or pair of classes
capable of this.  However, their inability to equip most equipment available to
those classes make this best as a step in transitioning to another class.

### SECTION 3G - Character race: Lizardman

Statistics:
```
Wizardry VI/VII STR 12, INT  5, PIE  5, VIT 14, DEX  8, SPD 10, PER  3 ( 57)
Wizardry VIII   STR 60, INT 25, PIE 25, VIT 70, DEX 40, SPD 50, SEN 30 (300)
```

Resistances:
```
Wizardry VI/VII -20% Cold, +10% Acid, +25% Psionic
Wizardry VIII   +15 Fire, +10 Water, +10 Earth, -10 Mental, -10 Divine
```

Other:
```
Wizardry VI     -1 penalty to mana regeneration
Wizardry VII    -1 penalty to mana regeneration
Wizardry VIII   slower mana regeneration
```

The abysmal mental stats and penalty to mana regeneration make the Lizardman
unsuitable as anything other than a pure fighter, which is only reasonable in
Wizardry VIII.  Even there, his newfound vulnerability to mental conditions
makes him a dubious choice for a frontline tank.

### SECTION 3H - Character race: Dracon

Statistics:
```
Wizardry VI/VII STR 10, INT  7, PIE  6, VIT 12, DEX 10, SPD  8, PER  6 ( 59)
Wizardry VIII   STR 55, INT 35, PIE 30, VIT 60, DEX 50, SPD 40, SEN 30 (300)
```

Resistances:
```
Wizardry VI/VII -20% Cold, +10% Acid, +25% Psionic
Wizardry VIII   +15 Water, +5 Air, -5 Mental, -5 Divine
```

Other:
```
Wizardry VI     may breathe acid at a stamina cost
Wizardry VII    may breathe acid at a stamina cost
Wizardry VIII   may breathe acid at a stamina cost
```

The ability of Dracons to breathe acid isn't particularly useful, only being of
real use at the very beginning of the game.  The ability of Bards to cast
spells with instruments is considerably more effective in comparison.  Their
lackluster stats and resistances make them not very useful overall, and once
you reach Wizardry VIII there is a spell that grants the ability to breathe
like a dracon anyway.

### SECTION 3I - Character race: Felpurr

Statistics:
```
Wizardry VI/VII STR  7, INT 10, PIE  7, VIT  7, DEX 10, SPD 12, PER 10 ( 63)
Wizardry VIII   STR 40, INT 40, PIE 30, VIT 35, DEX 50, SPD 60, SEN 50 (305)
```

Resistances:
```
Wizardry VI/VII +20% Cold, +20% Paralysis, +15% Missile
Wizardry VIII   -15 Water, +10 Air, +10 Earth, +10 Mental
```

Felpurrs come with excellent stats and resistances by Wizardry VI and VII
standards.  Their sudden vulnerability to Water magic in Wizardry VIII makes
them much less useful there (Water is the spell school that has the second-
highest number of status inflicting spells in that game), but if you are
starting a party in one of the earlier games it isn't so bad that it can't be
overcome.

### SECTION 3J - Character race: Rawulf

Statistics:
```
Wizardry VI/VII STR  8, INT  6, PIE 12, VIT 10, DEX  8, SPD  8, PER 10 ( 62)
Wizardry VIII   STR 40, INT 30, PIE 55, VIT 50, DEX 40, SPD 40, SEN 50 (305)
```

Resistances:
```
Wizardry VI/VII +20% Cold
Wizardry VIII   +10 Water, +5 Earth, +15 Divine
```

The Rawulf is a strong choice for a hybrid fighter-priest in all three games,
with good stats and resistances for the role.

### SECTION 3K - Character race: Mook

Statistics:
```
Wizardry VI/VII STR 10, INT 10, PIE  6, VIT 10, DEX  7, SPD  7, PER  9 ( 59)
Wizardry VIII   STR 50, INT 50, PIE 25, VIT 50, DEX 35, SPD 35, SEN 55 (300)
```

Resistances:
```
Wizardry VI/VII +15% Cold, +25% Magic
Wizardry VIII   +15 Water, +15 Mental, +10 Divine
```

Other:
```
Wizardry VI     None
Wizardry VII    None
Wizardry VIII   can equip Giant's Sword; gets special reaction from NPC Mooks
```

The Mook has mediocre statistics, but it does come with excellent resistances
and some unique abilities down the road in Wizardry VIII.  Mooks are
particularly suitable for being Rangers or Psionics in all three games, but are
good in any hybrid fighter-caster role.

## Character classes

### SECTION 4A - Character class: Fighter

```
Starting Equipment : Longsword, Buckler Shield, Leather Cuirass, Fur Legging,
                     Sandals
Attributes Required: STR 12
Starting Hit Points: 1d5+5 (6 to 10)
Level-up Hit Points: 1d5+5 (6 to 10)
Miss Chance Per Lev: 1d4+1 (2 to 5)
Spellbook          : None
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 1, Magic 1
Primary Skills     : None
Additional Skills  : None
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light      4% + 2%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  28% + 1%/level
                     Paralysis  4% + 2%/level  Psionic    8% + 2%/level
                     Air        8% + 2%/level  Lifeforce 28% + 2%/level
                     Poison     8% + 3%/level  Magic      4% + 3%/level
Experience Needed  : Level 2    1,000    Level 8     64,000
                     Level 3    2,000    Level 9    128,000
                     Level 4    4,000    Level 10   256,000
                     Level 5    8,000    Level 11   512,000
                     Level 6   16,000    Level 12+ +256,000 per level
                     Level 7   32,000
```

The Fighter at least fights well and can use most weapons and armor, but in
Wizardry VI and especially VII is no better than a Valkyrie or a Lord in this
regard.  The Fighter also has poor resistances; this combined with the
inability to learn spells makes the Fighter a very poor choice of class except
right at the start of the game.  The only advantage the Fighter can claim is
cheap late-game experience requirements, which isn't enough to offset the lack
of spellcasting growth; the Fighter doesn't even advance all that much faster
than the Valkyrie.

### SECTION 4B - Character class: Mage

```
Starting Equipment : Staff, Robes (U), Robes (L), Sandals, Scroll of Magic
                     Missile
Attributes Required: INT 12
Starting Hit Points: 1d3+1 (2 to 4)
Level-up Hit Points: 1d3+1 (2 to 4)
Miss Chance Per Lev: 1d3 (1 to 3)
Spellbook          : Mage
Mana Regeneration  : Fire 3, Water 3, Air 2, Earth 2, Mental 2, Magic 3
Primary Skills     : Thaumaturgy
Additional Skills  : Oratory, Thaumaturgy
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light      4% + 1%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  16% + 1%/level
                     Paralysis  8% + 1%/level  Psionic   16% + 1%/level
                     Air       12% + 2%/level  Lifeforce 16% + 3%/level
                     Poison    16% + 1%/level  Magic     24% + 3%/level
Experience Needed  : Level 2    1,250    Level 8     80,000
                     Level 3    2,500    Level 9    160,000
                     Level 4    5,000    Level 10   320,000
                     Level 5   10,000    Level 11   640,000
                     Level 6   20,000    Level 12+ +375,000 per level
                     Level 7   40,000
```

The Mage has the most useful spellbook in general, and superb mana regeneration
rates, making them an excellent choice to start the game with.  However, the
Mage has several serious problems: (1) the worst hit point growth in the game,
which most people at least expect; (2) the worst resistances in the game, which
is not at all obvious and is contrary to most other games, including Wizardry
VIII; (3) minimal miss chance reduction; (4) a lack of special equipment usable
only by them; (5) very low stat requirements, which makes subsequent class
changes more awkward; (6) by the time you reach the game's midpoint, a Bard who
routinely practices Music will be able to allocate plenty of skill points to
Thaumaturgy and thus almost catch up to the Mage in spellcasting ability.
These together argue for not including a Mage in your party after the early
game.

### SECTION 4C - Character class: Priest

```
Starting Equipment : Quarterstaff, Robes (U), Robes (L), Sandals, Potion of Lt.
                     Heal
Attributes Required: PIE 12, PER 8
Starting Hit Points: 1d4+3 (4 to 7)
Level-up Hit Points: 1d4+3 (4 to 7)
Miss Chance Per Lev: 1d4 (1 to 4)
Spellbook          : Priest
Mana Regeneration  : Fire 2, Water 2, Air 3, Earth 3, Mental 2, Magic 3
Primary Skills     : Theology
Additional Skills  : Oratory, Theology
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light     16% + 2%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  32% + 2%/level
                     Paralysis  8% + 2%/level  Psionic   20% + 2%/level
                     Air       16% + 2%/level  Lifeforce 40% + 2%/level
                     Poison    24% + 2%/level  Magic     20% + 2%/level
Experience Needed  : Level 2    1,250    Level 8     80,000
                     Level 3    2,500    Level 9    160,000
                     Level 4    5,000    Level 10   320,000
                     Level 5   10,000    Level 11   640,000
                     Level 6   20,000    Level 12+ +375,000 per level
                     Level 7   40,000
```

The Priest has the second most useful spellbook and excellent mana regeneration
rates at game start, and unlike the Mage isn't so blatantly terrible later in
the game; their hit point growth and miss chance reduction rates are good for a
caster, and their resistances are also pretty good.  This is a good class to
have on hand in the early game.  The Priest also can use all the items that a
Bishop can; there are many items only usable by a Priest or a Bishop.

### SECTION 4D - Character class: Thief

```
Starting Equipment : Cutlass, Cloth Shirt, Cloth Pants, Buskins, Dirk
Attributes Required: DEX 12, SPD 8
Starting Hit Points: 1d4+2 (3 to 6)
Level-up Hit Points: 1d4+2 (3 to 6)
Miss Chance Per Lev: 1d4 (1 to 4)
Spellbook          : None
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 1, Magic 1
Primary Skills     : Legerdemain, Skulduggery
Additional Skills  : Legerdemain, Skulduggery, Ninjutsu
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light     28% + 3%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis   8% + 1%/level
                     Paralysis 28% + 2%/level  Psionic   16% + 2%/level
                     Air       28% + 3%/level  Lifeforce  8% + 2%/level
                     Poison    24% + 2%/level  Magic     28% + 3%/level
Experience Needed  : Level 2      900    Level 8     57,600
                     Level 3    1,800    Level 9    115,200
                     Level 4    3,600    Level 10   230,400
                     Level 5    7,200    Level 11   460,800
                     Level 6   14,400    Level 12+ +225,000 per level
                     Level 7   28,800
```

The Thief advances in levels quickly and gets a little boost to Skulduggery at
the start, making building up this skill less tedious.  After the very early
game, the lack of spellcasting ability and mediocre physical combat ability
make the Thief a very poor choice, even given the cheap level-ups and good
resistances.  The Thief can equip a reasonable number of mid-power items, but
the only item in the game usable only by the Thief is the Thieves' Dagger,
which isn't of much use.  The Bard is otherwise in almost every way equal or
superior to the Thief; the Thief's other advantage is the marginally higher hit
point total.  Of special note is the Faerie's ability to switch freely between
Thief and Bard, described in section 3F.

### SECTION 4E - Character class: Ranger

```
Starting Equipment : Short Bow, Elm Arrow, Suede Doublet, Suede Pants, Buskins
Attributes Required: STR 10, INT 8, PIE 8, VIT 11, DEX 10, SPD 8, PER 8
Starting Hit Points: 2d4+5 (7 to 13)
Level-up Hit Points: 1d5+5 (6 to 10
Miss Chance Per Lev: 1d4+1 (2 to 5)
Spellbook          : Alchemist (starting at level 3)
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 1, Magic 1
Primary Skills     : Bows, Scouting
Additional Skills  : Legerdemain, Skulduggery, Ninjutsu, Alchemy
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light      8% + 2%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  28% + 2%/level
                     Paralysis  8% + 2%/level  Psionic   28% + 3%/level
                     Air       12% + 2%/level  Lifeforce 40% + 2%/level
                     Poison     8% + 3%/level  Magic     12% + 3%/level
Experience Needed  : Level 2    1,400    Level 8     89,600
                     Level 3    2,800    Level 9    179,200
                     Level 4    5,600    Level 10   358,400
                     Level 5   11,200    Level 11   716,800
                     Level 6   22,400    Level 12+ +415,000 per level
                     Level 7   44,800
```

The Ranger's strong points include good hit point growth and miss chance
reduction, broad stat requirements that are both easy to meet and make future
classes easier to enter, access to Alchemist spells and Ninjutsu, and good
resistances.  However, the Ranger cannot equip very much in the way of gear;
even most leather armor is off-limits.  The Ranger is best attacking from the
back ranks with extended or long-range weapons, which include the Spear of
Death and the Elven Bow.  Special Ranger equipment includes the Chamail Doublet
and Chamail Pants (which however aren't even as good as early-game leather
armor!) and the Forest Cape.  Additionally, the Ranger has high experience
point requirements and has many level-up skill points automatically diverted
into Bows and Scouting, which aren't the best places for them to go.  A Ranger
in the back ranks is still a reasonable choice for the endgame, because of the
good hit point and miss reduction development; you can easily train Bows to 51
by then to prevent diversion of skill points there.  Rangers do not have the
special ability to critically hit often with Bows that they have in Wizardry
VII and VIII.

### SECTION 4F - Character class: Alchemist

```
Starting Equipment : Staff, Robes (U), Robes (L), Sandals, Stink Bomb
Attributes Required: INT 13, DEX 13
Starting Hit Points: 1d4+2 (3 to 6)
Level-up Hit Points: 1d4+3 (4 to 7)
Miss Chance Per Lev: 1d3 (1 to 3)
Spellbook          : Alchemist
Mana Regeneration  : Fire 3, Water 2, Air 3, Earth 3, Mental 2, Magic 2
Primary Skills     : Alchemy
Additional Skills  : Alchemy
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light      4% + 1%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  16% + 1%/level
                     Paralysis  8% + 1%/level  Psionic   16% + 1%/level
                     Air       12% + 2%/level  Lifeforce 16% + 3%/level
                     Poison    16% + 1%/level  Magic     24% + 3%/level
Experience Needed  : Level 2    1,100    Level 8     70,400
                     Level 3    2,200    Level 9    140,800
                     Level 4    4,400    Level 10   281,600
                     Level 5    8,800    Level 11   563,200
                     Level 6   17,600    Level 12+ +312,000 per level
                     Level 7   35,200
```

The Alchemist has many of the same problems as the Mage, with identical poor
resistances and miss chance reduction.  The Alchemist does get some special
perks that make it decent: non-Silenceable spellcasting; rapid level-ups
compared to all other spellcasting classes; and robust hit point growth that is
more like a hybrid fighter-caster than a pure spellcaster.  These factors make
the Alchemist a good midgame pure spellcaster.  The Alchemist also is the only
class that can equip the Medicine Bag, should you find one in the late game.
Alchemists are still not good enough to be optimal in the endgame compared to a
hybrid fighter-caster.

### SECTION 4G - Character class: Bard

```
Starting Equipment : Sling, Bullet Stone, Cloth Shirt, Cloth Pants, Lute
Attributes Required: INT 10, DEX 12, SPD 8, PER 12
Starting Hit Points: 1d4+1 (2 to 5)
Level-up Hit Points: 1d3+2 (3 to 5)
Miss Chance Per Lev: 1d4 (1 to 4)
Spellbook          : Mage (starting at level 3)
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 1, Magic 1
Primary Skills     : Music
Additional Skills  : Music, Oratory, Legerdemain, Skulduggery, Ninjutsu,
                     Thaumaturgy
Special Abilities  : Instrument use
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light     28% + 3%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis   8% + 1%/level
                     Paralysis 28% + 2%/level  Psionic   16% + 2%/level
                     Air       28% + 3%/level  Lifeforce  8% + 2%/level
                     Poison    24% + 2%/level  Magic     28% + 3%/level
Experience Needed  : Level 2    1,250    Level 8     80,000
                     Level 3    2,500    Level 9    160,000
                     Level 4    5,000    Level 10   320,000
                     Level 5   10,000    Level 11   640,000
                     Level 6   20,000    Level 12+ +375,000 per level
                     Level 7   40,000
```

The Bard's ability to cast spells using instruments without spell points is
incredibly powerful in the early game and the midgame.  This mostly revolves
around the Sleep spell cast by the Lute, with a nod to the Bless spell cast by
the Angel's Tongue.  Always having a Bard in the early game and midgame makes
those phases of the game much easier.  Bards also have good resistances
(identical to a Thief's), access to the Mage spellbook, and can equip many mid-level
weapons and armor (similar to a Thief).  Bards also gain experience
relatively fast for a fighter-caster hybrid.  On the other hand, Bards don't
have many hit points; they actually have fewer than Priests or Alchemists.
Monsters become quite resistant to Sleep by the late game, and you should have
multiple characters able to cheaply throw Sleep or Hold Monsters by then.
Also, no new instruments show up to truly pick up the slack; even the Horn of
Prometheus, which can cast free Fireballs and shows up soon before the start of
the endgame, isn't quite as good as it sounds.  The Bard also has poor
Lifeforce resistance, which is useful for resisting the powerful death spells
that become common in the late game.  For these reasons, you will probably want
to leave the Bard out of your endgame party.

A special note on Wizardry VIII: Bards burn tons of stamina in Wizardry VIII,
and only females have a stamina regeneration item available early in the game.
While this isn't too restricting since you can freely change class before
Wizardry VIII, if you are building characters thematically this is still good
to keep in mind.

### SECTION 4H - Character class: Psionic

```
Starting Equipment : Dagger, Robes (U), Robes (L), Sandals, Shadow Cloak
Attributes Required: STR 10, INT 14, VIT 14, PER 10
Starting Hit Points: 1d3+2 (3 to 5)
Level-up Hit Points: 1d3+2 (3 to 5)
Miss Chance Per Lev: 1d3 (1 to 3)
Spellbook          : Psionic
Mana Regeneration  : Fire 2, Water 2, Air 2, Earth 2, Mental 4, Magic 2
Primary Skills     : Theosophy
Additional Skills  : Oratory, Theosophy
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light     32% + 3%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  20% + 1%/level
                     Paralysis 32% + 3%/level  Psionic   40% + 3%/level
                     Air        4% + 1%/level  Lifeforce 20% + 3%/level
                     Poison    28% + 1%/level  Magic     20% + 3%/level
Experience Needed  : Level 2    1,250    Level 8     80,000
                     Level 3    2,500    Level 9    160,000
                     Level 4    5,000    Level 10   320,000
                     Level 5   10,000    Level 11   640,000
                     Level 6   20,000    Level 12+ +375,000 per level
                     Level 7   40,000
```

The Psionic spellbook is the least useful of the four spellbooks in Wizardry
VI.  Psionics have decent resistances, and the unique ability to equip the PK
Crystal, which is a reasonably likely random drop in the late game.  They make
a good mid-game temporary class as well.  They otherwise have many of the same
weaknesses as Mages, and thus are a poor choice for the late game.

### SECTION 4I - Character class: Valkyrie

```
Starting Equipment : Spear, Fur Halter, Chamois Skirt, Leather Helm, Sandals
Attributes Required: STR 10, PIE 11, VIT 11, DEX 10, SPD 11, PER 8, Female
Starting Hit Points: 1d5+4 (5 to 9)
Level-up Hit Points: 1d5+4 (5 to 9)
Miss Chance Per Lev: 1d4+1 (2 to 5)
Spellbook          : Priest (starting at level 3)
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 1, Magic 1
Primary Skills     : Pole & Staff
Additional Skills  : Oratory, Theology
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light      8% + 2%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  28% + 2%/level
                     Paralysis  8% + 2%/level  Psionic   28% + 3%/level
                     Air       12% + 2%/level  Lifeforce 40% + 2%/level
                     Poison     8% + 3%/level  Magic     12% + 3%/level
Experience Needed  : Level 2    1,100    Level 8     70,400
                     Level 3    2,200    Level 9    140,800
                     Level 4    4,400    Level 10   281,600
                     Level 5    8,800    Level 11   563,200
                     Level 6   17,600    Level 12+ +312,000 per level
                     Level 7   35,200
```

The Valkyrie is a hybrid fighter-caster that can equip essentially all of the
heavy weapons and armor that a Fighter can, and advances in level rapidly for a
fighter-caster hybrid, almost as fast as a Fighter.  The Valkyrie gets the same
good resistances as the Ranger, and can easily train Pole and Staff by practice
to maximize skill points available for manual allocation.  The Valkyrie also
has broad and modest stat requirements that make it easy to switch both to and
from.  Soon before the endgame begins, you can find a Maenad's Lance, an
Extended weapon usable only by Valkyries that makes a back-rank Valkyrie a
potent fighter in the late game.  One or more Valkyries are an excellent
addition to the party in all stages in the game.  The only way in which
Valkyries are inferior to Lords is the lower hit point growth.

### SECTION 4J - Character class: Bishop

```
Starting Equipment : Quarterstaff, Robes (U), Robes (L), Mitre, Sandals
Attributes Required: INT 15, PIE 15, PER 8
Starting Hit Points: 1d4+2 (3 to 6)
Level-up Hit Points: 1d3+2 (2 to 5)
Miss Chance Per Lev: 1d3 (1 to 3)
Spellbook          : Mage (at even levels), Priest (at odd levels)
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 3, Magic 3
Primary Skills     : Thaumaturgy, Theology
Additional Skills  : Oratory, Thaumaturgy, Theology
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light     16% + 2%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  32% + 2%/level
                     Paralysis  8% + 2%/level  Psionic   20% + 2%/level
                     Air       16% + 2%/level  Lifeforce 40% + 2%/level
                     Poison    24% + 2%/level  Magic     20% + 2%/level
Experience Needed  : Level 2    1,500    Level 8     96,000
                     Level 3    3,000    Level 9    192,000
                     Level 4    6,000    Level 10   384,000
                     Level 5   12,000    Level 11   768,000
                     Level 6   24,000    Level 12+ +445,000 per level
                     Level 7   48,000
```

Bishops are pure casters that learn from both the Mage and Priest spellbooks.
They do have access to the equipment usable only by Priests or Bishops, and
identical resistances, but they have both lower hit point growth and miss
chance reduction compared to the Priest, along with lower mana regeneration at
game start.  They have the second-highest experience requirements in the game,
second only to Ninja.  Their starting Mitre is hard to replace, but is not
powerful enough to be worth more than a mention.  The ability to learn from two
spellbooks sounds powerful, but it is only useful if you never change anyone's
class, as it is easy to rack up many more spells through several class changes
with the same amount of experience.  All of this adds up to Bishops only being
useful as an intermediate step in class changing; a Bishop is a poor choice for
both the early game and the late game.

### SECTION 4K - Character class: Lord

```
Starting Equipment : Broadsword, Quilt Tunic, Quilt Legging, Steel Helm,
                     Buskins
Attributes Required: STR 12, INT 9, PIE 12, VIT 12, DEX 9, SPD 9, PER 14
Starting Hit Points: 1d7+7 (8 to 14)
Level-up Hit Points: 1d5+5 (6 to 10)
Miss Chance Per Lev: 1d4+1 (2 to 5)
Spellbook          : Priest (starting at level 3)
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 1, Magic 1
Primary Skills     : Sword
Additional Skills  : Oratory, Theology
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light      8% + 2%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  32% + 2%/level
                     Paralysis  8% + 2%/level  Psionic   20% + 1%/level
                     Air       12% + 2%/level  Lifeforce 40% + 2%/level
                     Poison     8% + 3%/level  Magic     16% + 3%/level
Experience Needed  : Level 2    1,400    Level 8     89,600
                     Level 3    2,800    Level 9    179,200
                     Level 4    5,600    Level 10   358,400
                     Level 5   11,200    Level 11   716,800
                     Level 6   22,400    Level 12+ +415,000 per level
                     Level 7   44,800
```

The Lord is for most purposes a Valkyrie that is allowed to be male and has
higher stat requirements.  It can equip most of the equipment that a Fighter or
Valkyrie can; the couple of exceptions are inconsequential.  The Lord requires
considerably more experience to advance in level, and has resistances that are
good but not quite as good as the Valkyrie.  For all of these relative
disadvantages, you might think that Lords have special equipment that only they
can use, but in fact there is nothing of the kind; there is no such thing as a
Garb of Lords or an Odinsword in Wizardry VI, VII, or VIII.  This is enough to
convince many people that they are a poor choice for females, but that's not
quite the case.  If you meet the higher stat requirements, this can make
subsequent class changes easier.  Lords also get more hit points than
Valkyries; the difference is enough that even with the significant difference
in level advancement, Lords will have more hit points unless you get many
millions of experience, which you won't get unless you level grind in the late
game.  There is also a lot of equipment usable only by Fighters, Valkyries, and
Lords.

### SECTION 4L - Character class: Samurai

```
Starting Equipment : Katana, Wakizashi, Robes (U), Robes (L), Sandals
Attributes Required: STR 12, INT 11, VIT 9, DEX 12, SPD 14, PER 8
Starting Hit Points: 2d4+5 (7 to 13)
Level-up Hit Points: 1d5+4 (5 to 9)
Miss Chance Per Lev: 1d4+2 (3 to 6)
Spellbook          : Mage (starting at level 3)
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 1, Magic 1
Primary Skills     : Sword
Additional Skills  : Oratory, Thaumaturgy, Kirijutsu
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light     28% + 3%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  28% + 1%/level
                     Paralysis 28% + 3%/level  Psionic   20% + 1%/level
                     Air       12% + 2%/level  Lifeforce 32% + 2%/level
                     Poison     8% + 3%/level  Magic     12% + 3%/level
Experience Needed  : Level 2    1,400    Level 8     89,600
                     Level 3    2,800    Level 9    179,200
                     Level 4    5,600    Level 10   358,400
                     Level 5   11,200    Level 11   716,800
                     Level 6   22,400    Level 12+ +415,000 per level
                     Level 7   44,800
```

The Samurai is a fighter-caster hybrid who specializes in inflicting damage,
doing so by learning from the Mage spellbook that has the best damage spells,
learning the Kirijutsu skill to inflict critical hits in melee, getting the
best miss chance reduction rate available, and able to equip special highly
effective swords that few or no other classes are capable of using.  This comes
at the price of having poor armor for a class that is only effective fighting
on the front ranks.  Samurai never have access to good helmets, gloves, or
footwear, and even the best body armor available to them (which only Samurai
can use) isn't quite as good as what a heavily armored Fighter/Lord/Valkyrie or
a highly skilled Monk or Ninja can achieve.  This weakness can be mitigated via
the Armor Shield spell and learning to Hide in combat from another class.
Their offensive capabilities are certainly worth this effort, though.  The
first good specialty weapon available to Samurai is the No-Dachi that becomes
available during the midgame; soon before the endgame begins, the devastating
Muramasa Blade can be found.  As the best weapons Samurai can wield are mostly
swords, just relying on practice will increase Sword skill enough to enable you
to put most skill points into Thaumaturgy; this makes the Samurai a strong
spellcaster by the late game.  The Samurai advances rather slowly, but is
powerful enough to be worth the trouble.

### SECTION 4M - Character class: Monk

```
Starting Equipment : Bo, Robes (U), Robes (L), Sandals, Shuriken
Attributes Required: STR 13, INT 8, PIE 13, DEX 10, SPD 13, PER 8
Starting Hit Points: 1d4+3 (4 to 7)
Level-up Hit Points: 1d4+3 (4 to 7)
Miss Chance Per Lev: 1d4+1 (2 to 5)
Spellbook          : Psionic (starting at level 3)
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 1, Magic 1
Primary Skills     : Hands & Feet, Theosophy
Additional Skills  : Hands & Feet, Oratory, Ninjutsu, Theosophy, Kirijutsu
Special Abilities  : Ninjutsu reduces AC
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light     40% + 3%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  20% + 1%/level
                     Paralysis 24% + 2%/level  Psionic   40% + 2%/level
                     Air       12% + 2%/level  Lifeforce 32% + 3%/level
                     Poison    28% + 1%/level  Magic     12% + 2%/level
Experience Needed  : Level 2    1,400    Level 8     89,600
                     Level 3    2,800    Level 9    179,200
                     Level 4    5,600    Level 10   358,400
                     Level 5   11,200    Level 11   716,800
                     Level 6   22,400    Level 12+ +415,000 per level
                     Level 7   44,800
```

The Monk is a hybrid fighter-caster that casts from the inferior but still
useful Psionic spellbook, and can learn Ninjutsu and Kirijutsu.  Monks are very
good at fighting bare-handed, and are in fact generally more effective fighting
bare-handed; the weapons worth equipping for a Monk are all not Short range and
are a good excuse to put your Monk in the back ranks.  The legendary Zatoichi
Bo is a special Monk weapon that is incredibly powerful, but don't count on
finding one as it is a rare drop in the endgame.  Monks cannot equip much in
the way of armor, but with enough Ninjutsu training and levels will not need it
for the AC reduction.  Resistances are more problematic; Monk resistances
aren't very good because there's a heavy focus in the not-all-that-useful Light
resistance.  Equipment other than weaponry should thus focus on enhancing
resistances, not AC.  The Monk advances in level rather slowly, and doesn't get
good hit point growth, but is still a good choice as a transition class while
class changing to pick up Psionics, Ninjutsu, and Kirijutsu, and is also a
strong candidate for a late-game hybrid in the back ranks.

### SECTION 4N - Character class: Ninja

```
Starting Equipment : Ninja Garb (U), Ninja Garb (L), Ninja Cowl, Tabi Boots,
                     Shuriken
Attributes Required: STR 12, INT 10, PIE 10, VIT 12, DEX 12, SPD 12
Starting Hit Points: 1d5+3 (4 to 8)
Level-up Hit Points: 1d5+3 (4 to 8)
Miss Chance Per Lev: 1d4+2 (3 to 6)
Spellbook          : Alchemist (starting at level 5)
Mana Regeneration  : Fire 1, Water 1, Air 1, Earth 1, Mental 1, Magic 1
Primary Skills     : Hands & Feet, Ninjutsu
Additional Skills  : Hands & Feet, Legerdemain, Skulduggery, Ninjutsu, Alchemy,
                     Kirijutsu
Special Abilities  : Ninjutsu reduces AC; bonus to Critical Hit chance
Resistances        : Fire       8% + 2%/level  Missile    8% + 2%/level
                     Light     40% + 3%/level  Acid       8% + 1%/level
                     Cold       8% + 2%/level  Hypnosis  32% + 2%/level
                     Paralysis 28% + 2%/level  Psionic   16% + 1%/level
                     Air       28% + 3%/level  Lifeforce  8% + 2%/level
                     Poison    24% + 2%/level  Magic      4% + 2%/level
Experience Needed  : Level 2    1,500    Level 8     96,000
                     Level 3    3,000    Level 9    192,000
                     Level 4    6,000    Level 10   384,000
                     Level 5   12,000    Level 11   768,000
                     Level 6   24,000    Level 12+ +475,000 per level
                     Level 7   48,000
```

The Ninja is the ultimate hybrid, capable of fighting on the front ranks,
learning Alchemist spells starting at level 5, and can learn all of
Legerdemain, Skulduggery, Ninjutsu, and Kirijutsu.  Despite this jack of all
trades appearance, the Ninja gets the best miss chance reduction rate in the
game and a special +5% bonus to critical hits.  The Ninja is thus a strong
choice in the midgame and the endgame, even with the slowest level advancement
in the game.  This remains true even though the Ninja does not get any special
tier 4 weapon; the tier 2 and 3 weaponry a Ninja can use are still reasonable
in the endgame.  Like the Monk, the Ninja mostly relies on Ninjutsu and levels
for AC, and can only equip special armor; also like the Monk, the Ninja has
unexciting resistances that focus too heavily on Light resistance.  An endgame
Ninja has poor Lifeforce resistance and will want to look for a way to cover
that.  The extra resistances Faeries receive thus make them particularly good
Ninja, even without the Cane of Corpus available.

## Suggested ways to build a party

### SECTION 5A - Preplanned party for the entire game

If you don't want to bother with a ton of class changes, or spend much time
planning party development, the following canned plan will help you get a lot
out of just two class changes per character for the entire game.

Be sure to start with as many bonus stat points as possible, at least 18 per
character (you can use Mad God's Cosmic Forge utility to guarantee this many);
a few of the start combinations below require a lot of points, and so do some
of the first class changes.  You may want to apply the carrying capacity fix as
well, since you won't have many spare points to put into Strength.  It also
helps to spend a bit of time rolling for a higher number of starting skill
points, especially for the Mage and Priest.

You still need to pay attention to stats gained at level up, to make sure you
can make class changes in a reasonable time frame (by 10th level at the
latest).

* Start with the following party (starting points required are indicated in
  parentheses):
  - Male Dwarf Ninja (15): put 1 skill point into Kirijutsu, 1 skill point into
    Legerdemain, and split the rest between Skulduggery and Alchemy.
  - Female Felpurr Valkyrie (5): put all skill points into Theology.
  - Female Rawulf Monk (16): put 1 skill point into Kirijutsu, the rest into
    Theosophy.
  - Female Faerie Bard (2): put some stat points into Piety for the first class
    change; put 1 skill point into Legerdemain, the rest into Thaumaturgy.
  - Male Mook Mage (2): put some stat points into Piety and Personality for the
    first class change; put all skill points into Thaumaturgy; choose Energy
    Blast and Armor Shield for starting spells.
  - Female Elf Priest (2): put some stat points into Dexterity and Personality
    for the first class change; put all skill points into Theology; choose Heal
    Wounds and Bless for starting spells.

  Stay as these classes until level 7 at the very earliest.  The idea is to
  hold out until you can reach Kuwali Kubona and buy spellbooks from her, to
  maximize the number of spells learned with just two class changes.  Level 7
  is also the minimum needed to learn 5th level spells without class changes.
  In practice, if you wait until Kuwali Kubona to start class changing, you'll
  probably be around level 9.

  Do not use level up spell picks on Knock-Knock, Direction, or Detect Secret;
  buy these spells from Queequeg.  You should also avoid using picks on as many
  of Kuwali Kubona's spells as possible (except for the Ninja who can't use
  those), although it's painful to go entirely without Cure Lesser Condition
  for that long.

  How to develop each character:
  - Dwarf Ninja: he will be your primary lockpicker early in the game, so to
    avoid some boring grinding it helps to directly apply skill points to
    Skulduggery.  Use bare hands exclusively to attack until he reaches 51
    Hands & Feet skill.  Hide in combat all the time to train Ninjutsu.  It
    will be difficult to reach even 3rd level Alchemy spells before levels
    start becoming expensive, so you only need to raise Alchemy to 18.
    Priority spell picks are Heal Wounds, Acid Splash, Poison, Blinding Flash,
    and Cure Lesser Condition.
  - Felpurr Valkyrie: she should use a polearm (the starting Spear, then a better
    one from Queequeg) to start out; once she reaches 51 Pole & Staff she can
    start developing other weapon skills.  Put as many skill points as possible
    into Theology, at least up to 36 for level 3 spells.  Priority spell picks
    are Heal Wounds, Dispel Undead, Silence, Cure Paralysis, Sane Mind, and
    Blades.
  - Rawulf Monk: like the Ninja, she should also rely entirely on bare hands to
    attack when starting out, and hide all the time in combat to train
    Ninjutsu.  Put all skill points into Theosophy, at least up to 36 for level
    3 spells.  Priority spell picks are Heal Wounds, Mental Attack, Silence,
    Mindread, Cure Paralysis, Sane Mind, and Psionic Blast.
  - Faerie Bard: use the Lute in every combat round early on, for its powerful
    effect and to train Music quickly.  Try to have her disarm a chest or pick
    a lock at least once just for the first Skulduggery point; do this for
    everyone with Skulduggery available but at 0 skill.  Get in some Hiding
    practice too.  She can optionally flip to Thief and back to Bard a few
    times to get more spells and skill points; if you do this, the last time
    she is a bard she will need to gain a Piety point most levels for the first
    serious class change.  Put all skill points into Thaumaturgy; use spell
    picks on Energy Blast and Armor Shield first, then on Magic Missile (just
    to get Magic spell point growth going) and Fireball.  If you do the
    Thief/Bard trick a few times, you should be able to learn the level 5 spell
    Anti-Magic for the late game.
  - Mook Mage: pour all skill points into Thaumaturgy, bringing it up to 72 so
    you can learn the level 5 spell Anti-Magic.  Pick up Magic Screen as soon
    as you can as well, since it's very useful to have starting in the Amazulu
    Pyramid.  Other spells to get along the way include Fireball, Stink Bomb,
    Iceball, and Deep Freeze.
  - Elf Priest: pour all skill points into Theology, and prioritize learning
    Dispel Undead, Enchanted Blade, Silence, Cure Paralysis, Blades, and Cure
    Poison.

* Once you are content with the spells you have learned, transition to the
  intermediate party as follows:
  - Dwarf: change to Samurai; practice Sword skill to at least 51 (ideally before
    switching); devote all skill points to Thaumaturgy, aiming for 72 skill
    points to learn Anti-Magic.
  - Felpurr: change to Ranger; practice Bow skill to at least 51 (ideally before
    switching), and also Ninjutsu; put 1 skill point into Legerdemain, then put
    all skill points into Alchemy.  With a little luck and dedication, you can
    reach 54 skill points for some 4th-level Alchemist spells.
  - Rawulf: change to Samurai; develop similarly to the Dwarf Samurai.
  - Faerie: change to Priest (see below for caveat); make a point of learning
    Dispel Undead.
  - Mook: change to Lord; learn to fight some in the front ranks; be sure to
    learn Dispel Undead.
  - Elf: change to Bard; practice Music and Ninjutsu; put 1 skill point into
    Legerdemain, then all into Thaumaturgy, aiming for 72 skill points to learn
    Anti-Magic.

  Change only one character at a time, and train the character for a few levels
  before starting the next, since very low level characters are a serious
  liability in combat.  You'll need to shuffle around characters to keep the
  best fighters in the front ranks.

  Once you change your Dwarf's class, you will no longer have a character
  suitable for unlocking doors and chests.  You can either train a different
  character in Skulduggery (be warned, this will take a fair bit of grinding
  and reloading), or rely on the Knock-Knock spell from now on.  The ninja
  armor is also temporarily useless, but don't throw it away.

  Don't forget to buy more spellbooks for characters that can now use them!

  The statistics to watch for most when gaining levels: the Dwarf needs a lot
  of Personality, and the Faerie needs a lot of both Strength and Vitality
  (enough that you may want to consider alternate class switching plans, such
  as switching her to Ranger too).

* Continue with the intermediate party until you are at least as high a level
  as before the first change; it may take until level 10 or 11 to accrue
  enough skill points to learn Anti-Magic.  Not everyone needs to know that
  spell, but I can't emphasize enough how strong it is in the late game.
  
* Then start the transition to the final party:
  - Dwarf: change to Lord
  - Felpurr: change to Samurai
  - Rawulf: change to Valkyrie
  - Faerie: change to Ninja
  - Mook: change to Monk
  - Elf: change to Ranger

  Don't progress beyond the Hall of the Dead until all class changes are done.

  This party is the same as the late game party in Section 5B, and the advice
  from this point is much the same.


### SECTION 5B - General optimal party construction

This section describes in general what to do if you don't mind spending more
time developing your characters.

For reasons listed in previous sections, an optimal starting party will have:
* at least 1 Bard (for the Lute)
* as many other characters as possible Mages or Priests (for the enhanced mana
  regeneration capacity, the starting spells, and low initial stat point cost)
* 4-5 female characters
* at least 1 Elf and 1 Faerie (unique racial abilities).  Add in at least 1
  Mook if you plan to play a party all the way to Wizardry VIII.

A suggested optimized initial party therefore goes along the lines of:
- Male Dwarf Priest
- Female Rawulf Priest
- Female Elf Priest or Mage
- Female Felpurr Mage
- Male Mook Mage
- Female Faerie Bard

You should consider replacing the Felpurr with a Hobbit if you plan to play the
party all the way to Wizardry VIII.

These all require few initial stat points to become eligible for.  Direct
remaining stat points so that an immediate class switch to a real class can be
made, then dump any remainder into Strength and Vitality.  The maximum number
of bonus points you can get naturally is 26, with 18 the highest typical number
of starting points.  Mad God's utility will let you automatically get 18-26
points if you don't feel like sitting at your keyboard for hours.  The Bard
should split initial skill points between Skulduggery and Thaumaturgy, and put
1 point into Legerdemain; everyone else should put all skill points into magic
skill.  Mages should take Energy Blast and Armor Shield as their spells;
Priests should take Heal Wounds and either Stamina or Bless.

Which classes to target for immediate class change depends on your long-term
plans and personal preference, but I strongly recommend including a non-Faerie
Bard, a non-Faerie Samurai, a Ninja, and at least one non-Faerie Lord/Valkyrie.

You will want to switch everyone in the party to these classes before reaching
level 2, to maximize miss chance reduction potential.  The Lute will allow you
to neutralize any threat on the castle ground level, even with a party as
fragile as this one at Expert level.  Before the switch, the Faerie Bard can
get a little practice in Ninjutsu, and everyone else can get in a bit of
Oratory practice.

Between this class change and the endgame, follow the general advice in section
2 and your personal preferences.  I recommend teaching everyone the Ninjutsu
and Kirijutsu skills, because these are great for enhancing your characters'
melee combat potential, even for spellcasters; this should go along with as
many of the important spells listed in section 2D as possible.  If you are
developing your characters with Wizardry VII in mind, also keep in mind the
information in section 6.

Once you are approaching the end of the Hall of the Dead, I recommend
transitioning to a final party of:
- Lord (wielding The Avenger)
- Samurai (wielding Muramasa Blade)
- Faerie Ninja (wielding Bushido Blade; don't make your Faerie one of the other
    classes here other than maybe Monk, since she won't be able to equip the
    weapons and armor any other class uses)
- Valkyrie (wielding Maenad's Lance; put her in the back ranks)
- Monk (wielding one of Cat'O Nine Tail, Spear of Death, Elven Bow, or Hayai
    Bo; if you are really lucky you can get a Zatoichi Bo in the endgame)
- Ranger (wielding one of Cat'O Nine Tail, Spear of Death, or Elven Bow; a
    Thief, Ranger, or Bard on the front lines is a bad idea in the endgame)

For the Monk and Ranger, the Cat'O Nine Tail and Spear of Death are preferable
because they are one handed, and pair up nicely with Rocks of Reflection to
greatly increase endgame defense at little cost in offense.

Split the unique Tier 4 heavy armor between the Lord and Valkyrie, as the
resistances they supply are more important than AC in the endgame.  Equipping
all the Ebony and Mantis equipment on a single character is overkill.

Advance everyone to at least level 10 before triggering the end of the midgame
(the second meeting with the Vampire King); this shouldn't take too long
spinning in place near the magic restoration fountain in the Hall of the Dead.

## Transferring to Wizardry VII

### SECTION 6A - Statistics and skills that transfer to Wizardry VII

Race, class, and sex all remain the same.

A character of level 1 to 5 will transfer at that level.  Any levels and
experience above level 5 are lost.  You do retain class rank, but that is only
for show.

Statistics generally remain intact; statistics of 13 or more may get reduced in
the process, especially for lower-level characters.  This potential reduction
does include Karma.  It is possible to get a stat lowered below the normal
minimum for your race and class.  It is also possible for a stat as high as the
maximum of 20 to survive the transfer intact (getting stats that high in
Wizardry VI requires the invocation of items such as Ankhs of Might).

All skills other than Mythology will transfer to some degree.  Skill levels
will transfer at a level up to a certain cut-off.  This cut-off is random and
determined for each skill individually.  This cut-off is usually somewhere in
the range of the high 20s to the low 40s, is independent of whether your
current class can learn that skill naturally, and is proportionately reduced if
you transfer a character below level 20; this is the only area I know of where
levels above 5 make a difference.

Mythology skill, as well as the new Swimming, Climbing, Diplomacy, and Mapping
skills, starts at 0 for all transferred characters.

Hit points are an apparently random number, somewhere in the low 40s for a
level 5 character, and appropriately reduced at lower levels.  Spellcasters get
magic points similarly determined, but in about the high 30s; you will get
these spell points even if you transfer with no spells in a realm.

Miss chance transfers in the low 60s for characters of 5th level or above;
lower level characters get a proportionately higher miss chance.  Class makes
no difference that I have seen, so there isn't an urgent need to transfer over
a bunch of Samurai and Ninja.

All spells above level 3 are forgotten.  Each spell of level 3 or below has a
random chance of being forgotten; this loss chance is roughly 1 in 8 for level
1 spells, 1 in 4 for level 2 spells, and 1 in 2 for level 3 spells.  These loss
rolls are independent of the level of magic skills transferred and of what
class you currently are.

Mana regeneration in Wizardry VII will actually adjust during the game upon
class changes and adjust to statistics when you level up, so while your current
class does affect mana regeneration upon transfer, it is not a major long-term
consideration.

### SECTION 6B - Items that transfer to Wizardry VII

There are two classes of items that transfer to Wizardry VII: those that
transfer freely, and those that transfer in a special way.

Items that transfer freely will transfer to Wizardry VII in any quantity, with
the only limit being the size of the inventories in Wizardry VII (20 slots per
character compared to 24 in Wizardry VI).  Whether these items are equipped or
in your Swag Bag makes no difference, and they will transfer all the way up to
the stack limit of 250.  These items include:

* most potions.  This includes Resurrection potions, Stink Bombs, Fire Bombs,
  Cherry Bombs (which are stronger in Wizardry VII), Acid Bombs, and Poison
  Bombs.  Deadly Poison potions do not transfer.
* all Tier 1 weapons and armor.  Any weapon or armor that Queequeg sells will
  transfer freely.
* all Tier 2 weapons and armor.  Any weapon that Smitty sells will transfer
  freely, other than the Vulcan Hammer.  Tier 2 armor includes all chain and
  most plate armor, as well as ninja armor, Mitres, Round Shields, and Heater
  Shields.
* Barbed Arrows (sold by Mai-Lai)
* some Tier 3 armor sold by Mai-Lai: Bronze Cuirass, Leather Greaves, Studded
  Leather, Stud Chausses, Phrygian Cap, Helm & Coif, Kabuto, Chamois Gloves,
  Copper Gloves.
* Sparklers, Firecrackers, Icicles, Skyrockets, Bottlerockets (sold by the
  Caterpillar)
* Wizard's Cone
* Crystal Wand
* Rod of Sprites (sold by the Queen of Faeries; this is the ideal offhand
  weapon for a Wizardry VII Faerie Ninja, so be sure to get one)
* a couple of instruments: Lute, Angel's Tongue.  These are the only two
  instruments that will transfer at all.
* PK Crystal (random drop from Keeper of Crystal)
* Amulet of Life
* Ankh of Life
* Silver Cross
* Ring of Stars
* Diamond Ring (from special ending; transfers all the way to Wizardry VIII)
* Cameo Locket

The Studded Leather and Stud Chausses are the best freely transferrable body
armor that can be bought for many classes; this includes the Ranger, who can't
equip them in Wizardry VI but can in VII.  For heavy fighters and Rangers, the
Helm & Coif is the best such helmet.  Each heavy fighter will also want to
bring over some Copper Gloves.

Items that transfer in a special way to Wizardry VII must be equipped to make
the trip.  Only one such item can make the transfer per character.  If a
character has more than one such item equipped, one will be chosen at random;
in order to guarantee the transfer of such an item, equip the item you want to
transfer and nothing else.  Items so transferred will be the very last item of
a character's inventory in Wizardry VII.

These special items include:
* most other Tier 3 weapons sold by Mai-Lai.  This excludes Cupid Arrows, Bone
  Breakers, Razor Stones, and Serpent Stones.
* most other Tier 3 armor sold by Mai-Lai.  This excludes Full Plate (U) and
  Full Plate (L), but does include the Jazeraint Tunic and Jazeraint Skirt,
  which cannot be purchased in Wizardry VII.  (These are only slightly better
  than Studded Leather armor, however.)
* Anointed Cloak (sold by Mai-Lai)
* Shadow Cloak (Psionic starting item)
* Tier 4 weapons: Blades of Aesir, Diamond Eyes, Elven Bow, Estoc de Olivia,
  Excaliber, Fang (only obtainable in Wizardry VII by transfer), Faust Halberd
  (gets -3 Regeneration), Maenad's Lance, Muramasa Blade, Peacemaker arrows,
  Rammbus Staff (gets -1 Regeneration), Saint Bastard, Spear of Death (only
  obtainable in Wizardry VII by transfer), Sword of Hearts, The Avenger,
  Zatoichi Bo.
* Tier 4 armor: Armet, Ebony Heaume, Ebony Plate (U), Ebony Plate (L), Hi-
  Kane-Do (U), Hi-Kane-Do (L), Mantis Gloves, Mantis Boots, Robe of Enchant
  (U), Robe of Enchant (L).  These items in Wizardry VII don't have nearly as
  many resistances as their Wizardry VI counterparts, unfortunately.  The
  Chamail Doublet and Chamail Pants do not transfer, which is fine because
  Rangers can equip much better armor in Wizardry VII anyway.
* Tier 4 miscellaneous: Displacer Cloak, Forest Cape, Medicine Bag, Midnight
  Cloak.  The Wizardry VII Displacer Cloak has a finite number of charges; the
  Wizardry VII Forest Cape loses all of its resistances.

Because the Wizardry VII equivalents of Wizardry VI tier 4 armor lose most of
their resistances, I recommend transferring a weapon for every character.  This
includes as many Tier 4 weapons as you can manage.  You can fill in the gaps by
going to Mai-Lai, who carries the following Tier 3 weapons that are also good
to transfer: Bushido Blade, Cat'O Nine Tail, Holy Basher, Vulcan Hammer.

Each character will receive an appropriate low-power weapon upon transfer to
Wizardry VII, based on class (exception: Faeries will receive a Faerie Stick
regardless of class), but you will not otherwise receive the normal starting
equipment for your class if you aren't already carrying it in Wizardry VI.

The first character in your party will get a Journey Map Kit in the first
inventory slot.

Finally, gold does not transfer directly to Wizardry VII; you lose all of your
gold, then are given a fixed amount of gold that depends on which ending you
got in Wizardry VI.  You get 5000 gold for the ending in which you take the
Cosmic Forge.  You start with no gold if you did not complete Wizardry VI.  If
you want to transfer a lot of gold over, you can convert it into Resurrection
potions, which stack and freely transfer; you can then cash them in as the need
arises.

If you want to maximize potential for a transfer to Wizardry VII, you want to
have all characters at least at level 20, with all level 1-3 spells known and
all skills except Mythology increased to around 48.  Have everyone equip their
weapon of choice for transfer, sell off all the powerful armor, buy everyone
replacement armor that will transfer, then convert all remaining gold into
stackable consumables that are good in Wizardry VII: Resurrection potions (to
sell for the cash), Cherry Bombs, Stink Bombs, Barbed Arrows, and magic stix.
If you really want to get the best start in Wizardry VII, find both a Diamond
Eyes and a Zatoichi Bo (this will take a LONG time!) and transfer those along
with The Avenger, a Muramasa Blade, a Maenad's Lance, and one other powerful
weapon of your choice.

Even after you do this, the transfer is random enough that you may want to run
the routine several times to get a better start.  Mad God's utility will allow
you to disable the Wizardry VII introduction to greatly speed up this process.

### SECTION 6C - Acquiring extra Diamond Rings and a bonus Cameo Locket

This trick comes from the FAQs at: http://www.softwarespecialties.com/

The Diamond Ring and Cameo Locket are powerful accessories that are obtained in
the special endings, and transfer freely to Wizardry VII.

You cannot normally obtain more than one Diamond Ring, nor can you normally get
both a Diamond Ring and a Cameo Locket.  These restrictions can be circumvented
by exploiting the bug described in section 1D(3).

To get multiple Diamond Rings, fill every single slot except one (EXACTLY one)
in your inventory with items; it's useful to have multiple stacks of stackable
items for this.  One character will need to hold multiple junk items.  Approach
Rebecca as usual for this special ending, and tell her the magic words to get a
Diamond Ring, which will go to the single empty inventory slot.  Now that your
inventory is full, she will be unable to give you the quest key, and you will
force the game into NPC mode.  Give her exactly one item, and you will be able
to tell her the magic words again to get a second Diamond Ring.  Repeat until
you have all but one of the Diamond Rings you want.  Before getting the last
Diamond Ring, have one character give her at least 4 items in one go; you need
to give her 7 items at once if you want to get every single item possible.

To get a Cameo Locket after getting a Diamond Ring, completely fill up your
entire inventory.  Approach Bela as normal, and tell him that you do not want
to accompany him on his journey.  He will try to give you the exit key, but
will be unable to do so, forcing you into NPC mode.  Attack him from the NPC
screen.  Your characters will now need to go into their inventories in the
middle of combat to free at least three inventory slots so they can pick up the
three items dropped at the end of the combat.  This obviously also precludes
you from getting the special ending where you journey with Bela to Guardia.

### SECTION 6D - Using my party in Wizardry VII

I have made available my own Wizardry VI endgame save at the following URL:
http://www.rawbw.com/~ssjlee/games/WIZ6-D35.RAR

This is a save that is all set up for loading into Wizardry VII, so you don't
need to fiddle around with it in Wizardry VI first.  The name of the saved game
is SAVEGAME.DBS, which is the Wizardry VI default.  (Wizardry VII will default
to SAVEGAME.BCF.)  You will start outside the poppy field near New City, which
is the standard transfer starting location.

If you haven't played Wizardry VII before, you'll want to head straight into
the poppy field, which will take you very near both the starter dungeon and New
City.

This is a party with skills at the transfer maxima, statistics other Karma all
at least 18, all possible spells that can transfer learned for everyone, and
most of the best possible starting equipment, including both a Diamond Eyes and
a Zatoichi Bo.  In order to transfer the good weapons, everyone is a hybrid,
including a rather awkward Faerie Samurai; once you get your feet wet and gain
a few levels you will want to switch everyone's classes to something more
suitable to your tastes.

## Combat tips for certain monsters

This is a list of notable monsters, sorted primarily by when in the game they
can appear.

If everyone in your party has high Ninjutsu skill, you can have everyone hide
in the first round of combat.  Late in the game, you can have 5 characters with
high Ninjutsu hide, with the 6th character a heavy armor user with most of the
Tier 4 heavy armor; that character can then act as a tank to absorb most
opposing attacks.  You can avoid all physical attacks if you are fast enough,
and hiding also means you will evade most spells.  Some spells are nasty enough
that you don't want to give the monsters even this chance, though.

### Castle and Hazard Area:

* Fat Rat (boss): has 75% Paralysis and 75% Hypnosis resistance, so things like
  Sleep spells won't work all that well.  Stink Bomb and poison work much
  better.  (As a reminder, if you can't cast Stink Bomb, you can buy them from
  Queequeg.)

* Giant Serpent (boss): has 8d4+70 hit points, which is a lot for this early in
  the game.  As it has 95% Paralysis, 95% Hypnosis, and 95% Psionic resistance,
  you don't have much chance of disabling it.  Fire, Cold, Poison, and Acid
  magical attacks all work well; physical attacks work too but they will miss a
  lot this early in the game.

* Rotting Corpse: for this and most other zombies including bosses, Dispel
  Undead works well.  Against this specific undead, Fire also works well as
  they only have 15% Fire resistance and 4d5+8 hit points.

* Captain Matey (boss): has high resistances across the board, including 125%
  Hypnosis resistance.  He has only 25% Air resistance; try a Stink Bomb if
  he's giving you trouble.

* Hydra Plant (boss): has a mist attack that works like a Sleep spell, and a
  paralyzing melee attack.  8d3+40 hit points, and 125% Light, Paralysis, Air,
  Hypnosis, and Psionic resistance.  Other damage spells and physical attacks
  should work well enough.

### Giant Mountain, Dwarf Mines:

* Monstrous Bat: obnoxious to fight, as they have 8d5+60 hit points but give
  very little experience for how difficult they are.  Unfortunately, trying to
  run away often causes your party to fall from the mountain paths to its
  death.

* Acid Slime, Cold Slime: have elemental breath and strong resistances, but 0%
  Fire resistance and not that many hit points.  A combination of Fire spells
  and hacking and slashing will do them in.

* Floater: These guys have 125% resistance to everything except Death across
  the board, poison breath, and nasty spells.  However they only have 6d2+6 hit
  points, so they can be quickly hacked into pieces.

* Giant Ant, Forager, Vaspess: these big ants all have 125% Light and 125% Air
  resistances, plus some Hypnosis resistance, but 0% for all other resistances;
  group damage spells work well.  They can inflict Poison and a lot of physical
  damage.

* Giant Wyrm, White Wyrm: these can appear in big groups and can inflict mass
  Air and Cold damage, but unfortunately don't have any notable weaknesses;
  multiple groups of these are very dangerous as there isn't any good way of
  disabling or killing them quickly.

* Hill Giant, Miner Giant, Mountain Giant: these beefy melee monsters all have
  0% Light resistance; a low-power Blinding Flash spell will shut them down.

* Rubber Beast (boss): has a dangerous mass paralysis attack and high
  resistances, and 6d4+70 hit points.  Most vulnerable to physical attacks; has
  0% Death resistance, so critical attacks will work normally.

* Toll Troll (boss): No sense in paying the toll; just attack him.  Has good
  resistances, but low (25%) Light resistance, so Blinding Flash works well.
  Has 10d5+200 hit points, so he'll take a while to beat down.

* Demonic Hellcat (boss): strong resistances across the board; has a fire
  breath attack and can critically hit, but only 6d5+48 hit points.  Does NOT
  have low Cold resistance; simple physical attacks work better.

* Frytz Gryns and Klaus Gryns (boss): Frytz has 12d5+185 hit points and only
  (strong) physical attacks.  Klaus has only 8d6+64 hit points, but can cast
  spells, of which Blinding Flash is most notable.  Poison works well against
  them, as both have 35% Poison resistance as their weak point.

* Guardian of Rock (boss): totally immune to most spells, but has 0% Acid
  resistance, so Acid Splash and Acid Bomb work reliably.  Cast Missile Shield
  to thwart its boulder attacks.

### Amazulu Pyramid:

* Shamaness: spellcasting Amazuli that are much more dangerous than non-
  spellcasters.  Shamanesses cast from the Mage spellbook, and have 50%
  Hypnosis and 25% Magic resistance.  They have no other resistances and only
  5d3+15 hit points, so direct group damage spells work well.

* Priestess: spellcasting Amazuli that cast from the Priest spellbook; more of
  a threat than Shamanesses.  They have the same resistances as Shamanesses.

* Pharaoh of Phyre: Dispel Undead them all as soon as you can.  Also, cast Fire
  Shield in the first round if there are a lot of them; their 50% Lifeforce
  resistance is enough so that quite a few may survive Dispel Undead. Only has
  35% Fire resistance, incidentally.  Frequently drop Ankhs of Phyre, which
  provide good Fire resistance.

* Amen-Tut-Butt (boss): has 125% Death resistance, so Dispel Undead will not
  work.  Casts really nasty Fire spells including Firestorm, so equip all the
  Ankhs of Phyre you found before the fight, then throw up defenses immediately
  once the fight begins.  Only has 10d3+70 hit points, but comes with lots of
  friends.

* Amazulu Queen and Kuwali Kubona (NPCs): Take care not to upset them, and
  don't pick a fight with them until you're ready to move on from the Hall of
  the Dead, as Kuwali Kubona is a good source of spellbooks and potions.

* Mau-Mu-Mu (boss): Using Kuwali Kubona's Foot Powder will let you approach
  painlessly without having to cast Levitate.  Casts nasty Fire spells
  including Firestorm; put up appropriate defenses.  Totally immune to most
  spells, but has 0% Cold resistance; Deep Freeze is particularly effective.
  Has 6d6+120 hit points.

### River Styx, Tomb of the Damned, Swamplands, Hall of the Dead:

* Nightgaunt: If you have Astral Gate, you can use it on these spellcasting
  demons.  If you don't, they've got good but not high resistances across the
  board; Silence is also effective at preventing from harming you.  More
  annoying than lethal, but they can sometimes appear in huge numbers.

* Mino-Daemon (boss): has strong fire attacks including Firestorm; put up
  appropriate defenses.  8d8+80 hit points; lowest resistances are Cold (50%)
  and Acid (35%).

* Huge Spider, Tarantula: cast a lot of Web spells, but have bad resistances
  for monsters this late in the game, and can be easily disabled with magic.

* Skeleton, Skeleton Lord: Skeletons are not too dangerous, but Skeleton Lords
  can cast a variety of nasty Priest spells; they can be hard to tell apart,
  and Dispel Undead works well against them, so spam Dispel Undead whenever a
  large crowd shows up.  Skeleton Lords appear in groups that are a bit
  smaller, if you don't have enough people that can cast Dispel Undead.

* Spectre, Wraith: Don't just cast Dispel Undead, as not only it is not
  particularly reliable against these undead, they can cast very nasty spells.
  They're both quite vulnerable to Silence, so cast that as well.

* Zombie Guard: unlike earlier zombies, has a fairly high 65% Lifeforce
  resistance, so Dispel Undead will work but not all that reliably.  Low Fire
  (25%) and Acid (20%) resistance, if you want to attack with other spells.

* Bulli's Ghost (boss): magically attacks, notably with Iceball and Deep
  Freeze.  75% Lifeforce resistance and 50% Death resistance, so Dispel Undead
  can work but probably won't; only 25% Magic resistance, so Silence is likely
  to work.  Only has 11d4+44 hit points, so a direct beatdown may work faster.

* Eila's Ghost (boss): magically attacks, notably with Prismic Missile.  75%
  Lifeforce resistance and 25% Death resistance, so Dispel Undead can work but
  probably won't; only 25% Magic resistance, so Silence is likely to work.
  Only has 11d4+44 hit points, so a direct beatdown may work faster.

* Maro's Ghost (boss): magically attacks, notably with Silence and Deadly
  Poison.  75% Lifeforce resistance and 25% Death resistance, so Dispel Undead
  can work but probably won't; only 25% Magic resistance, so Silence is likely
  to work.  Only has 11d4+44 hit points, so a direct beatdown may work faster.

* Narci's Ghost (boss): its only spell is Lifesteal, which is very deadly at
  this stage in the game.  75% Lifeforce resistance and 25% Death resistance,
  so Dispel Undead can work but probably won't; only 25% Magic resistance, so
  Silence is likely to work.  Only has 11d4+44 hit points, so a direct beatdown
  may work faster.

* Giant Crab, King Crab: strong physically, and have 75% Paralysis, Air,
  Hypnosis, and Psionic resistance, but have only 25% Fire, Cold, Poison, and
  Lifeforce Resistance.  A good target for those instant death spells you don't
  use much.

* Man O' War: much more dangerous than the similar looking Jelly Fish; has a
  mass paralysis attack and a paralyzing poisoning melee attack that has a 5%
  Critical rate.  Has 10d4+50 hit points and strong magic resistances across
  the board, so it's best to focus all your physical power on them.

* Sea Serpent, Water Dragon: The lowest resistance for both of these tough
  water monsters is 25% Poison resistance.

* Siren: frequently uses a singing attack that can drive your whole party
  insane, which can quickly kill your entire party.  Only has 5d4+15 hit points
  and low (20% or less) resistance to Fire, Light, Cold, and Poison, so simple
  group damage spells work better than debuffs.  Take them out fast before they
  can sing.

* Siren Sorceress: Sirens that mostly choose to cast spells, with many deadly
  spells like Asphyxiation, Iceball, Psionic Blast, etc.  They have fewer hit
  points than regular
