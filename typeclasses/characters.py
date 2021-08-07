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

import evennia
from evennia.utils import create
from evennia.contrib import gendersub

from world.definitions.chardefs import Language
from world.definitions.chardefs import OccupationTable
from world.definitions.chardefs import get_random_occupation
from world.definitions.chardefs import BirthAugur
from world.definitions.chardefs import BirthAugurAuraTable
from world.definitions.chardefs import Race
from world.definitions.chardefs import Alignment

import typeclasses.auras as auras


# PLACED IN THIS FILE UNTIL A BETTER SPOT FOUND

def roll_dice(num_dice, die_type):
    """
    3d6, for example, would be num_dice = 3, die_type = 6
    """
    result = 0
    for i in range(num_dice):
        result += random.randint(1, die_type)

    return result


def calculate_ability_modifier(ability_score):
    modifier = 0
    if ability_score <= 3:
        modifier = -3
    elif ability_score <= 5:
        modifier = -2
    elif ability_score <= 8:
        modifier = -1
    elif ability_score <= 12:
        modifier = 0
    elif ability_score <= 15:
        modifier = 1
    elif ability_score <= 17:
        modifier = 2
    elif ability_score > 17:
        modifier = 3

    return modifier

# PLACED IN THIS FILE UNTIL A BETTER SPOT FOUND


