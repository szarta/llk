"""
Prototypes

A prototype is a simple way to create individualized instances of a
given typeclass. It is dictionary with specific key names.

For example, you might have a Sword typeclass that implements everything a
Sword would need to do. The only difference between different individual Swords
would be their key, description and some Attributes. The Prototype system
allows to create a range of such Swords with only minor variations. Prototypes
can also inherit and combine together to form entire hierarchies (such as
giving all Sabres and all Broadswords some common properties). Note that bigger
variations, such as custom commands or functionality belong in a hierarchy of
typeclasses instead.

A prototype can either be a dictionary placed into a global variable in a
python module (a 'module-prototype') or stored in the database as a dict on a
special Script (a db-prototype). The former can be created just by adding dicts
to modules Evennia looks at for prototypes, the latter is easiest created
in-game via the `olc` command/menu.

Prototypes are read and used to create new objects with the `spawn` command
or directly via `evennia.spawn` or the full path `evennia.prototypes.spawner.spawn`.

A prototype dictionary have the following keywords:

Possible keywords are:
- `prototype_key` - the name of the prototype. This is required for db-prototypes,
  for module-prototypes, the global variable name of the dict is used instead
- `prototype_parent` - string pointing to parent prototype if any. Prototype inherits
  in a similar way as classes, with children overriding values in their partents.
- `key` - string, the main object identifier.
- `typeclass` - string, if not set, will use `settings.BASE_OBJECT_TYPECLASS`.
- `location` - this should be a valid object or #dbref.
- `home` - valid object or #dbref.
- `destination` - only valid for exits (object or #dbref).
- `permissions` - string or list of permission strings.
- `locks` - a lock-string to use for the spawned object.
- `aliases` - string or list of strings.
- `attrs` - Attributes, expressed as a list of tuples on the form `(attrname, value)`,
  `(attrname, value, category)`, or `(attrname, value, category, locks)`. If using one
   of the shorter forms, defaults are used for the rest.
- `tags` - Tags, as a list of tuples `(tag,)`, `(tag, category)` or `(tag, category, data)`.
-  Any other keywords are interpreted as Attributes with no category or lock.
   These will internally be added to `attrs` (eqivalent to `(attrname, value)`.

See the `spawn` command and `evennia.prototypes.spawner.spawn` for more info.

"""
from typeclasses.items import WearLocation
from typeclasses.items import FillLevel


APRON = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "apron",
    "desc": "A brown leather apron.",
    "possible_wear_locations": [WearLocation.Body]
}

PURPLE_CEREMONIAL_OVERCOAT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple ceremonial overcoat",
    "desc": "A purple ceremonial overcoat.",
    "possible_wear_locations": [WearLocation.Body]
}

BLACK_SILK_TIGHTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black silk tights",
    "desc": "A pair of black silk tights.",
    "possible_wear_locations": [WearLocation.Legs]
}

HOLY_SYMBOL = {
    "typeclass": "typeclasses.items.HolyItem",
    "key": "holy symbol",
    "desc": "A holy symbol.",
    "possible_wear_locations": [WearLocation.Held]
}

ORANGE_COTTON_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "orange cotton shirt",
    "desc": "An orange cotton shirt.",
    "possible_wear_locations": [WearLocation.Torso]
}


RED_SILK_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "red silk shirt",
    "desc": "A red short-sleeved silk shirt.",
    "possible_wear_locations": [WearLocation.Torso]
}

WHITE_LINEN_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white linen shirt",
    "desc": "A white long-sleeved linen shirt.",
    "possible_wear_locations": [WearLocation.Torso]
}

BLACK_CANVAS_SHOES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black canvas shoes",
    "desc": "A well-worn pair of black-dyed hemp canvas shoes.",
    "possible_wear_locations": [WearLocation.Feet]
}

MIXED_HIDE_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "mixed-hide pants",
    "desc": "A pair of mixed-hide pants.",
    "possible_wear_locations": [WearLocation.Legs]
}

LARGE_HIDE_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "large hide cloak",
    "desc": "A large cloak made of animal hides.",
    "possible_wear_locations": [WearLocation.Back]
}

GREEN_FEATHERED_CAP = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "green feathered cap",
    "desc": "A green feathered cap.",
    "possible_wear_locations": [WearLocation.Head]
}

