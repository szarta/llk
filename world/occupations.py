#from enum import Enum
from world.weapons import WeaponType
import world.prototypes as prototypes
from world.races import Race


class Occupation:
    occupation_list = ('', 'Alchemist', 'AnimalTrainer', 'Armorer',
        'Astrologer', 'Barber', 'Beadle', 'Beekeeper', 'Blacksmith',
        'Butcher', 'CaravanGuard', 'Cheesemaker', 'Cobbler',
        'ConfidenceArtist', 'Cooper', 'Costermonger', 'Cutpurse',
        'DitchDigger', 'DockWorker', 'DwarvenApothecarist',
        'DwarvenBlacksmith', 'DwarvenChestMaker', 'DwarvenHerder',
        'DwarvenMiner', 'DwarvenMinerTwo', 'DwarvenMushroomFarmer',
        'DwarvenRatCatcher', 'DwarvenStonemason', 'DwarvenStonemasonTwo',
        'ElvenArtisan', 'ElvenBarrister', 'ElvenChandler', 'ElvenFalconer',
        'ElvenForester', 'ElvenForesterTwo', 'ElvenGlassblower',
        'ElvenNavigator', 'ElvenSage', 'ElvenSageTwo', 'Farmer', 'FarmerTwo',
        'FarmerThree', 'FarmerFour', 'FarmerFive', 'FarmerSix', 'FarmerSeven',
        'FarmerEight', 'FarmerNine', 'FortuneTeller', 'Gambler', 'Gongfarmer',
        'Gravedigger','GravediggerTwo', 'GuildBeggar', 'GuildBeggarTwo',
        'HalflingChickenButcher', 'HalflingDyer', 'HalflingDyerTwo',
        'HalflingGloveMaker', 'HalflingGypsy', 'HalflingHaberdasher',
        'HalflingMariner', 'HalflingMoneylender', 'HalflingTrader',
        'HalflingVagrant', 'Healer', 'Herbalist', 'Herder', 'Hunter',
        'HunterTwo', 'IndenturedServant', 'Jester', 'Jeweler', 'Locksmith',
        'Mendicant', 'Mercenary', 'Merchant', 'Baker', 'Minstrel', 'Noble',
        'Orphan', 'Ostler', 'Outlaw', 'RopeMaker', 'Scribe', 'Shaman',
        'Slave', 'Smuggler', 'Soldier', 'Squire', 'SquireTwo', 'TaxCollector',
        'Trapper', 'TrapperTwo', 'Urchin', 'Wainwright', 'Weaver',
        'WizardsApprentice', 'Woodcutter', 'WoodcutterTwo', 'WoodcutterThree0')

    def __init__(self, name):
        self.name = self.occupation_list[name]

    def __str__(self):
        return str(self.name)

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
    str(Occupation.Armorer): {
        "name": "Armorer",
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
    str(Occupation.Astrologer): {
        "name": "Astrologer",
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
    str(Occupation.Barber): {
        "name": "Barber",
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
    str(Occupation.Beadle): {
        "name": "Beadle",
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
    str(Occupation.Beekeeper): {
        "name": "Beekeeper",
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
    str(Occupation.Blacksmith): {
        "name": "Blacksmith",
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
    str(Occupation.Butcher): {
        "name": "Butcher",
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
    str(Occupation.CaravanGuard): {
        "name": "Caravan Guard",
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
    str(Occupation.Cheesemaker): {
        "name": "Cheesemaker",
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
