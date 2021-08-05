from enum import Enum


class Language(Enum):
    Common = 1
    Thieves = 2
    Chaos = 3
    Law = 4
    Neutrality = 5
    Dwarf = 6
    Elf = 7
    Halfling = 8
    Gnome = 9
    Bugbear = 10
    Goblin = 11
    Gnoll = 12
    Harpy = 13
    Hobgoblin = 14
    Kobold = 15
    Lizardman = 16
    Minotaur = 17
    Ogre = 18
    Orc = 19
    Serpentman = 20
    Troglodyte = 21
    Angelic = 22
    Centaur = 23
    Demonic = 24
    Doppelganger = 25
    Dragon = 26
    Pixie = 27
    Giant = 28
    Griffon = 29
    Naga = 30
    Bear = 31
    Eagle = 32
    Ferret = 33
    Horse = 34
    Wolf = 35
    Spider = 36
    Undercommon = 37

    def __str__(self):
        if self == Language.Common:
            return "Common"
        elif self == Language.Thieves:
            return "Thieves' Cant"
        elif self == Language.Chaos:
            return "Chaos"
        elif self == Language.Law:
            return "Law"
        elif self == Language.Neutrality:
            return "Neutrality"
        elif self == Language.Dwarf:
            return "Dwarf"
        elif self == Language.Elf:
            return "Elf"
        elif self == Language.Halfling:
            return "Halfling"
        elif self == Language.Gnome:
            return "Gnome"
        elif self == Language.Bugbear:
            return "Bugbear"
        elif self == Language.Goblin:
            return "Goblin"
        elif self == Language.Gnoll:
            return "Gnoll"
        elif self == Language.Harpy:
            return "Harpy"
        elif self == Language.Hobgoblin:
            return "Hobgoblin"
        elif self == Language.Kobold:
            return "Kobold"
        elif self == Language.Lizardman:
            return "Lizardman"
        elif self == Language.Minotaur:
            return "Minotaur"
        elif self == Language.Ogre:
            return "Ogre"
        elif self == Language.Orc:
            return "Orc"
        elif self == Language.Serpentman:
            return "Serpentman"
        elif self == Language.Troglodyte:
            return "Troglodyte"
        elif self == Language.Angelic:
            return "Angelic"
        else:
            return "Unknown"