YELLOW_SUSPENDERS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "yellow suspenders",
    "desc": "A set of yellow suspenders.",
    "possible_wear_locations": [WearLocation.Shoulders]
}

BLUE_COTTON_JEANS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "blue cotton jeans",
    "desc": "A pair of blue cotton jeans.",
    "possible_wear_locations": [WearLocation.Legs]
}

LARGE_BROWN_HOODED_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "large brown hooded cloak",
    "desc": "A large brown hooded cloak.",
    "possible_wear_locations": [WearLocation.Back]
}

SILK_SASH_BELT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "silk sash belt",
    "desc": "A silk sash belt.",
    "possible_wear_locations": [WearLocation.Waist]
}

ROPE_BELT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "rope belt",
    "desc": "A belt made of rope.",
    "possible_wear_locations": [WearLocation.Waist]
}

BLACK_LEATHER_BELT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black leather belt",
    "desc": "A black leather belt.",
    "possible_wear_locations": [WearLocation.Waist]
}

MONOCLE = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "monocle",
    "desc": "A monocle.",
    "possible_wear_locations": [WearLocation.Head]
}

PURPLE_STARRY_ROBE = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple star robe",
    "desc": "A purple robe with yellow stars on it.",
    "possible_wear_locations": [WearLocation.Body]
}

THICK_LEATHER_GLOVES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "thick leather gloves",
    "desc": "A set of thick leather gloves.",
    "possible_wear_locations": [WearLocation.Hands]
}

LEATHER_TUNIC = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "leather tunic",
    "desc": "A leather tunic.",
    "possible_wear_locations": [WearLocation.Torso]
}

LEATHER_BOOTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "leather boots",
    "desc": "A set of leather boots.",
    "possible_wear_locations": [WearLocation.Feet]
}

WHITE_COTTON_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white cotton shirt",
    "desc": "A white cotton shirt.",
    "possible_wear_locations": [WearLocation.Torso]
}



LEATHER_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "leather pants",
    "desc": "A set of leather pants.",
    "possible_wear_locations": [WearLocation.Legs]
}

IRON_HELMET = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "iron helmet",
    "desc": "An iron helmet.",
    "armor_modifier": 1,
    "possible_wear_locations": [WearLocation.Head]
}

LARGE_BLACK_LEATHER_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "large black leather cloak",
    "desc": "A large black leather cloak.",
    "possible_wear_locations": [WearLocation.Back]
}

SPYGLASS = {
    "typeclass": "typeclasses.items.Item",
    "key": "spyglass",
    "desc": "A spyglass.",
}

SHOEHORN = {
    "typeclass": "typeclasses.items.Item",
    "key": "shoehorn",
    "desc": "A shoehorn.",
}

ORNATE_GOLD_RING = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "ornate gold ring",
    "desc": "An ornate gold ring.",
    "possible_wear_locations": [WearLocation.Fingers],
    "copper_value": 100
}

GIANT_RUBY_GEM = {
    "typeclass": "typeclasses.items.Item",
    "key": "giant ruby gem",
    "desc": "A giant ruby gem.",
    "copper_value": 200
}

GRAY_LINEN_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "gray linen pants",
    "desc": "A pair of gray linen pants shoes.",
    "possible_wear_locations": [WearLocation.Legs]
}

WOODEN_STAFF = {
    "typeclass": "typeclasses.items.Staff",
    "key": "wooden staff",
    "desc": "A simple wooden staff."
}

WOODEN_STORAGE_BARREL = {
    "typeclass": "typeclasses.items.DryGoodsContainer",
    "key": "wooden storage barrel",
    "desc": "A wooden storage barrel.",
    "max_items": 16
}

DRIED_ASSORTED_FRUIT = {
    "typeclass": "typeclasses.items.Item",
    "key": "dried assorted fruit",
    "desc": "A handful of dried assorted fruit.",
    "is_edible": True
}

SIDE_OF_BEEF = {
    "typeclass": "typeclasses.items.Item",
    "key": "side of beef",
    "desc": "A side of beef.",
    "is_edible": True
}

STINKY_CHEESE = {
    "typeclass": "typeclasses.items.Item",
    "key": "quarter wheel stinky cheese",
    "desc": "A quarter wheel of stinky cheese.",
    "is_edible": True
}

