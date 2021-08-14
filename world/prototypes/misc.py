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


ROLL_OF_LINEN = {
    "typeclass": "typeclasses.items.Item",
    "key": "linen roll",
    "material": MaterialType.Linen,
    "desc": "A roll of linen(one yard)."
}

CLUMP_OF_MITHRIL = {
    "typeclass": "typeclasses.items.Item",
    "key": "mithril clump",
    "material": MaterialType.Mithril,
    "desc": "A clump of mithril (one ounce)."
}

STACK_OF_WOOD = {
    "typeclass": "typeclasses.items.Item",
    "key": "stack of wood",
    "material": MaterialType.Wood,
    "desc": "A stack of wood (ten pounds)."
}

SACK_OF_NIGHTSOIL = {
    "typeclass": "typeclasses.items.Item",
    "key": "sack of nightsoil",
    "desc": "A sack of nightsoil."
}

BAG_OF_FINE_DIRT = {
    "typeclass": "typeclasses.items.Item",
    "key": "bag of fine dirt",
    "desc": "A bag of fine dirt (one pound)."
}

BAG_OF_FINE_STONE = {
    "typeclass": "typeclasses.items.Item",
    "key": "bag of fine stone",
    "desc": "A bag of fine dirt (ten pounds)."
}

BAG_OF_HERBS = {
    "typeclass": "typeclasses.items.Item",
    "key": "bag of herbs",
    "desc": "A bag of herbs (one pound)."
}

BAG_OF_CLAY = {
    "typeclass": "typeclasses.items.Item",
    "key": "bag of clay",
    "desc": "A bag of clay (one pound)."
}

BOOK_OF_RPG_SECRETS = {
    "typeclass": "typeclasses.items.Book",
    "key": "dusty tome",
    "desc": "A dusty tome.",
    "copper_value": 50,
    "language": Language.Dragon
}

BOOK_OF_LEGAL_OPINIONS = {
    "typeclass": "typeclasses.items.Book",
    "key": "thick leather-bound book",
    "desc": "A thick leather-bound book.",
    "copper_value": 200,
    "language": Language.Elf
}

SHOEHORN = {
    "typeclass": "typeclasses.items.Item",
    "key": "steel shoehorn",
    "material": MaterialType.Steel,
    "desc": "A steel shoehorn."
}

GLASS_BEADS = {
    "typeclass": "typeclasses.items.Item",
    "key": "glass beads",
    "material": MaterialType.Glass,
    "desc": "A glass beads."
}

GIANT_RUBY_GEM = {
    "typeclass": "typeclasses.items.Item",
    "key": "giant ruby gem",
    "material": MaterialType.Ruby,
    "desc": "A giant ruby gem.",
    "copper_value": 200
}

