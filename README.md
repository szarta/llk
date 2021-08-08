# Legacy of the Lightkeepers (llk) #

This is the source code for the rules and objects of a MUD (Multi-User Dungeon)
called Legacy of the Lightkeepers.  The MUD is written in Python using as its
base the [Evennia](https://www.evennia.com/) game engine.  The rules and
mechanics are driven by the rules described for an RPG tabletop system called 
[DCC](https://goodman-games.com/store/), or Dungeon Crawl Classics.
Modifications have been made to help streamline faster-paced, mostly solo 
online play.

In general, the goal of the project is to supplement our core-group's tabletop
storytelling experience within our RPG world, by allowing individual players to
build backstories and initial starting experiences for characters through a
persistent online world.

To the extent that the code can help others learn either Python or how to work
within the Evennia system, it is provided here.  I welcome any feedback.

# Setup #

The primary engine of the game is run by Evennia, a Python-based MUD/MUX/MUSH
game engine/system.  It provides the core handling for networking and
authentication, as well as the infrastructure for the game loop, DB-storage 
and basic starting commands.

You can run this source locally by first following the instructions of 
[Evennia Quick Start](https://www.evennia.com/docs/latest/Getting-Started.html).

Then, you can replace the init-ed shell of a game with this source.
