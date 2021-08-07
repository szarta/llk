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