class Character(gendersub.GenderCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods
    with the following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every
                    move.
    at_post_unpuppet(account) -  when Account disconnects from the Character,
                    we store the current location in the pre_logout_location
                    Attribute and move it to a None-location so the
                    "unpuppeted" character object does not need to stay on
                    grid. Echoes "Account has disconnected" to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    def get_modified_hp(self):
        stam = self.get_modified_stamina()
        modifier = calculate_ability_modifier(stam)

        for aura in self.db.auras:
            if auras.AuraEffect.HP in aura.db.effect_modifiers.keys():
                modifier += aura.db.effect_modifiers[auras.AuraEffect.HP]

        return (self.db.hp + modifier)

    def get_modified_strength(self):
        modifier = 0

        for aura in self.db.auras:
            if auras.AuraEffect.Strength in aura.db.effect_modifiers.keys():
                modifier += aura.db.effect_modifiers[auras.AuraEffect.Strength]

        return (self.db.strength + modifier)

    def get_modified_agility(self):
        modifier = 0

        for aura in self.db.auras:
            if auras.AuraEffect.Agility in aura.db.effect_modifiers.keys():
                modifier += aura.db.effect_modifiers[auras.AuraEffect.Agility]

        return (self.db.agility + modifier)

    def get_modified_stamina(self):
        modifier = 0

        for aura in self.db.auras:
            if auras.AuraEffect.Stamina in aura.db.effect_modifiers.keys():
                modifier += aura.db.effect_modifiers[auras.AuraEffect.Stamina]

        return (self.db.stamina + modifier)

    def get_modified_personality(self):
        modifier = 0

        for a in self.db.auras:
            if auras.AuraEffect.Personality in a.db.effect_modifiers.keys():
                modifier += a.db.effect_modifiers[auras.AuraEffect.Personality]

        return (self.db.personality + modifier)

    def get_modified_intelligence(self):
        modifier = 0

        for a in self.db.auras:
            if auras.AuraEffect.Intelligence in a.db.effect_modifiers.keys():
                modifier += \
                    a.db.effect_modifiers[auras.AuraEffect.Intelligence]

        return (self.db.intelligence + modifier)

    def get_modified_luck(self):
        modifier = 0

        for aura in self.db.auras:
            if auras.AuraEffect.Luck in aura.db.effect_modifiers.keys():
                modifier += aura.db.effect_modifiers[auras.AuraEffect.Luck]

        return (self.db.luck + modifier)

    def get_modified_speed(self):
        modifier = 0

        for aura in self.db.auras:
            if auras.AuraEffect.Speed in aura.db.effect_modifiers.keys():
                modifier += aura.db.effect_modifiers[auras.AuraEffect.Speed]

        return (self.db.speed + modifier)

    def get_modified_ac(self):
        agi = self.get_modified_agility()
        modifier = calculate_ability_modifier(agi)
        for aura in self.db.auras:
            if auras.AuraEffect.AC in aura.db.effect_modifiers.keys():
                modifier += aura.db.effect_modifiers[auras.AuraEffect.AC]

        return (self.db.ac + modifier)

    def set_birth_augur_effect(self):
        if self.db.birth_augur not in BirthAugurAuraTable:
            return

        luck_modifier = calculate_ability_modifier(self.db.luck)
        augur_data = BirthAugurAuraTable[self.db.birth_augur]
        if "effects" in augur_data and luck_modifier != 0:
            aura_effects = {}
            for m in augur_data["effects"]:
                if "modifier_multiplier" in augur_data:
                    aura_effects[m] = \
                        luck_modifier * augur_data["modifier_multiplier"]
                else:
                    aura_effects[m] = luck_modifier

            aura = create.create_object(
                auras.PersistentEffectAura,
                key=augur_data["name"],
                location=self,
                attributes=[
                    ("desc", augur_data["desc"]),
                    ("effect_modifiers", aura_effects)
                ]
            )
            aura.build_modifier_description()
            self.db.auras.append(aura)

    def at_object_creation(self):
        super().at_object_creation()

        self.db.level = 0
        self.db.ac = 0
        self.db.xp = 0
        self.db.alignment = Alignment.Neutral  # TODO: alignment selection

        # these are base stats before any modifiers or active effects
        self.db.strength = roll_dice(3, 6)
        self.db.agility = roll_dice(3, 6)
        self.db.stamina = roll_dice(3, 6)
        self.db.personality = roll_dice(3, 6)
        self.db.intelligence = roll_dice(3, 6)
        self.db.luck = roll_dice(3, 6)
        self.db.hp = roll_dice(1, 4)
        self.db.speed = 30

        self.db.auras = []

        self.db.birth_augur = random.choice(list(BirthAugur))
        self.set_birth_augur_effect()

        self.db.known_languages = []
        self.db.known_languages.append(Language.Common)

        self.db.weapon_proficiencies = []

        self.db.gold = 0
        self.db.silver = 0
        self.db.copper = roll_dice(5, 12)

        self.db.occupation = get_random_occupation()
        occupation = self.db.occupation
        if "weapon_proficiencies" in OccupationTable[occupation]:
            self.db.weapon_proficiencies.append(
                OccupationTable[occupation]["weapon_proficiencies"]
            )

        for item in OccupationTable[occupation]["items"]:
            item_clone = dict(item)
            item_clone["location"] = self
            evennia.prototypes.spawner.spawn(item_clone)

        if "race" in OccupationTable[occupation]:
            self.db.race = OccupationTable[occupation]["race"]
        else:
            self.db.race = Race.Human

        if self.db.race == Race.Dwarf or self.db.race == Race.Halfling:
            self.db.speed = 20

        if self.db.race == Race.Human:
            self.db.age = random.randint(18, 45)
        elif self.db.race == Race.Dwarf:
            self.db.age = random.randint(37, 75)
        elif self.db.race == Race.Elf:
            self.db.age = random.randint(35, 100)
        elif self.db.race == Race.Halfling:
            self.db.age = random.randint(20, 55)

        if "money" in OccupationTable[occupation]:
            money_data = OccupationTable[occupation]["money"]
            if "gold" in money_data:
                self.db.gold += money_data["gold"]
            if "silver" in money_data:
                self.db.silver += money_data["silver"]
            if "copper" in money_data:
                self.db.copper += money_data["copper"]

        if self.db.intelligence >= 8:
            if self.db.race == Race.Dwarf:
                self.db.known_languages.append(Language.Dwarf)
            elif self.db.race == Race.Elf:
                self.db.known_languages.append(Language.Elf)
            elif self.db.race == Race.Halfling:
                self.db.known_languages.append(Language.Halfling)

        self.db.current_hp = self.get_modified_hp()
