from evennia import DefaultObject
from enum import Enum
from world.weapons import WeaponType


class WearLocation(Enum):
    Inventory = 2
    Head = 3
    Neck = 4
    Shoulders = 5
    Arms = 6
    Hands = 7
    Fingers = 8
    Waist = 9
    Torso = 10
    Legs = 11
    Feet = 12
    Body = 13
    Back = 14
    Held = 15

    def __str__(self):
        if self == WearLocation.Head:
            return "head"
        elif self == WearLocation.Neck:
            return "neck"
        elif self == WearLocation.Shoulders:
            return "shoulders"
        elif self == WearLocation.Arms:
            return "arms"
        elif self == WearLocation.Hands:
            return "hands"
        elif self == WearLocation.Fingers:
            return "finger"
        elif self == WearLocation.Waist:
            return "waist"
        elif self == WearLocation.Torso:
            return "torso"
        elif self == WearLocation.Legs:
            return "legs"
        elif self == WearLocation.Feet:
            return "feet"
        elif self == WearLocation.Body:
            return "body"
        elif self == WearLocation.Back:
            return "back"
        elif self == WearLocation.Held:
            return "holding"
        else:
            return ""


class FillLevel(Enum):
    Empty = 0
    NearlyEmpty = 1
    HalfFull = 2
    NearlyFull = 3
    Full = 4

    def __str__(self):
        if self == FillLevel.Empty:
            return "empty"
        elif self == FillLevel.NearlyEmpty:
            return "nearly empty"
        elif self == FillLevel.HalfFull:
            return "half full"
        elif self == FillLevel.NearlyFull:
            return "nearly full"
        elif self == FillLevel.Full:
            return "full"


class Item(DefaultObject):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.is_drinkable = False
        self.db.is_edible = False

        self.db.auras = []

        self.db.age = 0
        self.db.decay_rate = 0
        self.db.durability = 0

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

        self.db.armor_modifier = 0

        self.db.possible_wear_locations = [
        ]

        self.db.current_worn_location = WearLocation.Inventory

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
        self.db.two_handed = False

        self.db.backstab_die_rolls = 2
        self.db.backstab_die_face = 6


class Blowgun(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Blowgun

        self.db.die_rolls = 1
        self.db.die_face = 3
        self.db.two_handed = False
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


class Club(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Club

        self.db.die_rolls = 1
        self.db.die_face = 4
        self.db.two_handed = False


class Crossbow(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Crossbow

        self.db.projectile_launcher = True

        self.db.die_rolls = 1
        self.db.die_face = 6
        self.db.two_handed = False


class Dagger(Weapon):

    def at_object_creation(self):
        super().at_object_creation()
        self.db.required_weapon_proficiency = WeaponType.Dagger

        self.db.die_rolls = 1
        self.db.die_face = 4
        self.db.two_handed = False

        self.db.backstab_die_rolls = 1
        self.db.backstab_die_face = 10

        self.db.throwable = True


class Staff(Weapon):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.die_rolls = 1
        self.db.die_face = 4
        self.db.two_handed = False
