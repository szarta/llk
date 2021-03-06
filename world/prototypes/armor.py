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
from world.definitions.itemdefs import FillLevel
from world.definitions.itemdefs import MaterialType
from world.definitions.itemdefs import WearLocation
from world.definitions.light import LightGenerationType
from world.definitions.language import Language


HIDE_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "hide pants",
    "material": MaterialType.Hide,
    "desc": "A pair of hide pants.",
    "armor_value": 10,
    "possible_wear_locations": [
        WearLocation.Legs
    ]
}

LEATHER_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "leather pants",
    "material": MaterialType.Leather,
    "desc": "A pair of leather pants.",
    "armor_value": 20,
    "possible_wear_locations": [
        WearLocation.Legs
    ]
}

LARGE_HIDE_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "large hide cloak",
    "material": MaterialType.Hide,
    "desc": "A large hide cloak.",
    "armor_value": 10,
    "possible_wear_locations": [
        WearLocation.Back
    ]
}

LARGE_BROWN_HOODED_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "large brown hooded cloak",
    "desc": "A large brown hooded cloak.",
    "armor_value": 10,
    "possible_wear_locations": [
        WearLocation.Back
    ]
}

LARGE_BLACK_LEATHER_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "large black leather cloak",
    "material": MaterialType.Leather,
    "desc": "A large black leather cloak.",
    "armor_value": 20,
    "possible_wear_locations": [
        WearLocation.Back
    ]
}

LEATHER_BRACERS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "leather bracers",
    "material": MaterialType.Leather,
    "desc": "A leather bracers.",
    "armor_value": 20,
    "possible_wear_locations": [
        WearLocation.Arms
    ]
}

THICK_LEATHER_GLOVES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "thick leather gloves",
    "material": MaterialType.Leather,
    "desc": "A thick leather gloves.",
    "armor_value": 20,
    "possible_wear_locations": [
        WearLocation.Hands
    ]
}

LEATHER_TUNIC = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "leather tunic",
    "material": MaterialType.Leather,
    "desc": "A leather tunic.",
    "armor_value": 20,
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

LEATHER_BOOTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "leather boots",
    "material": MaterialType.Leather,
    "desc": "A leather boots.",
    "armor_value": 20,
    "possible_wear_locations": [
        WearLocation.Feet
    ]
}

IRON_COIF = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "iron coif",
    "material": MaterialType.Iron,
    "desc": "An iron coif.",
    "armor_value": 40,
    "possible_wear_locations": [
        WearLocation.Head
    ]
}

IRON_HELM = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "iron helm",
    "material": MaterialType.Iron,
    "desc": "An iron helm.",
    "armor_value": 40,
    "possible_wear_locations": [
        WearLocation.Head
    ]
}

