from evennia import DefaultObject
from enum import Enum


class AuraEffect(Enum):
    MeleeAttack = 1
    MeleeDamage = 2
    RangeAttack = 3
    RangeDamage = 4
    UnarmedAttack = 5
    MountedAttack = 6
    Skill = 7
    FindTraps = 9
    DisableTraps = 10
    FindSecretDoors = 11
    SpellCheck = 12
    SpellDamage = 13
    TurnUnholy = 14
    Healing = 15
    ReflexSave = 16
    FortitudeSave = 17
    WillpowerSave = 18
    TrapSave = 19
    PoisonSave = 20
    AC = 21
    HP = 22
    Initiative = 23
    CriticalHit = 24
    Corruption = 25
    Fumble = 25
    Language = 26
    Speed = 27
    Strength = 28
    Agility = 29
    Stamina = 30
    Personality = 31
    Intelligence = 32
    Luck = 33
    Age = 34
    Light = 35
    Darkness = 36
    AttackUnholy = 37
    DamageUnholy = 38
    # TODO: likely address the other banes here

    def short_desc(self):
        if self == AuraEffect.MeleeAttack:
            return "melee atk"
        elif self == AuraEffect.MeleeDamage:
            return "melee dmg"
        elif self == AuraEffect.RangeAttack:
            return "range atk"
        elif self == AuraEffect.RangeDamage:
            return "range dmg"
        elif self == AuraEffect.UnarmedAttack:
            return "unarmed atk"
        elif self == AuraEffect.MountedAttack:
            return "mounted atk"
        elif self == AuraEffect.Skill:
            return "skill"
        elif self == AuraEffect.FindTraps:
            return "find trap"
        elif self == AuraEffect.DisableTraps:
            return "disable trap"
        elif self == AuraEffect.FindSecretDoors:
            return "find door"
        elif self == AuraEffect.SpellCheck:
            return "spell chk"
        elif self == AuraEffect.SpellDamage:
            return "spell dmg"
        elif self == AuraEffect.TurnUnholy:
            return "turn unholy"
        elif self == AuraEffect.Healing:
            return "heal"
        elif self == AuraEffect.ReflexSave:
            return "reflex save"
        elif self == AuraEffect.FortitudeSave:
            return "fort save"
        elif self == AuraEffect.WillpowerSave:
            return "will save"
        elif self == AuraEffect.TrapSave:
            return "trap save"
        elif self == AuraEffect.PoisonSave:
            return "poison save"
        elif self == AuraEffect.AC:
            return "AC"
        elif self == AuraEffect.HP:
            return "HP"
        elif self == AuraEffect.Initiative:
            return "init"
        elif self == AuraEffect.CriticalHit:
            return "crit hit"
        elif self == AuraEffect.Fumble:
            return "fumble"
        elif self == AuraEffect.Language:
            return "language"
        elif self == AuraEffect.Speed:
            return "speed"
        elif self == AuraEffect.Strength:
            return "str"
        elif self == AuraEffect.Agility:
            return "agi"
        elif self == AuraEffect.Stamina:
            return "stam"
        elif self == AuraEffect.Personality:
            return "pers"
        elif self == AuraEffect.Intelligence:
            return "int"
        elif self == AuraEffect.Corruption:
            return "corruption"
        elif self == AuraEffect.Luck:
            return "luck"
        elif self == AuraEffect.Age:
            return "age"
        elif self == AuraEffect.Light:
            return "light"
        elif self == AuraEffect.Darkness:
            return "darkness"
        elif self == AuraEffect.AttackUnholy:
            return "atk unholy"
        elif self == AuraEffect.DamageUnholy:
            return "dmg unholy"
        else:
            return "unknown"


class PersistentEffectAura(DefaultObject):

    def at_object_creation(self):
        super().at_object_creation()

        self.db.hidden = False
        self.db.known_effects = True
        self.db.effect_modifiers = {}
        self.db.modifier_description = "+0 stam"
        self.db.understandable_description = "You know this aura."
        self.db.indecipherable_description = "Gives a faint glow."

        self.db.desc = "This is an aura."

    def build_modifier_description(self):
        modifier_description = ""
        for k in self.db.effect_modifiers.keys():
            effect_desc = k.short_desc()
            modifier = self.db.effect_modifiers[k]
            sign = "-"
            if modifier >= 0:
                sign = "+"
            modifier = abs(modifier)

            modifier_description = f'{modifier_description},{effect_desc} {sign}{modifier}'

        self.db.modifier_description = modifier_description.lstrip(",")
