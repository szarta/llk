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


HOLY_SYMBOL = {
    "typeclass": "typeclasses.items.HolyItem",
    "key": "holy symbol",
    "material": MaterialType.Ivory,
    "desc": "A holy symbol.",
    "possible_wear_locations": [
        WearLocation.Held
    ]
}

LANTERN = {
    "typeclass": "typeclasses.items.IgnitableLightSource",
    "key": "iron lantern",
    "material": MaterialType.Iron,
    "desc": "An iron lantern.",
    "light_type": LightGenerationType.AverageAmbientLight,
    "possible_wear_locations": [
        WearLocation.Held
    ]
}

CANDLE = {
    "typeclass": "typeclasses.items.IgnitableLightSource",
    "key": "wax candle",
    "material": MaterialType.Wax,
    "desc": "A wax candle.",
    "light_type": LightGenerationType.WeakAmbientLight,
    "possible_wear_locations": [
        WearLocation.Held
    ]
}

SHEET_OF_PARCHMENT_PAPER = {
    "typeclass": "typeclasses.items.Item",
    "key": "sheet of parchment paper",
    "material": MaterialType.ParchmentPaper,
    "desc": "A sheet of parchment paper."
}

TAROT_DECK = {
    "typeclass": "typeclasses.items.Item",
    "key": "deck of tarot cards",
    "desc": "A deck of tarot cards."
}

DICE = {
    "typeclass": "typeclasses.items.Item",
    "key": "set of dice",
    "desc": "A set of dice."
}

STEEL_TONGS = {
    "typeclass": "typeclasses.items.Item",
    "key": "set of steel tongs",
    "material": MaterialType.Steel,
    "desc": "A set of steel tongs.",
    "possible_wear_locations": [
        WearLocation.Held
    ]
}

HEMP_NET = {
    "typeclass": "typeclasses.items.Item",
    "key": "hemp net",
    "material": MaterialType.Hemp,
    "desc": "A hemp net.",
    "possible_wear_locations": [
        WearLocation.Held
    ]
}

SPYGLASS = {
    "typeclass": "typeclasses.items.Item",
    "key": "spyglass",
    "desc": "A spyglass.",
    "possible_wear_locations": [
        WearLocation.Held
    ]
}

