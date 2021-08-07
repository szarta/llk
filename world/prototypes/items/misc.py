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


ROLL_OF_LINEN = {
    "typeclass": "typeclasses.items.Item",
    "key": "linen roll",
    "desc": "A roll of linen (one yard)."
}

CLUMP_OF_MITHRIL = {
    "typeclass": "typeclasses.items.Item",
    "key": "clump mithril",
    "desc": "A clump of mithril (one ounce)."
}

STACK_OF_WOOD = {
    "typeclass": "typeclasses.items.Item",
    "key": "stacked wood",
    "desc": "A stack of wood (ten pounds)."
}

BAG_OF_FINE_DIRT = {
    "typeclass": "typeclasses.items.Item",
    "key": "bag of fine dirt",
    "desc": "A bag of fine dirt (one pound)."
}

BOOK_OF_RPG_SECRETS = {
    "typeclass": "typeclasses.items.Item",
    "key": "book of rpg secrets",
    "desc": "A book of rpg secrets.",
    "copper_value": 50
}

HOLY_SYMBOL = {
    "typeclass": "typeclasses.items.HolyItem",
    "key": "holy symbol",
    "desc": "A holy symbol.",
    "possible_wear_locations": [WearLocation.Held]
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

GIANT_RUBY_GEM = {
    "typeclass": "typeclasses.items.Item",
    "key": "giant ruby gem",
    "desc": "A giant ruby gem.",
    "copper_value": 200
}

STEEL_TONGS = {
    "typeclass": "typeclasses.items.Item",
    "key": "steel tongs",
    "desc": "A pair of steel tongs.",
}
