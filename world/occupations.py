from enum import Enum
from world.weapons import WeaponType
import world.prototypes as prototypes
from world.races import Race


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
    Jeweler = 72
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
            prototypes.APRON,
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
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    str(Occupation.Armorer): {
        "name": "Armorer",
        "items": [
            prototypes.BALL_PEEN_HAMMER
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    str(Occupation.Astrologer): {
        "name": "Astrologer",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    str(Occupation.Barber): {
        "name": "Barber",
        "items": [
            prototypes.FOLDING_STRAIGHT_EDGE_RAZOR
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    str(Occupation.Beadle): {
        "name": "Beadle",
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.Beekeeper): {
        "name": "Beekeeper",
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.Blacksmith): {
        "name": "Blacksmith",
        "items": [
            prototypes.BALL_PEEN_HAMMER
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    str(Occupation.Butcher): {
        "name": "Butcher",
        "items": [
            prototypes.SHARP_IRON_CLEAVER
        ],
        "weapon_proficiencies": [
            WeaponType.Axe
        ],
        "starting_loc": []
    },
    str(Occupation.CaravanGuard): {
        "name": "Caravan Guard",
        "items": [
            prototypes.IRON_SHORT_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ],
        "starting_loc": []
    },
    str(Occupation.Cheesemaker): {
        "name": "Cheesemaker",
        "items": [
            prototypes.WOODEN_CUDGEL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.Cobbler): {
        "name": "Cobbler",
        "items": [
            prototypes.SHARP_STITCHING_AWL
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    str(Occupation.ConfidenceArtist): {
        "name": "Confidence Artist",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    str(Occupation.Cooper): {
        "name": "Cooper",
        "items": [
            prototypes.IRON_CROWBAR
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    str(Occupation.Costermonger): {
        "name": "Costermonger",
        "items": [
            prototypes.IRON_PARING_KNIFE
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    str(Occupation.Cutpurse): {
        "name": "Cutpurse",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    str(Occupation.DitchDigger): {
        "name": "Ditch Digger",
        "items": [
            prototypes.SHOVEL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.DockWorker): {
        "name": "Dock Worker",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenApothecarist): {
        "name": "Apothecarist",
        "race": Race.Dwarf,
        "items": [
            prototypes.WOODEN_CUDGEL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenBlacksmith): {
        "name": "Blacksmith",
        "race": Race.Dwarf,
        "items": [
            prototypes.BALL_PEEN_HAMMER
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenChestMaker): {
        "name": "Chest Maker",
        "race": Race.Dwarf,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenHerder): {
        "name": "Herder",
        "race": Race.Dwarf,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenMiner): {
        "name": "Miner",
        "race": Race.Dwarf,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenMinerTwo): {
        "name": "Miner",
        "race": Race.Dwarf,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenMushroomFarmer): {
        "name": "Mushroom Farmer",
        "race": Race.Dwarf,
        "items": [
            prototypes.SHOVEL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenRatCatcher): {
        "name": "Rat Catcher",
        "race": Race.Dwarf,
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenStonemason): {
        "name": "Stonemason",
        "race": Race.Dwarf,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.DwarvenStonemasonTwo): {
        "name": "Stonemason",
        "race": Race.Dwarf,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenArtisan): {
        "name": "Artisan",
        "race": Race.Elf,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.ElvenBarrister): {
        "name": "Barrister",
        "race": Race.Elf,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenChandler): {
        "name": "Chandler",
        "race": Race.Elf,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenFalconer): {
        "name": "Falconer",
        "race": Race.Elf,
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenForester): {
        "name": "Forester",
        "race": Race.Elf,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.ElvenForesterTwo): {
        "name": "Forester",
        "race": Race.Elf,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.ElvenGlassblower): {
        "name": "Glassblower",
        "race": Race.Elf,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenNavigator): {
        "name": "Navigator",
        "race": Race.Elf,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenSage): {
        "name": "Sage",
        "race": Race.Elf,
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    str(Occupation.ElvenSageTwo): {
        "name": "Sage",
        "race": Race.Elf,
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    str(Occupation.Farmer): {
        "name": "Farmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerTwo): {
        "name": "Farmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerThree): {
        "name": "Farmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerFour): {
        "name": "Farmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerFive): {
        "name": "Farmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerSix): {
        "name": "Farmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerSeven): {
        "name": "Farmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerEight): {
        "name": "Farmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FarmerNine): {
        "name": "Farmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.FortuneTeller): {
        "name": "Fortune Teller",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    str(Occupation.Gambler): {
        "name": "Gambler",
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    str(Occupation.Gongfarmer): {
        "name": "Gongfarmer",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Gravedigger): {
        "name": "Grave Digger",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.GravediggerTwo): {
        "name": "Grave Digger",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.GuildBeggar): {
        "name": "Guild Beggar",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.GuildBeggarTwo): {
        "name": "Guild Beggar",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingChickenButcher): {
        "name": "Alchemist",
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingDyer): {
        "name": "Dyer",
        "race": Race.Halfling,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.HalflingDyerTwo): {
        "name": "Dyer",
        "race": Race.Halfling,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.HalflingGloveMaker): {
        "name": "Glovemaker",
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingGypsy): {
        "name": "Gypsy",
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingHaberdasher): {
        "name": "Haberdasher",
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingMariner): {
        "name": "Mariner",
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HalflingMoneylender): {
        "name": "Moneylender",
        "race": Race.Halfling,
        "items": [
            prototypes.IRON_SHORT_SWORD
        ],
        "money": {
            "gold": 5,
            "silver": 10,
            "copper": 200
        },
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ],
        "starting_loc": []
    },
    str(Occupation.HalflingTrader): {
        "name": "Trader",
        "race": Race.Halfling,
        "items": [
            prototypes.IRON_SHORT_SWORD
        ],
        "money": {
            "silver": 20,
        },
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ],
        "starting_loc": []
    },
    str(Occupation.HalflingVagrant): {
        "name": "Vagrant",
        "race": Race.Halfling,
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    str(Occupation.Healer): {
        "name": "Healer",
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    str(Occupation.Herbalist): {
        "name": "Herbalist",
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    str(Occupation.Herder): {
        "name": "Herder",
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.Hunter): {
        "name": "Hunter",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.HunterTwo): {
        "name": "Hunter",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.IndenturedServant): {
        "name": "Indentured Servant",
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.Jester): {
        "name": "Jester",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Jeweler): {
        "name": "Jeweler",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    str(Occupation.Locksmith): {
        "name": "Locksmith",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    str(Occupation.Mendicant): {
        "name": "Mendicant",
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    str(Occupation.Mercenary): {
        "name": "Mercenary",
        "items": [
            prototypes.IRON_LONG_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.Longsword
        ],
        "starting_loc": []
    },
    str(Occupation.Merchant): {
        "name": "Merchant",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "money": {
            "gold": 4,
            "silver": 14,
            "copper": 27
        },
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    str(Occupation.Baker): {
        "name": "Baker",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Minstrel): {
        "name": "Minstrel",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    str(Occupation.Noble): {
        "name": "Noble",
        "items": [
            prototypes.IRON_LONG_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.Longsword
        ],
        "starting_loc": []
    },
    str(Occupation.Orphan): {
        "name": "Orphan",
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    str(Occupation.Ostler): {
        "name": "Ostler",
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    str(Occupation.Outlaw): {
        "name": "Outlaw",
        "items": [
            prototypes.IRON_SHORT_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ],
        "starting_loc": []
    },
    str(Occupation.RopeMaker): {
        "name": "Rope Maker",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Scribe): {
        "name": "Scribe",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Shaman): {
        "name": "Shaman",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Slave): {
        "name": "Slave",
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    str(Occupation.Smuggler): {
        "name": "Smuggler",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Soldier): {
        "name": "Soldier",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Squire): {
        "name": "Squire",
        "items": [
            prototypes.IRON_LONG_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.Longsword
        ],
        "starting_loc": []
    },
    str(Occupation.SquireTwo): {
        "name": "Alchemist",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.TaxCollector): {
        "name": "Tax Collector",
        "items": [
            prototypes.IRON_LONG_SWORD
        ],
        "money": {
            "copper": 100
        },
        "weapon_proficiencies": [
            WeaponType.Longsword
        ],
        "starting_loc": []
    },
    str(Occupation.Trapper): {
        "name": "Trapper",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.TrapperTwo): {
        "name": "Trapper",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Urchin): {
        "name": "Urchin",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.Wainwright): {
        "name": "Wainwright",
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    str(Occupation.Weaver): {
        "name": "Weaver",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    str(Occupation.WizardsApprentice): {
        "name": "Wizard's Apprentice",
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    str(Occupation.Woodcutter): {
        "name": "Woodcutter",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.WoodcutterTwo): {
        "name": "Woodcutter",
        "items": [

        ],
        "starting_loc": []
    },
    str(Occupation.WoodcutterThree): {
        "name": "Woodcutter",
        "items": [

        ],
        "starting_loc": []
    }
}
