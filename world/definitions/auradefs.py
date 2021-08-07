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
from utils.enum import AutoNumberEnum


class AuraEffectType(AutoNumberEnum):
    def __init__(self, display_name='unknown'):
        self.display_name = display_name

    MeleeAttack = "melee atk"
    MeleeDamage = "melee dmg"
    RangeAttack = "range atk"
    RangeDamage = "range dmg"
    UnarmedAttack = "unarmed atk"
    MountedAttack = "mounted atk"
    Skill = "skill"
    FindTraps = "find trap"
    DisableTraps = "disable trap"
    FindSecretDoors = "find door"
    SpellCheck = "spell chk"
    SpellDamage = "spell dmg"
    TurnUnholy = "turn unholy"
    Healing = "heal"
    ReflexSave = "reflex save"
    FortitudeSave = "fort save"
    WillpowerSave = "will save"
    TrapSave = "trap save"
    PoisonSave = "poison save"
    AC = "AC"
    HP = "HP"
    Initiative = "init"
    CriticalHit = "crit hit"
    Corruption = "corrupt"
    Fumble = "fumble"
    Language = "lang"
    Speed = "speed"
    Strength = "str"
    Agility = "agi"
    Stamina = "stam"
    Personality = "pers"
    Intelligence = "int"
    Luck = "luck"
    Age = "age"
    Light = "light"
    Darkness = "dark"
    AttackUnholy = "atk unholy"
    DamageUnholy = "dmg unholy"
    # TODO: likely address the other banes here