STEEL_TONGS = {
    "typeclass": "typeclasses.items.Item",
    "key": "steel tongs",
    "desc": "A pair of steel tongs.",
}

JAR_OF_HONEY = {
    "typeclass": "typeclasses.items.LiquidContainer",
    "key": "clay jar",
    "desc": "A clay jar.",
    "fill_level": FillLevel.Full,
    "liquid_contents": "honey"
}

FLASK_OF_OIL = {
    "typeclass": "typeclasses.items.LiquidContainer",
    "key": "flask",
    "desc": "A simple flask.",
    "fill_level": FillLevel.Full,
    "liquid_contents": "oil"
}

WOODEN_CLUB = {
    "typeclass": "typeclasses.items.Club",
    "key": "wooden club",
    "desc": "A simple wooden club."
}

BALL_PEEN_HAMMER = {
    "typeclass": "typeclasses.items.Club",
    "key": "ball-peen hammer",
    "desc": "A ball-peen hammer."
}

IRON_CROWBAR = {
    "typeclass": "typeclasses.items.Club",
    "key": "iron crowbar",
    "desc": "An iron crowbar."
}

IRON_LONG_SWORD = {
    "typeclass": "typeclasses.items.Longsword",
    "key": "iron longsword",
    "desc": "An iron longsword."
}

SHOVEL = {
    "typeclass": "typeclasses.items.Staff",
    "key": "shovel",
    "desc": "A shovel with a wooden handle and iron spade."
}

SMALL_IRON_DAGGER = {
    "typeclass": "typeclasses.items.Dagger",
    "key": "small iron dagger",
    "desc": "A small iron dagger."
}

IRON_PARING_KNIFE = {
    "typeclass": "typeclasses.items.Dagger",
    "key": "iron paring knife",
    "desc": "An iron paring knife."
}

SCISSORS = {
    "typeclass": "typeclasses.items.Dagger",
    "key": "scissors",
    "desc": "A pair of scissors."
}

IRON_SHORT_SWORD = {
    "typeclass": "typeclasses.items.ShortSword",
    "key": "iron short sword",
    "desc": "An iron short sword."
}

FOLDING_STRAIGHT_EDGE_RAZOR = {
    "typeclass": "typeclasses.items.Dagger",
    "key": "folding straight-edge razor",
    "desc": "A folding straight-edge razor."
}

SHARP_STITCHING_AWL = {
    "typeclass": "typeclasses.items.Dagger",
    "key": "sharp stitching awl",
    "desc": "A sharp stitching awl."
}

WOODEN_CUDGEL = {
    "typeclass": "typeclasses.items.Staff",
    "key": "wooden cudgel",
    "desc": "A wooden cudgel."
}

SHARP_IRON_CLEAVER = {
    "typeclass": "typeclasses.items.Axe",
    "key": "sharp iron cleaver",
    "desc": "A sharp iron cleaver."
}


## example of module-based prototypes using
## the variable name as `prototype_key` and
## simple Attributes

# from random import randint
#
# GOBLIN = {
# "key": "goblin grunt",
# "health": lambda: randint(20,30),
# "resists": ["cold", "poison"],
# "attacks": ["fists"],
# "weaknesses": ["fire", "light"],
# "tags": = [("greenskin", "monster"), ("humanoid", "monster")]
# }
#
# GOBLIN_WIZARD = {
# "prototype_parent": "GOBLIN",
# "key": "goblin wizard",
# "spells": ["fire ball", "lighting bolt"]
# }
#
# GOBLIN_ARCHER = {
# "prototype_parent": "GOBLIN",
# "key": "goblin archer",
# "attacks": ["short bow"]
# }
#
# This is an example of a prototype without a prototype
# (nor key) of its own, so it should normally only be
# used as a mix-in, as in the example of the goblin
# archwizard below.
# ARCHWIZARD_MIXIN = {
# "attacks": ["archwizard staff"],
# "spells": ["greater fire ball", "greater lighting"]
# }
#
# GOBLIN_ARCHWIZARD = {
# "key": "goblin archwizard",
# "prototype_parent" : ("GOBLIN_WIZARD", "ARCHWIZARD_MIXIN")
# }
