import random

from utils.enum import AutoNumberEnum
from world.weapons import WeaponType
import world.prototypes as prototypes
from world.races import Race


class Occupation(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Alchemist = "Alchemist"
    AnimalTrainer = "Animal Trainer"
    Armorer = "Armorer"
    Astrologer = "Astrologer"
    Barber = "Barber"
    Beadle = "Beadle"
    Beekeeper = "Beekeeper"
    Blacksmith = "Blacksmith"
    Butcher = "Butcher"
    CaravanGuard = "Caravan Guard"
    Cheesemaker = "Cheesemaker"
    Cobbler = "Cobbler"
    ConfidenceArtist = "Confidence Artist"
    Cooper = "Cooper"
    Costermonger = "Costermonger"
    Cutpurse = "Cutpurse"
    DitchDigger = "Ditch Digger"
    DockWorker = "Dock Worker"
    DwarvenApothecarist = "Apothecarist"
    DwarvenBlacksmith = "Blacksmith"
    DwarvenChestMaker = "Chest Maker"
    DwarvenHerder = "Herder"
    DwarvenMiner = "Miner"
    DwarvenMushroomFarmer = "Mushroom Farmer"
    DwarvenRatCatcher = "Rat Catcher"
    DwarvenStonemason = "Stonemason"
    ElvenArtisan = "Artisan"
    ElvenBarrister = "Barrister"
    ElvenChandler = "Chandler"
    ElvenFalconer = "Falconer"
    ElvenForester = "Forester"
    ElvenGlassblower = "Glassblower"
    ElvenNavigator = "Navigator"
    ElvenSage = "Sage"
    Farmer = "Farmer"
    FortuneTeller = "FortuneTeller"
    Gambler = "Gambler"
    Gongfarmer = "Gongfarmer"
    Gravedigger = "Gravedigger"
    GuildBeggar = "Guild Beggar"
    HalflingChickenButcher = "Chicken Butcher"
    HalflingDyer = "Dyer"
    HalflingGloveMaker = "Glove Maker"
    HalflingGypsy = "Gypsy"
    HalflingHaberdasher = "Haberdasher"
    HalflingMariner = "Mariner"
    HalflingMoneylender = "Moneylender"
    HalflingTrader = "Trader"
    HalflingVagrant = "Vagrant"
    Healer = "Healer"
    Herbalist = "Herbalist"
    Herder = "Herder"
    Hunter = "Hunter"
    IndenturedServant = "Indentured Servant"
    Jester = "Jester"
    Jeweler = "Jeweler"
    Locksmith = "Locksmith"
    Mendicant = "Mendicant"
    Mercenary = "Mercenary"
    Merchant = "Merchant"
    Baker = "Baker"
    Minstrel = "Minstrel"
    Noble = "Noble"
    Orphan = "Orphan"
    Ostler = "Ostler"
    Outlaw = "Outlaw"
    RopeMaker = "Rope Maker"
    Scribe = "Scribe"
    Shaman = "Shaman"
    Slave = "Slave"
    Smuggler = "Smuggler"
    Soldier = "Soldier"
    Squire = "Squire"
    TaxCollector = "Tax Collector"
    Trapper = "Trapper"
    Urchin = "Urchin"
    Wainwright = "Wainwright"
    Weaver = "Weaver"
    WizardsApprentice = "Wizard's Apprentice"
    Woodcutter = "Woodcutter"


def get_random_occupation():
    occupations = list(Occupation)

    # DCC occupation table gives some occupations multiple chances
    occupations.append(Occupation.DwarvenMiner)
    occupations.append(Occupation.DwarvenStonemason)
    occupations.append(Occupation.ElvenForester)
    occupations.append(Occupation.ElvenSage)
    for i in range(0, 8):
        occupations.append(Occupation.Farmer)
    occupations.append(Occupation.Gravedigger)
    occupations.append(Occupation.GuildBeggar)
    occupations.append(Occupation.HalflingDyer)
    occupations.append(Occupation.Hunter)
    occupations.append(Occupation.Squire)
    occupations.append(Occupation.Trapper)
    occupations.append(Occupation.Woodcutter)

    return random.choice(occupations)


OccupationTable = {
    Occupation.Alchemist: {
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
    Occupation.AnimalTrainer: {
        "items": [
            prototypes.GREEN_FEATHERED_CAP,
            prototypes.LARGE_HIDE_CLOAK,
            prototypes.WHITE_LINEN_SHIRT,
            prototypes.ROPE_BELT,
            prototypes.MIXED_HIDE_PANTS,
            prototypes.WOODEN_CLUB,
            prototypes.LEATHER_BOOTS
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    Occupation.Armorer: {
        "items": [
            prototypes.WHITE_LINEN_SHIRT,
            prototypes.IRON_HELMET,
            prototypes.LEATHER_PANTS,
            prototypes.THICK_LEATHER_GLOVES,
            prototypes.BLACK_LEATHER_BELT,
            prototypes.LEATHER_BOOTS,
            prototypes.BALL_PEEN_HAMMER
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    Occupation.Astrologer: {
        "items": [
            prototypes.SMALL_IRON_DAGGER,
            prototypes.SPYGLASS,
            prototypes.PURPLE_STARRY_ROBE,
            prototypes.ROPE_BELT,
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    Occupation.Barber: {
        "items": [
            prototypes.APRON,
            prototypes.RED_SILK_SHIRT,
            prototypes.BLACK_LEATHER_BELT,
            prototypes.LEATHER_PANTS,
            prototypes.BLACK_CANVAS_SHOES,
            prototypes.FOLDING_STRAIGHT_EDGE_RAZOR,
            prototypes.SCISSORS
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    Occupation.Beadle: {
        "items": [
            prototypes.PURPLE_CEREMONIAL_OVERCOAT,
            prototypes.ORANGE_COTTON_SHIRT,
            prototypes.BLACK_SILK_TIGHTS,
            prototypes.BLACK_CANVAS_SHOES,
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.Beekeeper: {
        "items": [
            prototypes.WOODEN_STAFF,
            prototypes.JAR_OF_HONEY,
            prototypes.WHITE_LINEN_SHIRT,
            prototypes.LEATHER_PANTS,
            prototypes.LEATHER_BOOTS
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.Blacksmith: {
        "items": [
            prototypes.WHITE_LINEN_SHIRT,
            prototypes.LEATHER_PANTS,
            prototypes.THICK_LEATHER_GLOVES,
            prototypes.BLACK_LEATHER_BELT,
            prototypes.LEATHER_BOOTS,
            prototypes.BALL_PEEN_HAMMER,
            prototypes.STEEL_TONGS
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    Occupation.Butcher: {
        "items": [
            prototypes.SHARP_IRON_CLEAVER,
            prototypes.WHITE_COTTON_SHIRT,
            prototypes.LEATHER_PANTS,
            prototypes.BLACK_CANVAS_SHOES,
            prototypes.APRON,
            prototypes.SIDE_OF_BEEF
        ],
        "weapon_proficiencies": [
            WeaponType.Axe
        ],
        "starting_loc": []
    },
    Occupation.CaravanGuard: {
        "items": [
            prototypes.IRON_SHORT_SWORD,
            prototypes.SILK_SASH_BELT,
            prototypes.LARGE_BROWN_HOODED_CLOAK,
            prototypes.LEATHER_TUNIC,
            prototypes.LEATHER_PANTS,
            prototypes.LEATHER_BOOTS
        ],
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ],
        "starting_loc": []
    },
    Occupation.Cheesemaker: {
        "items": [
            prototypes.APRON,
            prototypes.WHITE_LINEN_SHIRT,
            prototypes.YELLOW_SUSPENDERS,
            prototypes.BLUE_COTTON_JEANS,
            prototypes.LEATHER_BOOTS,
            prototypes.WOODEN_CUDGEL,
            prototypes.STINKY_CHEESE
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.Cobbler: {
        "items": [
            prototypes.SHARP_STITCHING_AWL
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    Occupation.ConfidenceArtist: {
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    Occupation.Cooper: {
        "items": [
            prototypes.IRON_CROWBAR
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    Occupation.Costermonger: {
        "items": [
            prototypes.IRON_PARING_KNIFE
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    Occupation.Cutpurse: {
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    Occupation.DitchDigger: {
        "items": [
            prototypes.SHOVEL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.DockWorker: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.DwarvenApothecarist: {
        "race": Race.Dwarf,
        "items": [
            prototypes.WOODEN_CUDGEL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.DwarvenBlacksmith: {
        "race": Race.Dwarf,
        "items": [
            prototypes.BALL_PEEN_HAMMER
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    Occupation.DwarvenChestMaker: {
        "race": Race.Dwarf,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.DwarvenHerder: {
        "race": Race.Dwarf,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.DwarvenMiner: {
        "race": Race.Dwarf,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.DwarvenMushroomFarmer: {
        "race": Race.Dwarf,
        "items": [
            prototypes.SHOVEL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.DwarvenRatCatcher: {
        "race": Race.Dwarf,
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    Occupation.DwarvenStonemason: {
        "race": Race.Dwarf,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.ElvenArtisan: {
        "race": Race.Elf,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.ElvenBarrister: {
        "race": Race.Elf,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.ElvenChandler: {
        "race": Race.Elf,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.ElvenFalconer: {
        "race": Race.Elf,
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    Occupation.ElvenForester: {
        "race": Race.Elf,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.ElvenGlassblower: {
        "race": Race.Elf,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.ElvenNavigator: {
        "race": Race.Elf,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.ElvenSage: {
        "race": Race.Elf,
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    Occupation.Farmer: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.FortuneTeller: {
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    Occupation.Gambler: {
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    Occupation.Gongfarmer: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Gravedigger: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.GuildBeggar: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.HalflingChickenButcher: {
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.HalflingDyer: {
        "race": Race.Halfling,
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.HalflingGloveMaker: {
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.HalflingGypsy: {
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.HalflingHaberdasher: {
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.HalflingMariner: {
        "race": Race.Halfling,
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.HalflingMoneylender: {
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
    Occupation.HalflingTrader: {
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
    Occupation.HalflingVagrant: {
        "race": Race.Halfling,
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    Occupation.Healer: {
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    Occupation.Herbalist: {
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    Occupation.Herder: {
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.Hunter: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.IndenturedServant: {
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.Jester: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Jeweler: {
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    Occupation.Locksmith: {
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ],
        "starting_loc": []
    },
    Occupation.Mendicant: {
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    Occupation.Mercenary: {
        "items": [
            prototypes.IRON_LONG_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.Longsword
        ],
        "starting_loc": []
    },
    Occupation.Merchant: {
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
    Occupation.Baker: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Minstrel: {
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    Occupation.Noble: {
        "items": [
            prototypes.IRON_LONG_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.Longsword
        ],
        "starting_loc": []
    },
    Occupation.Orphan: {
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ],
        "starting_loc": []
    },
    Occupation.Ostler: {
        "items": [
            prototypes.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ],
        "starting_loc": []
    },
    Occupation.Outlaw: {
        "items": [
            prototypes.IRON_SHORT_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ],
        "starting_loc": []
    },
    Occupation.RopeMaker: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Scribe: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Shaman: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Slave: {
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    Occupation.Smuggler: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Soldier: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Squire: {
        "items": [
            prototypes.IRON_LONG_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.Longsword
        ],
        "starting_loc": []
    },
    Occupation.TaxCollector: {
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
    Occupation.Trapper: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Urchin: {
        "items": [

        ],
        "starting_loc": []
    },
    Occupation.Wainwright: {
        "items": [
            prototypes.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ],
        "starting_loc": []
    },
    Occupation.Weaver: {
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    Occupation.WizardsApprentice: {
        "items": [
            prototypes.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ],
        "starting_loc": []
    },
    Occupation.Woodcutter: {
        "items": [

        ],
        "starting_loc": []
    }
}
