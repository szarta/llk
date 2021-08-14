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


ORANGE_COTTON_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "orange cotton shirt",
    "material": MaterialType.Cotton,
    "desc": "An orange cotton shirt.",
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

WHITE_COTTON_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white cotton shirt",
    "material": MaterialType.Cotton,
    "desc": "A white cotton shirt.",
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

WHITE_SILK_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white silk shirt",
    "material": MaterialType.Silk,
    "desc": "A white silk shirt.",
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

RED_SILK_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "red silk shirt",
    "material": MaterialType.Silk,
    "desc": "A red silk shirt.",
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

PURPLE_SILK_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple silk shirt",
    "material": MaterialType.Silk,
    "desc": "A purple silk shirt.",
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

WHITE_LINEN_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white linen shirt",
    "material": MaterialType.Linen,
    "desc": "A white linen shirt.",
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

BROWN_LINEN_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "brown linen shirt",
    "material": MaterialType.Linen,
    "desc": "A brown linen shirt.",
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

CHECKERED_FLANNEL_SHIRT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "checkered flannel shirt",
    "material": MaterialType.Flannel,
    "desc": "A checkered flannel shirt.",
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

STITCHED_HEMP_VEST = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "stitched hemp vest",
    "material": MaterialType.Hemp,
    "desc": "A stitched hemp vest.",
    "possible_wear_locations": [
        WearLocation.Torso
    ]
}

GRAY_LINEN_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "gray linen pants",
    "material": MaterialType.Linen,
    "desc": "A pair of gray linen pants.",
    "possible_wear_locations": [
        WearLocation.Legs
    ]
}

BLACK_LINEN_PANTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black linen pants",
    "material": MaterialType.Linen,
    "desc": "A pair of black linen pants.",
    "possible_wear_locations": [
        WearLocation.Legs
    ]
}

BLACK_SILK_TIGHTS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black silk tights",
    "material": MaterialType.Silk,
    "desc": "A pair of black silk tights.",
    "possible_wear_locations": [
        WearLocation.Legs
    ]
}

FINE_BLACK_SLACKS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "fine black slacks",
    "material": MaterialType.Cotton,
    "desc": "A pair of fine black slacks.",
    "possible_wear_locations": [
        WearLocation.Legs
    ]
}

BLUE_DENIM_JEANS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "blue cotton jeans",
    "material": MaterialType.Cotton,
    "desc": "A pair of blue cotton jeans.",
    "possible_wear_locations": [
        WearLocation.Legs
    ]
}

SILK_SASH_BELT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "silk sash belt",
    "material": MaterialType.Silk,
    "desc": "A silk sash belt.",
    "possible_wear_locations": [
        WearLocation.Waist
    ]
}

ROPE_BELT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "hemp rope belt",
    "material": MaterialType.Hemp,
    "desc": "A hemp rope belt.",
    "possible_wear_locations": [
        WearLocation.Waist
    ]
}

BLACK_LEATHER_BELT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black leather belt",
    "material": MaterialType.Leather,
    "desc": "A black leather belt.",
    "possible_wear_locations": [
        WearLocation.Waist
    ]
}

BLACK_CANVAS_SHOES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black canvas shoes",
    "material": MaterialType.Hemp,
    "desc": "A black canvas shoes.",
    "possible_wear_locations": [
        WearLocation.Feet
    ]
}

FINE_BLACK_LEATHER_SHOES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "fine black leather shoes",
    "material": MaterialType.Leather,
    "desc": "A fine black leather shoes.",
    "possible_wear_locations": [
        WearLocation.Feet
    ]
}

SAILORS_CAP = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "wool sailor's cap",
    "material": MaterialType.Wool,
    "desc": "A wool sailor's cap.",
    "possible_wear_locations": [
        WearLocation.Head
    ]
}

PURPLE_SILK_HEADSCARF = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple silk headscarf",
    "material": MaterialType.Silk,
    "desc": "A purple silk headscarf.",
    "possible_wear_locations": [
        WearLocation.Head
    ]
}

GREEN_FEATHERED_CAP = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "green feathered cap",
    "material": MaterialType.Wool,
    "desc": "A green feathered cap.",
    "possible_wear_locations": [
        WearLocation.Head
    ]
}

BROWN_WOOL_CAP = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "brown wool cap",
    "material": MaterialType.Wool,
    "desc": "A brown wool cap.",
    "possible_wear_locations": [
        WearLocation.Head
    ]
}

SPECTACLES = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "spectacles",
    "material": MaterialType.Glass,
    "desc": "A spectacles.",
    "possible_wear_locations": [
        WearLocation.Head
    ]
}

MONOCLE = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "monocle",
    "material": MaterialType.Glass,
    "desc": "A monocle.",
    "possible_wear_locations": [
        WearLocation.Head
    ]
}

ORNATE_GOLD_RING = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "ornate gold ring",
    "material": MaterialType.Gold,
    "desc": "An ornate gold ring.",
    "copper_value": 100,
    "possible_wear_locations": [
        WearLocation.Fingers
    ]
}

PURPLE_STARRY_ROBE = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple star robe",
    "material": MaterialType.Silk,
    "desc": "A purple robe with yellow stars on it.",
    "possible_wear_locations": [
        WearLocation.Body
    ]
}

GRAY_LINEN_ROBE = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "gray linen robe",
    "material": MaterialType.Linen,
    "desc": "A gray linen robe.",
    "possible_wear_locations": [
        WearLocation.Body
    ]
}

BLUE_HOODED_WOOL_CLOAK = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "blue hooded wool cloak",
    "material": MaterialType.Wool,
    "desc": "A blue hooded wool cloak.",
    "possible_wear_locations": [
        WearLocation.Back
    ]
}

BLACK_AND_RED_COTTON_SHEMAGH = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "black and red cotton shemagh",
    "material": MaterialType.Cotton,
    "desc": "A black and red cotton shemagh.",
    "possible_wear_locations": [
        WearLocation.Neck
    ]
}

WHITE_COTTON_APRON = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "white cotton apron",
    "material": MaterialType.Cotton,
    "desc": "A white cotton apron.",
    "possible_wear_locations": [
        WearLocation.Body
    ]
}

BROWN_LEATHER_APRON = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "brown leather apron",
    "material": MaterialType.Leather,
    "desc": "A brown leather apron.",
    "possible_wear_locations": [
        WearLocation.Body
    ]
}

PURPLE_CEREMONIAL_OVERCOAT = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "purple ceremonial overcoat",
    "material": MaterialType.Wool,
    "desc": "A purple ceremonial overcoat.",
    "possible_wear_locations": [
        WearLocation.Body
    ]
}

YELLOW_SUSPENDERS = {
    "typeclass": "typeclasses.items.WearableItem",
    "key": "yellow suspenders",
    "desc": "A set of yellow suspenders.",
    "possible_wear_locations": [
        WearLocation.Shoulders
    ]
}

