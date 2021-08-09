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
from evennia import DefaultRoom
from evennia import CmdSet
from evennia import Command


class ExistentialPlaneCmdSet(CmdSet):
    """
    Used to restrict commands while on the Existential Plane (starting area)
    """
    key = "existential_cmdset"
    priority = 1
    mergetype = "Remove"

    def at_cmdset_creation(self):
        commands_to_remove = [
            "sheet",
            "modifiers"
        ]

        for cmd in commands_to_remove:
            self.add(Command(key=cmd))


class ExistentialPlane(DefaultRoom):
    """
    Rooms in the starting area, prior to player puppeting of a "true" in-game
    character.
    """
    def at_object_creation(self):
        self.cmdset.add(ExistentialPlaneCmdSet)


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    pass
