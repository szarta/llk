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
from world.definitions.itemdefs import MaterialType

ROLL_OF_LINEN = {
    "typeclass": "typeclasses.items.Item",
    "key": "linen roll",
    "desc": "A roll of linen (one yard).",
    "material": MaterialType.Linen,
}

CLUMP_OF_MITHRIL = {
    "typeclass": "typeclasses.items.Item",
    "key": "clump mithril",
    "desc": "A clump of mithril (one ounce).",
    "material": MaterialType.Mithril,
}

STACK_OF_WOOD = {
    "typeclass": "typeclasses.items.Item",
    "key": "stacked wood",
    "desc": "A stack of wood (ten pounds).",
    "material": MaterialType.Wood,
}

BURLAP_SACK = {
    "typeclass": "typeclasses.items.Item",
    "key": "sack",
    "material": MaterialType.Burlap,
}

BAG_OF_FINE_DIRT = {
    "typeclass": "typeclasses.items.Item",
    "key": "bag of fine dirt",
    "desc": "A bag of fine dirt (one pound)."
}

BAG_OF_FINE_STONE = {
    "typeclass": "typeclasses.items.Item",
    "key": "bag of fine stone",
    "desc": "A bag of fine stone (ten pounds)."
}

BAG_OF_CLAY = {
    "typeclass": "typeclasses.items.Item",
    "key": "bag of clay",
    "desc": "A bag of clay (one pound)."
}

BOOK_OF_RPG_SECRETS = {
    "typeclass": "typeclasses.items.Item",
    "key": "book of rpg secrets",
    "desc": "A book of rpg secrets.",
    "copper_value": 50
}

BOOK_OF_LEGAL_OPINIONS = {
    "typeclass": "typeclasses.items.Item",
    "key": "book of legal opinions",
    "desc": "A book of legal opinions.",
    "copper_value": 200
}

SHOEHORN = {
    "typeclass": "typeclasses.items.Item",
    "key": "shoehorn",
    "material": MaterialType.Steel,
}

GIANT_RUBY_GEM = {
    "typeclass": "typeclasses.items.Item",
    "key": "giant gem",
    "material": MaterialType.Ruby,
    "copper_value": 200
}
