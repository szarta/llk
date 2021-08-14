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


class Language(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Common = "Common"
    Thieves = "Thieves' Cant"
    Chaos = "Chaos"
    Law = "Law"
    Neutrality = "Neutrality"
    Dwarf = "Dwarf"
    Elf = "Elf"
    Halfling = "Halfling"
    Gnome = "Gnome"
    Bugbear = "Bugbear"
    Goblin = "Goblin"
    Gnoll = "Gnoll"
    Harpy = "Harpy"
    Hobgoblin = "Hobgoblin"
    Kobold = "Kobold"
    Lizardman = "Lizardman"
    Minotaur = "Minotaur"
    Ogre = "Ogre"
    Orc = "Orc"
    Serpentman = "Serpentman"
    Troglodyte = "Troglodyte"
    Angelic = "Angelic"
    Centaur = "Centaur"
    Demonic = "Demonic"
    Doppelganger = "Doppleganger"
    Dragon = "Dragon"
    Pixie = "Pixie"
    Giant = "Giant"
    Griffon = "Griffon"
    Naga = "Naga"
    Bear = "Bear"
    Eagle = "Eagle"
    Ferret = "Ferret"
    Horse = "Horse"
    Wolf = "Wolf"
    Spider = "Spider"
    Undercommon = "Undercommon"
