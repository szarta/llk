"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
import random
import evennia
from enum import Enum

from evennia.utils import create
from evennia.contrib import gendersub
from world.languages import Language
from world.occupations import Occupation
from world.occupations import OccupationTable
import typeclasses.auras as auras
from world.birthaugur import BirthAugur
from world.birthaugur import BirthAugurTable
from world.races import Race

from world.weapons import WeaponType


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


class Alignment(Enum):
    Lawful = 0
    Neutral = 1
    Chaotic = 2

    def __str__(self):
        if self == Alignment.Lawful:
            return "Lawful"
        elif self == Alignment.Neutral:
            return "Neutral"
        elif self == Alignment.Chaotic:
            return "Chaotic"
        else:
            return "unknown"


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
    def at_object_creation(self):
        super().at_object_creation()

        self.db.level = 0
        self.db.ac = 0
        self.db.xp = 0
        self.db.age = 0  # TODO: figure this out, random?  races?
        self.db.alignment = Alignment.Neutral  # TODO: alignment selection

        self.db.strength = roll_dice(3, 6)
        self.db.agility = roll_dice(3, 6)
        self.db.stamina = roll_dice(3, 6)
        self.db.personality = roll_dice(3, 6)
        self.db.intelligence = roll_dice(3, 6)
        self.db.luck = roll_dice(3, 6)
        self.db.base_speed = 30

        self.db.birth_augur = BirthAugur(roll_dice(1, 30))

        luck_modifier = calculate_ability_modifier(self.db.luck)
        self.db.auras = []

        augur_data = BirthAugurTable[str(self.db.birth_augur)]
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

        self.db.known_languages = []
        self.db.known_languages.append(Language.Common)

        self.db.weapon_proficiencies = []
        self.db.weapon_proficiencies.append(WeaponType.Basic)

        self.db.gold = 0
        self.db.silver = 0
        self.db.copper = roll_dice(5, 12)

        self.db.base_hp = roll_dice(1, 4)
        self.db.max_hp = self.db.base_hp + calculate_ability_modifier(
            self.db.stamina
        )

        self.db.current_hp = self.db.max_hp

        self.db.occupation = Occupation(roll_dice(1, 100))
        occupation = str(self.db.occupation)
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
            self.db.base_speed = 20

        if self.db.intelligence >= 8:
            if self.db.race == Race.Dwarf:
                self.db.known_languages.append(Language.Dwarf)
            elif self.db.race == Race.Elf:
                self.db.known_languages.append(Language.Elf)
            elif self.db.race == Race.Halfling:
                self.db.known_languages.append(Language.Halfling)
