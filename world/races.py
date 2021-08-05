from enum import Enum


# contains a lot of overlap with languages, but will likely grow over time
class Race(Enum):
    Human = 1
    Dwarf = 2
    Elf = 3
    Halfling = 4
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
    Angel = 22
    Centaur = 23
    Demon = 24
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

    def __str__(self):
        if self == Race.Human:
            return "Human"
        elif self == Race.Dwarf:
            return "Dwarf"
        elif self == Race.Elf:
            return "Elf"
        elif self == Race.Halfling:
            return "Halfling"
        else:
            return "todo"
