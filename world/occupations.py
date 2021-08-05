from enum import Enum
from evennia.utils import create
import typeclasses.items as items
from typeclasses.items import FillLevel
from typeclasses.items import WearLocation
from world.weapons import WeaponType


class Occupation(Enum):
    Alchemist = 1
    AnimalTrainer = 2
    Armorer = 3
    Astrologer = 4
    Barber = 5
    Beadle = 6
    Beekeeper = 7
    Blacksmith = 8
    Butcher = 9
    CaravanGuard = 10
    Cheesemaker = 11
    Cobbler = 12
    ConfidenceArtist = 13
    Cooper = 14
    Costermonger = 15
    Cutpurse = 16
    DitchDigger = 17
    DockWorker = 18
    DwarvenApothecarist = 19
    DwarvenBlacksmith = 20
    DwarvenChestMaker = 21
    DwarvenHerder = 22
    DwarvenMiner = 23
    DwarvenMinerTwo = 24
    DwarvenMushroomFarmer = 25
    DwarvenRatCatcher = 26
    DwarvenStonemason = 27
    DwarvenStonemasonTwo = 28
    ElvenArtisan = 29
    ElvenBarrister = 30
    ElvenChandler = 31
    ElvenFalconer = 32
    ElvenForester = 33
    ElvenForesterTwo = 34
    ElvenGlassblower = 35
    ElvenNavigator = 36
    ElvenSage = 37
    ElvenSageTwo = 38
    Farmer = 39
    FarmerTwo = 40
    FarmerThree = 41
    FarmerFour = 42
    FarmerFive = 43
    FarmerSix = 44
    FarmerSeven = 45
    FarmerEight = 46
    FarmerNine = 47
    FortuneTeller = 48
    Gambler = 49
    Gongfarmer = 50
    Gravedigger = 51
    GravediggerTwo = 52
    GuildBeggar = 53
    GuildBeggarTwo = 54
    HalflingChickenButcher = 55
    HalflingDyer = 56
    HalflingDyerTwo = 57
    HalflingGloveMaker = 58
    HalflingGypsy = 59
    HalflingHaberdasher = 60
    HalflingMariner = 61
    HalflingMoneylender = 62
    HalflingTrader = 63
    HalflingVagrant = 64
    Healer = 65
    Herbalist = 66
    Herder = 67
    Hunter = 68
    HunterTwo = 69
    IndenturedServant = 70
    Jester = 71
    Jewler = 72
    Locksmith = 73
    Mendicant = 74
    Mercenary = 75
    Merchant = 76
    Baker = 77
    Minstrel = 78
    Noble = 79
    Orphan = 80
    Ostler = 81
    Outlaw = 82
    RopeMaker = 83
    Scribe = 84
    Shaman = 85
    Slave = 86
    Smuggler = 87
    Soldier = 88
    Squire = 89
    SquireTwo = 90
    TaxCollector = 91
    Trapper = 92
    TrapperTwo = 93
    Urchin = 94
    Wainwright = 95
    Weaver = 96
    WizardsApprentice = 97
    Woodcutter = 98
    WoodcutterTwo = 99
    WoodcutterThree = 100

    def __str__(self):
        if self == Occupation.Alchemist:
            return "Alchemist"
        elif self == Occupation.AnimalTrainer:
            return "Animal trainer"
        elif self == Occupation.Armorer:
            return "Armorer"
        elif self == Occupation.Astrologer:
            return "Astrologer"
        else:
            return "No string yet."


def fill_initial_occupation_benefits(target_character, occupation):
    if occupation == Occupation.Alchemist:
        create.create_object(
            items.WearableItem,
            key="smock",
            location=target_character,
            attributes=[
                ("desc", "A brown leather smock."),
                ("current_worn_location", WearLocation.Body),
                ("possible_wear_locations", [
                    WearLocation.Body
                ])
            ]
        )

        create.create_object(
            items.WearableItem,
            key="linen shirt",
            location=target_character,
            attributes=[
                ("desc", "A white long-sleeved linen shirt."),
                ("current_worn_location", WearLocation.Torso),
                ("possible_wear_locations", [
                    WearLocation.Torso
                ])
            ]
        )

        create.create_object(
            items.WearableItem,
            key="black canvas shoes",
            location=target_character,
            attributes=[
                ("desc", "A well-worn pair of black-dyed hemp canvas shoes."),
                ("current_worn_location", WearLocation.Feet),
                ("possible_wear_locations", [
                    WearLocation.Feet
                ])
            ]
        )

        create.create_object(
            items.WearableItem,
            key="linen pants",
            location=target_character,
            attributes=[
                ("desc", "A pair of gray linen pants."),
                ("current_worn_location", WearLocation.Legs),
                ("possible_wear_locations", [
                    WearLocation.Legs
                ])
            ]
        )

        create.create_object(
            items.Staff,
            key="staff",
            location=target_character,
            attributes=[
                ("desc", "A simple wooden staff.")
            ]
        )

        # TODO: likely put a script that makes it dangerous to drink
        flask = create.create_object(
            items.LiquidContainer,
            key="flask",
            location=target_character,
            attributes=[
                ("liquid_contents", "oil"),
                ("fill_level", FillLevel.Full)
            ]
        )
        flask.update_description()

        target_character.db.weapon_proficiencies.append(WeaponType.Staff)

    elif occupation == Occupation.AnimalTrainer:
        create.create_object(
            items.Club,
            key="club",
            location=target_character,
            attributes=[
                ("desc", "A simple wooden club.")
            ]
        )

        # TODO: make a pony??
        target_character.db.weapon_proficiencies.append(WeaponType.Club)

    elif occupation == Occupation.Armorer:
        create.create_object(
            items.Club,
            key="hammer",
            location=target_character,
            attributes=[
                ("desc", "A flat-edged blacksmith hammer.")
            ]
        )

        create.create_object(
            items.WearableItem,
            key="iron helmet",
            location=target_character,
            attributes=[
                ("current_worn_location", WearLocation.Head),
                ("armor_modifier", 1),
                ("possible_wear_locations", [
                    WearLocation.Head
                ])
            ]
        )

        target_character.db.weapon_proficiencies.append(WeaponType.Club)

    elif occupation == Occupation.Astologer:
        create.create_object(
            items.Dagger,
            key="dagger",
            location=target_character
        )

        create.create_object(
            items.Item,
            key="spyglass",
            location=target_character
        )

        target_character.db.weapon_proficiencies.append(WeaponType.Dagger)
