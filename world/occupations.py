from enum import Enum
from evennia.utils import create
import typeclasses.items as items
from world.weapons import WeaponType
import world.prototypes as prototypes


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


OccupationTable = {
    str(Occupation.Alchemist): {
        "name": "Alchemist",
        "items": [
            prototypes.WOODEN_STAFF,
            prototypes.FLASK_OF_OIL,
            prototypes.SMOCK,
            prototypes.WHITE_LINEN_SHIRT,
            prototypes.BLACK_CANVAS_SHOES,
            prototypes.GRAY_LINEN_PANTS
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.AnimalTrainer): {
        "name": "Animal Trainer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Armorer): {
        "name": "Armorer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Astrologer): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Barber): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Beadle): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Beekeeper): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Blacksmith): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Butcher): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.CaravanGuard): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Cheesemaker): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Cobbler): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ConfidenceArtist): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Cooper): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Costermonger): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Cutpurse): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DitchDigger): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DockWorker): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenApothecarist): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenBlacksmith): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenChestMaker): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenHerder): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenMiner): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenMinerTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenMushroomFarmer): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenRatCatcher): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenStonemason): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenStonemasonTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenArtisan): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenBarrister): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenChandler): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenFalconer): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenForester): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenForesterTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenGlassblower): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenNavigator): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenSage): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenSageTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Farmer): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerThree): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerFour): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerFive): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerSix): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerSeven): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerEight): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerNine): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FortuneTeller): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Gambler): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Gongfarmer): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Gravedigger): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.GravediggerTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.GuildBeggar): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.GuildBeggarTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingChickenButcher): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingDyer): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingDyerTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingGloveMaker): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingGypsy): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingHaberdasher): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingMariner): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingMoneylender): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingTrader): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingVagrant): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Healer): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Herbalist): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Herder): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Hunter): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HunterTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.IndenturedServant): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Jester): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Jewler): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Locksmith): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Mendicant): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Mercenary): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Merchant): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Baker): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Minstrel): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Noble): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Orphan): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Ostler): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Outlaw): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.RopeMaker): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Scribe): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Shaman): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Slave): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Smuggler): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Soldier): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Squire): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.SquireTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.TaxCollector): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Trapper): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.TrapperTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Urchin): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Wainwright): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Weaver): {
        "name": "Alchemist",
        "items": [

        ],
        "wearable_items": [

        ],
        "starting_loc": []
    },
    str(Occupation.WizardsApprentice): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Woodcutter): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.WoodcutterTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.WoodcutterThree): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    }
}
