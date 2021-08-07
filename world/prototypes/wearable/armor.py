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
from typeclasses.items import WearLocation
from typeclasses.items import MaterialType


########
# Legs #
########

HIDE_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "pants",
    "armor_value": 10,
    "material": MaterialType.Hide,
    "possible_wear_locations": [WearLocation.Legs]
}

LEATHER_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "pants",
    "armor_value": 20,
    "material": MaterialType.Leather,
    "possible_wear_locations": [WearLocation.Legs]
}


########
# Back #
########

LARGE_HIDE_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "large cloak",
    "armor_value": 10,
    "material": MaterialType.Hide,
    "possible_wear_locations": [WearLocation.Back]
}

LARGE_BROWN_HOODED_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "large brown hooded cloak",
    "armor_value": 10,
    "possible_wear_locations": [WearLocation.Back]
}

LARGE_BLACK_LEATHER_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "large black cloak",
    "armor_value": 20,
    "material": MaterialType.Leather,
    "possible_wear_locations": [WearLocation.Back]
}


#########
# Hands #
#########

THICK_LEATHER_GLOVES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "thick gloves",
    "armor_value": 20,
    "material": MaterialType.Leather,
    "possible_wear_locations": [WearLocation.Hands]
}

#########
# Torso #
#########

LEATHER_TUNIC = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "tunic",
    "armor_value": 20,
    "material": MaterialType.Leather,
    "possible_wear_locations": [WearLocation.Torso]
}

########
# Feet #
########

LEATHER_BOOTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "boots",
    "armor_value": 20,
    "material": MaterialType.Leather,
    "possible_wear_locations": [WearLocation.Feet]
}

########
# Head #
########

IRON_COIF = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "coif",
    "armor_value ": 40,
    "material": MaterialType.Iron,
    "possible_wear_locations": [WearLocation.Head]
}
