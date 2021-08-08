"""
MIT License

Copyright (c) 2021 Brandon Arrendondo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from world.definitions.itemdefs import WearLocation
from world.definitions.itemdefs import MaterialType


#########
# Torso #
#########

ORANGE_COTTON_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "orange shirt",
    "material": MaterialType.Cotton,
    "possible_wear_locations": [WearLocation.Torso]
}

WHITE_COTTON_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white shirt",
    "material": MaterialType.Cotton,
    "possible_wear_locations": [WearLocation.Torso]
}

WHITE_SILK_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white shirt",
    "material": MaterialType.Silk,
    "possible_wear_locations": [WearLocation.Torso]
}

RED_SILK_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "red shirt",
    "material": MaterialType.Silk,
    "possible_wear_locations": [WearLocation.Torso]
}

PURPLE_SILK_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple shirt",
    "material": MaterialType.Silk,
    "possible_wear_locations": [WearLocation.Torso]
}

CHECKERED_FLANNEL_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "checkered shirt",
    "material": MaterialType.Flannel,
    "possible_wear_locations": [WearLocation.Torso]
}

WHITE_LINEN_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white shirt",
    "material": MaterialType.Linen,
    "possible_wear_locations": [WearLocation.Torso]
}

BROWN_LINEN_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "brown shirt",
    "material": MaterialType.Linen,
    "possible_wear_locations": [WearLocation.Torso]
}

STITCHED_HEMP_VEST = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "stitched vest",
    "material": MaterialType.Hemp,
    "possible_wear_locations": [WearLocation.Torso]
}

########
# Legs #
########

GRAY_LINEN_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "gray pants",
    "material": MaterialType.Linen,
    "possible_wear_locations": [WearLocation.Legs]
}

FINE_BLACK_SLACKS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "fine black slacks",
    "material": MaterialType.Cotton,
    "possible_wear_locations": [WearLocation.Legs]
}

BLACK_LINEN_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black pants",
    "material": MaterialType.Linen,
    "possible_wear_locations": [WearLocation.Legs]
}

BLUE_DENIM_JEANS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "blue jeans",
    "material": MaterialType.Denim,
    "possible_wear_locations": [WearLocation.Legs]
}

BLACK_SILK_TIGHTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black tights",
    "material": MaterialType.Silk,
    "possible_wear_locations": [WearLocation.Legs]
}

#########
# Waist #
#########

SILK_SASH_BELT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "sash belt",
    "material": MaterialType.Silk,
    "possible_wear_locations": [WearLocation.Waist]
}

ROPE_BELT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "rope belt",
    "material": MaterialType.Hemp,
    "possible_wear_locations": [WearLocation.Waist]
}

BLACK_LEATHER_BELT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black belt",
    "material": MaterialType.Leather,
    "possible_wear_locations": [WearLocation.Waist]
}

########
# Feet #
########

BLACK_CANVAS_SHOES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black canvas shoes",
    "material": MaterialType.Hemp,
    "possible_wear_locations": [WearLocation.Feet]
}

FINE_BLACK_LEATHER_SHOES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "fine black shoes",
    "material": MaterialType.Leather,
    "possible_wear_locations": [WearLocation.Feet]
}

########
# Head #
########

SAILORS_CAP = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "sailor's cap",
    "material": MaterialType.Wool,
    "possible_wear_locations": [WearLocation.Head]
}

PURPLE_SILK_HEADSCARF = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple headscarf",
    "material": MaterialType.Silk,
    "possible_wear_locations": [WearLocation.Head]
}

GREEN_FEATHERED_CAP = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "green feathered cap",
    "material": MaterialType.Wool,
    "possible_wear_locations": [WearLocation.Head]
}

BROWN_WOOL_CAP = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "brown cap",
    "material": MaterialType.Wool,
    "possible_wear_locations": [WearLocation.Head]
}

SPECTACLES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "spectacles",
    "material": MaterialType.Glass,
    "possible_wear_locations": [WearLocation.Head]
}

MONOCLE = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "monocle",
    "material": MaterialType.Glass,
    "possible_wear_locations": [WearLocation.Head]
}


###########
# Fingers #
###########

ORNATE_GOLD_RING = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "ornate gold ring",
    "material": MaterialType.Gold,
    "possible_wear_locations": [WearLocation.Fingers],
    "copper_value": 100
}

#########
# Robes #
#########

PURPLE_STARRY_ROBE = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple star robe",
    "desc": "A purple robe with yellow stars on it.",
    "material": MaterialType.Silk,
    "possible_wear_locations": [WearLocation.Body]
}

GRAY_LINEN_ROBE = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "gray robe",
    "material": MaterialType.Linen,
    "possible_wear_locations": [WearLocation.Body]
}

#########
# Misc  #
#########

BLUE_HOODED_WOOL_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "blue hooded cloak",
    "material": MaterialType.Wool,
    "possible_wear_locations": [WearLocation.Back]
}

BLACK_AND_RED_COTTON_SHEMAGH = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black and red shemagh",
    "material": MaterialType.Cotton,
    "possible_wear_locations": [WearLocation.Neck]
}

WHITE_COTTON_APRON = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white apron",
    "material": MaterialType.Cotton,
    "possible_wear_locations": [WearLocation.Body]
}

BROWN_LEATHER_APRON = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "brown apron",
    "material": MaterialType.Leather,
    "possible_wear_locations": [WearLocation.Body]
}

PURPLE_CEREMONIAL_OVERCOAT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple ceremonial overcoat",
    "material": MaterialType.Wool,
    "possible_wear_locations": [WearLocation.Body]
}

YELLOW_SUSPENDERS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "yellow suspenders",
    "desc": "A set of yellow suspenders.",
    "possible_wear_locations": [WearLocation.Shoulders]
}
