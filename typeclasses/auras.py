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
from evennia import DefaultObject


class PersistentEffectAura(DefaultObject):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.hidden = False
        self.db.known_effects = True
        self.db.effect_modifiers = {}
        self.db.modifier_description = "+0 stam"
        self.db.understandable_description = "You know this aura."
        self.db.indecipherable_description = "Gives a faint glow."

        self.db.desc = "This is an aura."

    def build_modifier_description(self):
        modifier_description = ""
        for k in self.db.effect_modifiers.keys():
            effect_desc = k.short_desc()
            modifier = self.db.effect_modifiers[k]
            sign = "-"
            if modifier >= 0:
                sign = "+"
            modifier = abs(modifier)

            modifier_description = \
                f'{modifier_description}, {effect_desc} {sign}{modifier}'

        self.db.modifier_description = \
            modifier_description.lstrip(",").lstrip()
