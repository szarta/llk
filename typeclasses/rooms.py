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
import random
from evennia import DefaultRoom
from evennia import CmdSet
from evennia import Command

# evennia.utils.utils.wrap(text, width=None, indent=0)


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    def at_object_creation(self):
        self.db.details = {}

    def return_detail(self, key):
        detail = None
        lower_key = key.lower()
        print(lower_key)
        if lower_key in self.db.details:
            detail = self.db.details[lower_key]

        return detail

    def return_appearance(self, looker, **kwargs):
        """
        This is called when e.g. the look command wants to retrieve
        the description of this object.

        Args:
            looker (Object): The object looking at us.
            **kwargs (dict): Arbitrary, optional arguments for users
                overriding the call (unused by default).

        Returns:
            description (str): Our description.

        """
        # ensures that our description is current based on time/season
        self.update_current_description()
        # run the normal return_appearance method, now that desc is updated.
        return super(Room, self).return_appearance(looker, **kwargs)

    def update_current_description(self):
        # this could be later used for season-based updates, or random room
        # changes, etc.
        pass


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


class ExistentialPlane(Room):
    """
    Rooms in the starting area, prior to player puppeting of a "true" in-game
    character.
    """
    def at_object_creation(self):
        super().at_object_creation()

        self.cmdset.add(ExistentialPlaneCmdSet)

    def update_current_description(self):
        if "stars" in self.db.details:
            self.db.details["stars"] = random.choice([
                "When you see stars that's all they are.",
                "When you look at the stars, you feel like yourself.",
                "When you find out what went on, you'll bring it back.",
                "You're out back counting stars.",
                "The stars will all come out, you'll turn and come back down.",
                "It's far - beyond the stars."
            ])
