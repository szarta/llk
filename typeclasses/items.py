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
from evennia.utils import create

from world.definitions.itemdefs import WeaponType
from world.definitions.itemdefs import MaterialType
from world.definitions.itemdefs import FillLevel
from world.definitions.itemdefs import WearLocation
from world.definitions.bodytype import BodyType

import typeclasses.auras as auras


class Item(DefaultObject):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.is_drinkable = False
        self.db.is_edible = False

        self.db.auras = []

        self.db.material = MaterialType.Unknown

        self.db.age = 0
        self.db.decay_rate = 0
        self.db.durability = 0

        # 10 cp = 1sp, copper to silver
        # 10 sp = 1gp, silver to gold
        # 10 gp = 1ep, gold to electrum
        # 10 ep = 1pp, electrum to platinum
        self.copper_value = 0

        self.db.desc = "This is an item."


class Ammunition(Item):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.ammunition_type = 0


class DryGoodsContainer(Item):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.contents = []
        self.db.max_items = 0
        self.db.lockable = False
        self.db.unlock_item = None


class HolyItem(Item):

    def at_object_creation(self):
        super().at_object_creation()

        aura = create.create_object(
            auras.PersistentEffectAura,
            key="Holy Aura",
            location=self,
            attributes=[
                ("desc", "A holy aura."),
                ("effect_modifiers", {auras.AuraEffect.TurnUnholy: 1})
            ]
        )

        self.db.auras.append(aura)


class LiquidContainer(Item):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.is_drinkable = True
        self.db.fill_level = FillLevel.Empty
        self.db.liquid_contents = "unknown liquid"

    def update_description(self):
        # TODO: we need to call this at some point after item creation...
        level = str(self.db.fill_level)
        if self.db.fill_level == FillLevel.Empty:
            level = "An {}".format(level)
        else:
            level = "A {}".format(level)

        self.db.desc = "{} {} of {}.".format(
            level,
            self.key,
            self.db.liquid_contents
        )


class WearableItem(Item):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.armor_value = 0

        self.db.possible_wear_locations = [
        ]

        self.db.current_worn_location = WearLocation.Inventory

        # note that armor find from fallen has 25% chance of being useless
        # demi-humans cannot wear armor sized for human
        # 75% chance discovered armor is human-sized, default to human
        self.db.target_body_type = BodyType.Normal

    def is_currently_worn(self):
        worn = (
            self.db.current_worn_location != WearLocation.Inventory
        )
        return worn


class Weapon(WearableItem):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.die_rolls = 1
        self.db.die_face = 2
        self.db.projectile_launcher = False
        self.db.throwable = False
        self.db.required_weapon_proficiency = WeaponType.Basic
        self.db.ammo_per_shot = 0
        self.db.matching_ammunition_types = []

        # 2 handed weapons have d16 on initiative checks
        self.db.two_handed = False

        # backstab weapons get bonuses
        self.db.backstab_weapon = False

        # weapons that require a mount to use
        self.db.requires_mount = False

        self.db.possible_wear_locations.append(
            WearLocation.Held
        )


class Blackjack(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Blackjack

        self.db.die_rolls = 1
        self.db.die_face = 3

        self.db.backstab_die_rolls = 2
        self.db.backstab_die_face = 6


class Blowgun(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Blowgun

        self.db.die_rolls = 1
        self.db.die_face = 3

        self.db.projectile_launcher = True

        self.db.backstab_die_rolls = 1
        self.db.backstab_die_face = 5


class Battleaxe(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Battleaxe

        self.db.die_rolls = 1
        self.db.die_face = 10
        self.db.two_handed = True

        self.db.possible_wear_locations.append(
            WearLocation.Back
        )


class ShortSword(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.ShortSword

        self.db.die_rolls = 1
        self.db.die_face = 6


class Longsword(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Longsword

        self.db.die_rolls = 1
        self.db.die_face = 8


class Axe(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Axe

        self.db.die_rolls = 1
        self.db.die_face = 6


class Club(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Club

        self.db.die_rolls = 1
        self.db.die_face = 4


class Crossbow(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Crossbow

        self.db.projectile_launcher = True

        self.db.die_rolls = 1
        self.db.die_face = 6


class Dagger(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Dagger

        self.db.die_rolls = 1
        self.db.die_face = 4

        self.db.backstab_die_rolls = 1
        self.db.backstab_die_face = 10

        self.db.throwable = True


class Staff(Weapon):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.die_rolls = 1
        self.db.die_face = 4
