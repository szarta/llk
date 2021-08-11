#
# This is a batchcode file, used by Evennia's batch code processor to generate
# rooms, exits, items, and npcs within the MUD.
#
# It gets run (within the game) with:
#
#     @batchcode path.to.file
#
#########################
# The Existential Plane #
#########################
#
# This is the character selection zone of the MUD.
#

#HEADER
import random
from evennia import create_object, search_object
from typeclasses.objects import Object

if caller.ndb.all_rooms is None:
    caller.ndb.all_rooms = {}

#CODE

room_1 = create_object("rooms.ExistentialPlane", key="The Existential Plane")
room_1.db.desc = """
You (or the incorporeal manifestation of your |bself|n) stands (or rather,
floats, or exists, whatever) on the cliffs of a rock surrounded on all
sides by what looks like a brilliant backdrop of |bstars|n, |bnebulae|n, and
all sorts of other astronomical objects that typically inspire awe in people.

But you are also not exactly people, so you (clearly) have other more pressing
matters to attend to.
"""
room_1.db.details["stars"] = "OooOo stars."
room_1.db.details["nebulae"] = """
The plural of nebula. I looked it up, trust me.
"""
