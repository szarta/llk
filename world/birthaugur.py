from enum import Enum
from typeclasses.auras import AuraEffect


class BirthAugur(Enum):
    HarshWinter = 1
    TheBull = 2
    FortunateDate = 3
    RaisedByWolves = 4
    ConceivedOnHorseback = 5
    BornOnTheBattlefield = 6
    PathOfTheBear = 7
    Hawkeye = 8
    PackHunter = 9
    BornUnderTheLoom = 10
    FoxCunning = 11
    FourLeafClover = 12
    SeventhChild = 13
    TheRagingStorm = 14
    RighteousHeart = 15
    SurvivedPlague = 16
    LuckySign = 17
    GuardianAngel = 18
    SurvivedSpiderBite = 19
    StruckByLightning = 20
    LivedThroughFamine = 21
    ResistedTemptation = 22
    CharmedHouse = 23
    SpeedOfTheCobra = 24
    BountifulHarvest = 25
    WarriorsArm = 26
    UnholyHouse = 27
    TheBrokenStar = 28
    Birdsong = 29
    WildChild = 30


BirthAugurTable = {
    str(BirthAugur.HarshWinter): {
        "name": "Harsh Winter",
        "desc": "Born into a harsh winter.",
        "effects": [
            AuraEffect.MeleeAttack,
            AuraEffect.RangeAttack
        ]
    },
    str(BirthAugur.TheBull): {
        "name": "The Bull",
        "desc": "Childhood nickname: The Bull",
        "effects": [
            AuraEffect.MeleeAttack
        ]
    },
    str(BirthAugur.FortunateDate): {
        "name": "Fortunate Date",
        "desc": "Born on a lucky date.",
        "effects": [
            AuraEffect.RangeAttack
        ]
    },
    str(BirthAugur.RaisedByWolves): {
        "name": "Raised by Wolves",
        "desc": "Raised by wolves.",
        "effects": [
            AuraEffect.UnarmedAttack
        ]
    },
    str(BirthAugur.ConceivedOnHorseback): {
        "name": "Conceived on Horseback",
        "desc": "Conceived on horseback.",
        "effects": [
            AuraEffect.MountedAttack
        ]
    },
    str(BirthAugur.BornOnTheBattlefield): {
        "name": "Born on the Battlefield",
        "desc": "Born on the battlefield.",
        "effects": [
            AuraEffect.MeleeDamage,
            AuraEffect.RangeDamage,
            AuraEffect.SpellDamage
        ]
    },
    str(BirthAugur.PathOfTheBear): {
        "name": "Path of the Bear",
        "desc": "Followed the Path of the Bear.",
        "effects": [
            AuraEffect.MeleeDamage
        ]
    },
    str(BirthAugur.Hawkeye): {
        "name": "Hawkeye",
        "desc": "Has hawkeye vision.",
        "effects": [
            AuraEffect.RangeDamage
        ]
    },
    str(BirthAugur.PackHunter): {
        "name": "Pack Hunter",
        "desc": "An innate pack hunter."
    },
    str(BirthAugur.BornUnderTheLoom): {
        "name": "Born Under the Loom",
        "desc": "Born under the loom.",
        "effects": [
            AuraEffect.Skill
        ]
    },
    str(BirthAugur.FoxCunning): {
        "name": "Fox Cunning",
        "desc": "Born with the cunning of a fox",
        "effects": [
            AuraEffect.FindTraps,
            AuraEffect.DisableTraps
        ]
    },
    str(BirthAugur.FourLeafClover): {
        "name": "Four Leaf Clover",
        "desc": "Influenced by the four leaf clover.",
        "effects": [
            AuraEffect.FindSecretDoors
        ]
    },
    str(BirthAugur.SeventhChild): {
        "name": "Seventh Child",
        "desc": "The seventh child of the house.",
        "effects": [
            AuraEffect.SpellCheck
        ]
    },
    str(BirthAugur.TheRagingStorm): {
        "name": "The Raging Storm",
        "desc": "Born in the midst of a raging storm.",
        "effects": [
            AuraEffect.SpellDamage
        ]
    },
    str(BirthAugur.RighteousHeart): {
        "name": "Righteous Heart",
        "desc": "A heart that yearns for righteousness.",
        "effects": [
            AuraEffect.TurnUnholy
        ]
    },
    str(BirthAugur.SurvivedPlague): {
        "name": "Survived Plague",
        "desc": "Survived a deadly plague.",
        "effects": [
            AuraEffect.Healing
        ]
    },
    str(BirthAugur.LuckySign): {
        "name": "Lucky Sign",
        "desc": "Has birthmark of a lucky sign.",
        "effects": [
            AuraEffect.ReflexSave,
            AuraEffect.FortitudeSave,
            AuraEffect.WillpowerSave
        ]
    },
    str(BirthAugur.GuardianAngel): {
        "name": "Guardian Angel",
        "desc": "Visited by a guardian angel",
        "effects": [
            AuraEffect.TrapSave
        ]
    },
    str(BirthAugur.SurvivedSpiderBite): {
        "name": "Survived Spider Bite",
        "desc": "Survived the bite of a deadly spider.",
        "effects": [
            AuraEffect.PoisonSave
        ]
    },
    str(BirthAugur.StruckByLightning): {
        "name": "Struck By Lightning",
        "desc": "Was struck by lightning and lived.",
        "effects": [
            AuraEffect.ReflexSave
        ]
    },
    str(BirthAugur.LivedThroughFamine): {
        "name": "Lived Through Famine",
        "desc": "Lived through a severe famine.",
        "effects": [
            AuraEffect.FortitudeSave
        ]
    },
    str(BirthAugur.ResistedTemptation): {
        "name": "Resisted Temptation",
        "desc": "Resisted a powerful temptation.",
        "effects": [
            AuraEffect.WillpowerSave
        ]
    },
    str(BirthAugur.CharmedHouse): {
        "name": "Charmed House",
        "desc": "Born to a charmed house.",
        "effects": [
            AuraEffect.AC
        ]
    },
    str(BirthAugur.SpeedOfTheCobra): {
        "name": "Speed of the Cobra",
        "desc": "Has the speed of a cobra.",
        "effects": [
            AuraEffect.Initiative
        ]
    },
    str(BirthAugur.BountifulHarvest): {
        "name": "Bountiful Harvest",
        "desc": "Childhood blessed by bountiful harvests.",
        "effects": [
            AuraEffect.HP
        ]
    },
    str(BirthAugur.WarriorsArm): {
        "name": "Warrior's Arm",
        "desc": "Has the arms of a true warrior.",
        "modifier_multiplier": 2,
        "effects": [
            AuraEffect.CriticalHit
        ]
    },
    str(BirthAugur.UnholyHouse): {
        "name": "Unholy House",
        "desc": "Born to an unholy household.",
        "effects": [
            AuraEffect.Corruption
        ]
    },
    str(BirthAugur.TheBrokenStar): {
        "name": "The Broken Star",
        "desc": "Born in the light of a Broken Star.",
        "modifier_multiplier": 2,
        "effects": [
            AuraEffect.Fumble
        ]
    },
    str(BirthAugur.Birdsong): {
        "name": "Birdsong",
        "desc": "Heard the songs of birds in the womb.",
        "effects": [
            AuraEffect.Language
        ]
    },
    str(BirthAugur.WildChild): {
        "name": "Wild Child",
        "desc": "Was a wild child.",
        "modifier_multiplier": 5,
        "effects": [
            AuraEffect.Speed
        ]
    }
}
