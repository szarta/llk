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
from typeclasses.items import MaterialType


########
# Wood #
########

WOODEN_STAFF = {
    "typeclass": "typeclasses.items.Staff",
    "key": "staff",
    "material": MaterialType.Wood
}

POLE = {
    "typeclass": "typeclasses.items.Staff",
    "key": "pole",
    "material": MaterialType.Wood
}

WOODEN_CLUB = {
    "typeclass": "typeclasses.items.Club",
    "key": "club",
    "material": MaterialType.Wood
}

WOODEN_CUDGEL = {
    "typeclass": "typeclasses.items.Staff",
    "key": "cudgel",
    "material": MaterialType.Wood
}

########
# Iron #
########

SHARP_IRON_CLEAVER = {
    "typeclass": "typeclasses.items.Axe",
    "key": "sharp cleaver",
    "material": MaterialType.Iron
}

IRON_CROWBAR = {
    "typeclass": "typeclasses.items.Club",
    "key": "crowbar",
    "material": MaterialType.Iron
}

IRON_CHISEL = {
    "typeclass": "typeclasses.items.Dagger",
    "key": "chisel",
    "material": MaterialType.Iron
}

IRON_LONG_SWORD = {
    "typeclass": "typeclasses.items.Longsword",
    "key": "longsword",
    "material": MaterialType.Iron
}

IRON_MINING_PICK = {
    "typeclass": "typeclasses.items.Club",
    "key": "mining pick",
    "material": MaterialType.Iron
}

SHOVEL = {
    "typeclass": "typeclasses.items.Staff",
    "key": "shovel",
    "material": MaterialType.Iron,
    "desc": "A shovel with a wooden handle and iron spade."
}

SMALL_IRON_DAGGER = {
    "typeclass": "typeclasses.items.Dagger",
    "key": "small dagger",
    "material": MaterialType.Iron
}

IRON_PARING_KNIFE = {
    "typeclass": "typeclasses.items.Dagger",
    "key": "paring knife",
    "material": MaterialType.Iron
}

IRON_SHORT_SWORD = {
    "typeclass": "typeclasses.items.ShortSword",
    "key": "short sword",
    "material": MaterialType.Iron
}

#########################
# Non-descript material #
#########################

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

BALL_PEEN_HAMMER = {
    "typeclass": "typeclasses.items.Club",
    "key": "ball-peen hammer",
    "desc": "A ball-peen hammer."
}

SCISSORS = {
    "typeclass": "typeclasses.items.Dagger",
    "key": "scissors",
    "desc": "A pair of scissors."
}
