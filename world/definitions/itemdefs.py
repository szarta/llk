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
from utils.enum import AutoNumberEnum


class WeaponType(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Improvised = "Improvised"

    Staff = "Staff"

    Club = "Club"
    Blackjack = "Blackjack"
    Mace = "Mace"
    Warhammer = "Warhammer"
    Flail = "Flail"

    Dagger = "Dagger"
    ShortSword = "Short sword"
    Longsword = "Longsword"
    TwoHandedSword = "Two-handed sword"

    Handaxe = "Handaxe"
    Axe = "Axe"
    Battleaxe = "Battleaxe"

    Dart = "Dart"
    Blowgun = "Blowgun"
    Sling = "Sling"
    Shortbow = "Shortbow"
    Crossbow = "Crossbow"
    Longbow = "Longbow"

    Spear = "Spear"
    Javelin = "Javelin"
    Lance = "Lance"
    Polearm = "Polearm"


class MaterialType(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Unknown = "Unknown"
    Linen = "Linen"
    Hemp = "Hemp"
    Ivory = "Ivory"
    Burlap = "Burlap"
    Silk = "Silk"
    Cotton = "Cotton"
    Lace = "Lace"
    Denim = "Denim"
    Wool = "Wool"
    Flannel = "Flannel"
    Fishnet = "Fishnet"
    Fur = "Fur"
    Hide = "Hide"
    ScrapLeather = "Scrap Leather"
    Leather = "Leather"
    StuddedLeather = "Studded Leather"
    Bronze = "Bronze"
    Iron = "Iron"
    Copper = "Copper"
    Silver = "Silver"
    Gold = "Gold"
    Glass = "Glass"
    Steel = "Steel"
    Obsidian = "Obsidian"
    Ruby = "Ruby"
    Stone = "Stone"
    Wax = "Wax"
    Wood = "Wood"
    ParchmentPaper = "Parchment Paper"
    Clay = "Clay"
    Mithril = "Mithril"


class WearLocation(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name
    Inventory = "Inventory"
    Head = "Head"
    Neck = "Neck"
    Shoulders = "Shoulders"
    Arms = "Arms"
    Hands = "Hands"
    Fingers = "Fingers"
    Waist = "Waist"
    Torso = "Torso"
    Legs = "Legs"
    Feet = "Feet"
    Body = "Body"
    Back = "Back"
    Held = "Held"


class FillLevel(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Empty = "Empty"
    NearlyEmpty = "Nearly Empty"
    HalfFull = "Half Full"
    NearlyFull = "Nearly Full"
    Full = "Full"
