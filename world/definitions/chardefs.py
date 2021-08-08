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

from utils.enum import AutoNumberEnum
from world.definitions.auradefs import AuraEffectType
from world.definitions.itemdefs import WeaponType

import world.prototypes.wearable.armor as armor
import world.prototypes.wearable.clothes as clothes
import world.prototypes.wearable.weapons as weapons

import world.prototypes.items.containers as containers
import world.prototypes.items.misc as miscitems
import world.prototypes.items.food as food
import world.prototypes.items.implements as implements


class Race(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Human = "Human"
    Dwarf = "Dwarf"
    Elf = "Elf"
    Halfling = "Halfling"
    Gnome = "Gnome"
    Bugbear = "Bugbear"
    Goblin = "Goblin"
    Gnoll = "Gnoll"
    Harpy = "Harpy"
    Hobgoblin = "Hobgoblin"
    Kobold = "Kobold"
    Lizardman = "Lizardman"
    Minotaur = "Minotaur"
    Ogre = "Ogre"
    Orc = "Orc"
    Serpentman = "Serpentman"
    Troglodyte = "Troglodyte"
    Angelic = "Angelic"
    Centaur = "Centaur"
    Demonic = "Demonic"
    Doppelganger = "Doppleganger"
    Dragon = "Dragon"
    Pixie = "Pixie"
    Giant = "Giant"
    Griffon = "Griffon"
    Naga = "Naga"
    Bear = "Bear"
    Eagle = "Eagle"
    Ferret = "Ferret"
    Horse = "Horse"
    Wolf = "Wolf"
    Spider = "Spider"


class Alignment(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Lawful = "Lawful"
    Neutral = "Neutral"
    Chaotic = "Chaotic"


class BirthAugur(AutoNumberEnum):
    def __init__(self, display_name=['unknown', 'unknown']):
        self.display_name = display_name

    HarshWinter = ["Harsh Winter", "Born into a harsh winter."]
    TheBull = ["The Bull", "Childhood nickname: The Bull"]
    FortunateDate = ["Fortunate Date", "Born on a fortunate date."]
    RaisedByWolves = ["Raised By Wolves", "Raised by wolves."]
    ConceivedOnHorseback = [
        "Conceived on Horseback", "Conceived on horseback."
    ]
    BornOnTheBattlefield = [
        "Born on the Battlefield", "Born on the battlefield."
    ]
    PathOfTheBear = ["Path of the Bear", "Followed the Path of the Bear."]
    Hawkeye = ["Hawkeye", "Has hawkeye vision."]

    # TODO: for packhunter, make initial weapon +1 and
    # useable only by that character
    PackHunter = ["Packhunter", "An innate pack hunter."]

    BornUnderTheLoom = ["Born Under the Loom", "Was born under a loom."]
    FoxCunning = ["Fox Cunning", "Born with the cunning of a fox."]
    FourLeafClover = [
        "Four Leaf Clover", "Influenced by the four leaf clover."
    ]
    SeventhChild = ["Seventh Child", "The seventh child of the house."]
    TheRagingStorm = [
        "The Raging Storm", "Born in the midst of a raging storm."
    ]
    RighteousHeart = [
        "Righteous Heart", "A heart that yearns for righteousness."
    ]

    SurvivedPlague = ["Survived Plague", "Survived a deadly plague."]
    LuckySign = ["Lucky Sign", "Has birthmark of a lucky sign."]
    GuardianAngel = ["Guardian Angel", "Visited by a guardian angel."]
    SurvivedSpiderBite = [
        "Survived Spider Bite", "Survived the bite of a deadly spider."
    ]

    StruckByLightning = [
        "Struck by Lightning", "Was struck by lightning and lived."
    ]

    LivedThroughFamine = ["Lived Through Famine", "Survived a brutal famine."]
    ResistedTemptation = [
        "Resisted Temptation", "Resisted a powerful temptation."
    ]
    CharmedHouse = ["Charmed House", "Was born to a charmed house."]
    SpeedOfTheCobra = ["Speed of the Cobra", "Has the speed of a cobra."]
    BountifulHarvest = [
        "Bountiful Harvest", "Every childhood harvest was bountiful."
    ]
    WarriorsArm = ["Warrior's Arm", "Has the arms of a warrior of old."]
    UnholyHouse = ["Unholy House", "Was born in an unholy house."]
    TheBrokenStar = [
        "The Broken Star", "Was born under the light of a broken star."
    ]
    Birdsong = ["Birdsong", "Heard the songs of birds in the womb."]
    WildChild = ["Wild Child", "Was a wild child."]


BirthAugurAuraTable = {
    BirthAugur.HarshWinter: {
        "effects": [
            AuraEffectType.MeleeAttack,
            AuraEffectType.RangeAttack
        ]
    },
    BirthAugur.TheBull: {
        "effects": [
            AuraEffectType.MeleeAttack
        ]
    },
    BirthAugur.FortunateDate: {
        "effects": [
            AuraEffectType.RangeAttack
        ]
    },
    BirthAugur.RaisedByWolves: {
        "effects": [
            AuraEffectType.UnarmedAttack
        ]
    },
    BirthAugur.ConceivedOnHorseback: {
        "effects": [
            AuraEffectType.MountedAttack
        ]
    },
    BirthAugur.BornOnTheBattlefield: {
        "effects": [
            AuraEffectType.MeleeDamage,
            AuraEffectType.RangeDamage,
            AuraEffectType.SpellDamage
        ]
    },
    BirthAugur.PathOfTheBear: {
        "effects": [
            AuraEffectType.MeleeDamage
        ]
    },
    BirthAugur.Hawkeye: {
        "effects": [
            AuraEffectType.RangeDamage
        ]
    },
    BirthAugur.BornUnderTheLoom: {
        "effects": [
            AuraEffectType.Skill
        ]
    },
    BirthAugur.FoxCunning: {
        "effects": [
            AuraEffectType.FindTraps,
            AuraEffectType.DisableTraps
        ]
    },
    BirthAugur.FourLeafClover: {
        "effects": [
            AuraEffectType.FindSecretDoors
        ]
    },
    BirthAugur.SeventhChild: {
        "effects": [
            AuraEffectType.SpellCheck
        ]
    },
    BirthAugur.TheRagingStorm: {
        "effects": [
            AuraEffectType.SpellDamage
        ]
    },
    BirthAugur.RighteousHeart: {
        "effects": [
            AuraEffectType.TurnUnholy
        ]
    },
    BirthAugur.SurvivedPlague: {
        "effects": [
            AuraEffectType.Healing
        ]
    },
    BirthAugur.LuckySign: {
        "effects": [
            AuraEffectType.ReflexSave,
            AuraEffectType.FortitudeSave,
            AuraEffectType.WillpowerSave
        ]
    },
    BirthAugur.GuardianAngel: {
        "effects": [
            AuraEffectType.TrapSave
        ]
    },
    BirthAugur.SurvivedSpiderBite: {
        "effects": [
            AuraEffectType.PoisonSave
        ]
    },
    BirthAugur.StruckByLightning: {
        "effects": [
            AuraEffectType.ReflexSave
        ]
    },
    BirthAugur.LivedThroughFamine: {
        "effects": [
            AuraEffectType.FortitudeSave
        ]
    },
    BirthAugur.ResistedTemptation: {
        "effects": [
            AuraEffectType.WillpowerSave
        ]
    },
    BirthAugur.CharmedHouse: {
        "effects": [
            AuraEffectType.AC
        ]
    },
    BirthAugur.SpeedOfTheCobra: {
        "effects": [
            AuraEffectType.Initiative
        ]
    },
    BirthAugur.BountifulHarvest: {
        "effects": [
            AuraEffectType.HP
        ]
    },
    BirthAugur.WarriorsArm: {
        "modifier_multiplier": 2,
        "effects": [
            AuraEffectType.CriticalHit
        ]
    },
    BirthAugur.UnholyHouse: {
        "effects": [
            AuraEffectType.Corruption
        ]
    },
    BirthAugur.TheBrokenStar: {
        "modifier_multiplier": 2,
        "effects": [
            AuraEffectType.Fumble
        ]
    },
    BirthAugur.Birdsong: {
        "effects": [
            AuraEffectType.Language
        ]
    },
    BirthAugur.WildChild: {
        "modifier_multiplier": 5,
        "effects": [
            AuraEffectType.Speed
        ]
    }
}


class ArmorCoverageLevel(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Unprotected = "Unprotected"
    BetterThanNothing = "Better than Nothing"
    Minimal = "Minimal"
    Soldier = "Solider"
    Medium = "Medium"
    Geared = "Geared"
    Protected = "Protected"
    Strong = "Strong"
    Armored = "Armored"
    Tank = "Tank"


class Language(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    Common = "Common"
    Thieves = "Thieves' Cant"
    Chaos = "Chaos"
    Law = "Law"
    Neutrality = "Neutrality"
    Dwarf = "Dwarf"
    Elf = "Elf"
    Halfling = "Halfling"
    Gnome = "Gnome"
    Bugbear = "Bugbear"
    Goblin = "Goblin"
    Gnoll = "Gnoll"
    Harpy = "Harpy"
    Hobgoblin = "Hobgoblin"
    Kobold = "Kobold"
    Lizardman = "Lizardman"
    Minotaur = "Minotaur"
    Ogre = "Ogre"
    Orc = "Orc"
    Serpentman = "Serpentman"
    Troglodyte = "Troglodyte"
    Angelic = "Angelic"
    Centaur = "Centaur"
    Demonic = "Demonic"
    Doppelganger = "Doppleganger"
    Dragon = "Dragon"
    Pixie = "Pixie"
    Giant = "Giant"
    Griffon = "Griffon"
    Naga = "Naga"
    Bear = "Bear"
    Eagle = "Eagle"
    Ferret = "Ferret"
    Horse = "Horse"
    Wolf = "Wolf"
    Spider = "Spider"
    Undercommon = "Undercommon"


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
            weapons.WOODEN_STAFF,
            containers.FLASK_OF_OIL,
            clothes.BROWN_LEATHER_APRON,
            clothes.WHITE_LINEN_SHIRT,
            clothes.BLACK_CANVAS_SHOES,
            clothes.GRAY_LINEN_PANTS
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.AnimalTrainer: {
        "items": [
            weapons.WOODEN_CLUB,
            clothes.GREEN_FEATHERED_CAP,
            armor.LARGE_HIDE_CLOAK,
            clothes.WHITE_LINEN_SHIRT,
            clothes.ROPE_BELT,
            armor.HIDE_PANTS,
            armor.LEATHER_BOOTS
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ]
    },
    Occupation.Armorer: {
        "items": [
            weapons.BALL_PEEN_HAMMER,
            clothes.WHITE_LINEN_SHIRT,
            armor.IRON_COIF,
            armor.LEATHER_PANTS,
            armor.THICK_LEATHER_GLOVES,
            clothes.BLACK_LEATHER_BELT,
            armor.LEATHER_BOOTS
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ]
    },
    Occupation.Astrologer: {
        "items": [
            weapons.SMALL_IRON_DAGGER,
            implements.SPYGLASS,
            clothes.PURPLE_STARRY_ROBE,
            clothes.ROPE_BELT
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.Barber: {
        "items": [
            weapons.FOLDING_STRAIGHT_EDGE_RAZOR,
            clothes.WHITE_COTTON_APRON,
            clothes.RED_SILK_SHIRT,
            clothes.BLACK_LEATHER_BELT,
            armor.LEATHER_PANTS,
            clothes.BLACK_CANVAS_SHOES,
            weapons.SCISSORS
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.Beadle: {
        "items": [
            weapons.WOODEN_STAFF,
            clothes.PURPLE_CEREMONIAL_OVERCOAT,
            clothes.ORANGE_COTTON_SHIRT,
            clothes.BLACK_SILK_TIGHTS,
            clothes.BLACK_CANVAS_SHOES,
            implements.HOLY_SYMBOL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.Beekeeper: {
        "items": [
            weapons.WOODEN_STAFF,
            containers.JAR_OF_HONEY,
            clothes.WHITE_LINEN_SHIRT,
            armor.LEATHER_PANTS,
            armor.LEATHER_BOOTS
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.Blacksmith: {
        "items": [
            clothes.WHITE_LINEN_SHIRT,
            armor.LEATHER_PANTS,
            armor.THICK_LEATHER_GLOVES,
            clothes.BLACK_LEATHER_BELT,
            armor.LEATHER_BOOTS,
            weapons.BALL_PEEN_HAMMER,
            implements.STEEL_TONGS
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ]
    },
    Occupation.Butcher: {
        "items": [
            weapons.SHARP_IRON_CLEAVER,
            clothes.WHITE_COTTON_SHIRT,
            armor.LEATHER_PANTS,
            clothes.BLACK_CANVAS_SHOES,
            clothes.WHITE_COTTON_APRON,
            food.SIDE_OF_BEEF
        ],
        "weapon_proficiencies": [
            WeaponType.Axe
        ]
    },
    Occupation.CaravanGuard: {
        "items": [
            weapons.IRON_SHORT_SWORD,
            clothes.SILK_SASH_BELT,
            armor.LARGE_BROWN_HOODED_CLOAK,
            armor.LEATHER_TUNIC,
            armor.LEATHER_PANTS,
            armor.LEATHER_BOOTS,
            miscitems.ROLL_OF_LINEN
        ],
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ]
    },
    Occupation.Cheesemaker: {
        "items": [
            clothes.WHITE_COTTON_APRON,
            clothes.WHITE_LINEN_SHIRT,
            clothes.YELLOW_SUSPENDERS,
            clothes.BLUE_DENIM_JEANS,
            armor.LEATHER_BOOTS,
            weapons.WOODEN_CUDGEL,
            food.STINKY_CHEESE
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.Cobbler: {
        "items": [
            clothes.SPECTACLES,
            clothes.WHITE_LINEN_SHIRT,
            clothes.BLACK_LEATHER_BELT,
            clothes.GRAY_LINEN_PANTS,
            armor.LEATHER_BOOTS,
            weapons.SHARP_STITCHING_AWL,
            miscitems.SHOEHORN
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.ConfidenceArtist: {
        "items": [
            clothes.RED_SILK_SHIRT,
            armor.HIDE_PANTS,
            armor.LARGE_BLACK_LEATHER_CLOAK,
            armor.LEATHER_BOOTS,
            weapons.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.Cooper: {
        "items": [
            armor.THICK_LEATHER_GLOVES,
            clothes.WHITE_LINEN_SHIRT,
            clothes.GRAY_LINEN_PANTS,
            armor.LEATHER_BOOTS,
            weapons.IRON_CROWBAR,
            containers.WOODEN_STORAGE_BARREL
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ]
    },
    Occupation.Costermonger: {
        "items": [
            clothes.WHITE_COTTON_APRON,
            clothes.WHITE_LINEN_SHIRT,
            clothes.BLACK_CANVAS_SHOES,
            clothes.GRAY_LINEN_PANTS,
            armor.LEATHER_BRACERS,
            weapons.IRON_PARING_KNIFE
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.Cutpurse: {
        "items": [
            armor.LARGE_BROWN_HOODED_CLOAK,
            weapons.SMALL_IRON_DAGGER,
            clothes.WHITE_LINEN_SHIRT,
            clothes.GRAY_LINEN_PANTS,
            armor.LEATHER_BOOTS,
            containers.SMALL_CHEST
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.DitchDigger: {
        "items": [
            clothes.BROWN_WOOL_CAP,
            clothes.STITCHED_HEMP_VEST,
            armor.THICK_LEATHER_GLOVES,
            clothes.GRAY_LINEN_PANTS,
            armor.LEATHER_BOOTS,
            miscitems.BAG_OF_FINE_DIRT,
            weapons.SHOVEL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.DockWorker: {
        "items": [
            clothes.WHITE_LINEN_SHIRT,
            armor.LEATHER_PANTS,
            weapons.POLE,
            miscitems.BOOK_OF_RPG_SECRETS,
            armor.LEATHER_BOOTS,
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.DwarvenApothecarist: {
        "race": Race.Dwarf,
        "items": [
            clothes.WHITE_COTTON_SHIRT,
            armor.THICK_LEATHER_GLOVES,
            clothes.BLACK_CANVAS_SHOES,
            clothes.GRAY_LINEN_PANTS,
            weapons.WOODEN_CUDGEL,
            containers.STEEL_VIAL
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.DwarvenBlacksmith: {
        "race": Race.Dwarf,
        "items": [
            clothes.WHITE_LINEN_SHIRT,
            armor.LEATHER_PANTS,
            armor.THICK_LEATHER_GLOVES,
            clothes.BLACK_LEATHER_BELT,
            armor.LEATHER_BOOTS,
            miscitems.CLUMP_OF_MITHRIL,
            weapons.BALL_PEEN_HAMMER
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ]
    },
    Occupation.DwarvenChestMaker: {
        "race": Race.Dwarf,
        "items": [
            clothes.CHECKERED_FLANNEL_SHIRT,
            armor.LEATHER_PANTS,
            armor.THICK_LEATHER_GLOVES,
            clothes.BLACK_LEATHER_BELT,
            miscitems.STACK_OF_WOOD,
            clothes.BLACK_CANVAS_SHOES,
            weapons.IRON_CHISEL
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.DwarvenHerder: {
        "race": Race.Dwarf,
        "items": [
            clothes.STITCHED_HEMP_VEST,
            armor.THICK_LEATHER_GLOVES,
            weapons.WOODEN_STAFF,
            armor.HIDE_PANTS,
            armor.LEATHER_BOOTS
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.DwarvenMiner: {
        "race": Race.Dwarf,
        "items": [
            clothes.STITCHED_HEMP_VEST,
            armor.IRON_HELM,
            weapons.IRON_MINING_PICK,
            armor.LEATHER_BOOTS,
            armor.LEATHER_PANTS,
            armor.THICK_LEATHER_GLOVES,
            implements.LANTERN
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ]
    },
    Occupation.DwarvenMushroomFarmer: {
        "race": Race.Dwarf,
        "items": [
            weapons.SHOVEL,
            clothes.WHITE_LINEN_SHIRT,
            clothes.ROPE_BELT,
            clothes.GRAY_LINEN_PANTS,
            armor.LEATHER_BOOTS,
            armor.THICK_LEATHER_GLOVES,
            miscitems.BURLAP_SACK
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.DwarvenRatCatcher: {
        "race": Race.Dwarf,
        "items": [
            clothes.WHITE_LINEN_SHIRT,
            clothes.GRAY_LINEN_PANTS,
            weapons.WOODEN_CLUB,
            clothes.BLACK_CANVAS_SHOES,
            implements.HEMP_NET
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ]
    },
    Occupation.DwarvenStonemason: {
        "race": Race.Dwarf,
        "items": [
            weapons.WOODEN_MALLET,
            clothes.WHITE_LINEN_SHIRT,
            clothes.GRAY_LINEN_PANTS,
            clothes.BLACK_CANVAS_SHOES,
            miscitems.BAG_OF_FINE_STONE
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ]
    },
    Occupation.ElvenArtisan: {
        "race": Race.Elf,
        "items": [
            clothes.GREEN_FEATHERED_CAP,
            weapons.WOODEN_STAFF,
            clothes.BLACK_LINEN_PANTS,
            clothes.PURPLE_SILK_SHIRT,
            armor.LEATHER_BOOTS,
            miscitems.BAG_OF_CLAY
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.ElvenBarrister: {
        "race": Race.Elf,
        "items": [
            clothes.WHITE_SILK_SHIRT,
            clothes.FINE_BLACK_LEATHER_SHOES,
            clothes.FINE_BLACK_SLACKS,
            clothes.SPECTACLES,
            weapons.MITHRIL_QUILL,
            miscitems.BOOK_OF_LEGAL_OPINIONS
        ]
    },
    Occupation.ElvenChandler: {
        "race": Race.Elf,
        "items": [
            clothes.WHITE_SILK_SHIRT,
            clothes.BLACK_LINEN_PANTS,
            clothes.BLACK_CANVAS_SHOES,
            weapons.SCISSORS
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.ElvenFalconer: {
        "race": Race.Elf,
        "items": [
            weapons.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ]
    },
    Occupation.ElvenForester: {
        "race": Race.Elf,
        "items": [
            weapons.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.ElvenGlassblower: {
        "race": Race.Elf,
        "items": [

        ]
    },
    Occupation.ElvenNavigator: {
        "race": Race.Elf,
        "items": [

        ]
    },
    Occupation.ElvenSage: {
        "race": Race.Elf,
        "items": [
            weapons.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ]
    },
    Occupation.Farmer: {
        "items": [

        ]
    },
    Occupation.FortuneTeller: {
        "items": [
            weapons.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ]
    },
    Occupation.Gambler: {
        "items": [
            weapons.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ]
    },
    Occupation.Gongfarmer: {
        "items": [

        ]
    },
    Occupation.Gravedigger: {
        "items": [

        ]
    },
    Occupation.GuildBeggar: {
        "items": [

        ]
    },
    Occupation.HalflingChickenButcher: {
        "race": Race.Halfling,
        "items": [

        ]
    },
    Occupation.HalflingDyer: {
        "race": Race.Halfling,
        "items": [
            weapons.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.HalflingGloveMaker: {
        "race": Race.Halfling,
        "items": [

        ]
    },
    Occupation.HalflingGypsy: {
        "race": Race.Halfling,
        "items": [

        ]
    },
    Occupation.HalflingHaberdasher: {
        "race": Race.Halfling,
        "items": [

        ]
    },
    Occupation.HalflingMariner: {
        "race": Race.Halfling,
        "items": [

        ]
    },
    Occupation.HalflingMoneylender: {
        "race": Race.Halfling,
        "items": [
            weapons.IRON_SHORT_SWORD
        ],
        "money": {
            "gold": 5,
            "silver": 10,
            "copper": 200
        },
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ]
    },
    Occupation.HalflingTrader: {
        "race": Race.Halfling,
        "items": [
            weapons.IRON_SHORT_SWORD
        ],
        "money": {
            "silver": 20,
        },
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ]
    },
    Occupation.HalflingVagrant: {
        "race": Race.Halfling,
        "items": [
            weapons.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ]
    },
    Occupation.Healer: {
        "items": [
            weapons.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ]
    },
    Occupation.Herbalist: {
        "items": [
            weapons.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ]
    },
    Occupation.Herder: {
        "items": [
            weapons.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.Hunter: {
        "items": [

        ]
    },
    Occupation.IndenturedServant: {
        "items": [
            weapons.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.Jester: {
        "items": [

        ]
    },
    Occupation.Jeweler: {
        "items": [
            weapons.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ]
    },
    Occupation.Locksmith: {
        "items": [
            weapons.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger

        ]
    },
    Occupation.Mendicant: {
        "items": [
            weapons.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ]
    },
    Occupation.Mercenary: {
        "items": [
            weapons.IRON_LONG_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.Longsword
        ]
    },
    Occupation.Merchant: {
        "items": [
            weapons.SMALL_IRON_DAGGER
        ],
        "money": {
            "gold": 4,
            "silver": 14,
            "copper": 27
        },
        "weapon_proficiencies": [
            WeaponType.Dagger

        ]
    },
    Occupation.Baker: {
        "items": [

        ]
    },
    Occupation.Minstrel: {
        "items": [
            weapons.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.Noble: {
        "items": [
            weapons.IRON_LONG_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.Longsword
        ]
    },
    Occupation.Orphan: {
        "items": [
            weapons.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club

        ]
    },
    Occupation.Ostler: {
        "items": [
            weapons.WOODEN_STAFF
        ],
        "weapon_proficiencies": [
            WeaponType.Staff
        ]
    },
    Occupation.Outlaw: {
        "items": [
            weapons.IRON_SHORT_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.ShortSword
        ]
    },
    Occupation.RopeMaker: {
        "items": [

        ]
    },
    Occupation.Scribe: {
        "items": [

        ]
    },
    Occupation.Shaman: {
        "items": [

        ]
    },
    Occupation.Slave: {
        "items": [
            weapons.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ]
    },
    Occupation.Smuggler: {
        "items": [

        ]
    },
    Occupation.Soldier: {
        "items": [

        ]
    },
    Occupation.Squire: {
        "items": [
            weapons.IRON_LONG_SWORD
        ],
        "weapon_proficiencies": [
            WeaponType.Longsword
        ]
    },
    Occupation.TaxCollector: {
        "items": [
            weapons.IRON_LONG_SWORD
        ],
        "money": {
            "copper": 100
        },
        "weapon_proficiencies": [
            WeaponType.Longsword
        ]
    },
    Occupation.Trapper: {
        "items": [

        ]
    },
    Occupation.Urchin: {
        "items": [

        ]
    },
    Occupation.Wainwright: {
        "items": [
            weapons.WOODEN_CLUB
        ],
        "weapon_proficiencies": [
            WeaponType.Club
        ]
    },
    Occupation.Weaver: {
        "items": [
            weapons.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.WizardsApprentice: {
        "items": [
            weapons.SMALL_IRON_DAGGER
        ],
        "weapon_proficiencies": [
            WeaponType.Dagger
        ]
    },
    Occupation.Woodcutter: {
        "items": [

        ]
    }
}
