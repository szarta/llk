# from enum import Enum


# contains a lot of overlap with languages, but will likely grow over time
class Race:
    racelist = ('', 'Human', 'Dwarf', 'Elf', 'Halfling', 'Gnome', 'Bugbear',
        'Goblin', 'Gnoll', 'Harpy', 'Hobgoblin', 'Kobold', 'Lizardman',
        'Minotaur', 'Ogre', 'Orc', 'Serpentman', 'Troglodyte', 'Angel',
        'Centaur', 'Demon', 'Doppelganger', 'Dragon', 'Pixie', 'Giant',
        'Griffon', 'Naga', 'Bear', 'Eagle', 'Ferret', 'Horse', 'Wolf',
        'Spider')

    def __init__(self,  name):
       self.name = self.racelist[name]

    def __str__(self):
        return str(self.name)
