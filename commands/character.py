from evennia import Command
from evennia.utils.ansi import raw as raw_ansi
from typeclasses.items import WearLocation
from typeclasses.characters import calculate_ability_modifier
from evennia.utils import utils
from world.birthaugur import BirthAugurTable
from world.occupations import OccupationTable


class CmdSheet(Command):
    key = "sheet"

    def func(self):
        caller = self.caller
        stat_sheet = """
+--------------------------------------------------------
| Name: {name}
| Age: {age}, Gender: {gender}
| Birth Augur: {augur}
| Alignment: {align}
| Occupation: {occupation}
| Wealth: {gold}gp, {silver}sp, {copper}cp
| Level: {level}, XP: {xp}
+--------------------------------------------------------
| Str  : {strength}  |  HP : {cur_hp} (max: {max_hp})
| Agi  : {agility}  |  AC : {ac}
| Stam : {stamina}  |
| Pers : {personality}  |
| Int  : {intelligence}  |
| Luck : {luck}  |
+--------------------------------------------------------
| Known Languages: {languages}
+--------------------------------------------------------
"""

        languages = ""
        current_line = ""
        first_line = True
        for lang in caller.db.known_languages:
            lang_str = str(lang)
            lang_len = len(lang_str)
            line_length = 52
            if first_line:
                line_length = 40

            if (len(current_line) + lang_len) > line_length:
                if first_line:
                    first_line = False

                current_line.rstrip(",")
                languages += current_line
                current_line = "\n|   "

            current_line = f'{current_line}{lang_str},'

        languages += current_line.rstrip(",")

        augur_str = BirthAugurTable[str(caller.db.birth_augur)]["desc"]

        caller.msg(stat_sheet.format(
            name=caller.name,
            age=caller.db.age,
            level=caller.db.level,
            xp=caller.db.xp,
            gender=caller.db.gender,
            occupation=OccupationTable[str(caller.db.occupation)]["name"],
            align=str(caller.db.alignment),
            augur=augur_str,
            strength=f'{caller.db.strength}'.rjust(2, " "),
            agility=f'{caller.db.agility}'.rjust(2, " "),
            stamina=f'{caller.db.stamina}'.rjust(2, " "),
            personality=f'{caller.db.personality}'.rjust(2, " "),
            intelligence=f'{caller.db.intelligence}'.rjust(2, " "),
            luck=f'{caller.db.luck}'.rjust(2, " "),
            max_hp=f'{caller.db.max_hp}'.rjust(2, " "),
            cur_hp=f'{caller.db.current_hp}'.rjust(2, " "),
            languages=languages,
            ac=f'{caller.db.ac}'.rjust(2, " "),
            gold=f'{caller.db.gold}'.rjust(3, " "),
            silver=f'{caller.db.silver}'.rjust(3, " "),
            copper=f'{caller.db.copper}'.rjust(3, " "),
        ))


class CmdModifiers(Command):
    key = "modifiers"

    def func(self):
        caller = self.caller

        modifiers_sheet = """
+--------------------------------------------------------
| Str  : {strength} {str_effect}
| Agi  : {agility} {agi_effect}
| Stam : {stamina} {stam_effect}
| Pers : {personality} {pers_effect}
| Int  : {intelligence}
| Luck : {luck}
{calamaties}
{known_effects}
"""
        augur_effect = "No effect."

        calamaties = "+--------------------------------------------------------"
        has_calamaties = False
        if caller.db.strength <= 5:
            calamaties += "\n| You can only hold a weapon or a shield, not both."
            has_calamaties = True

        if caller.db.stamina <= 5:
            calamaties += "\n| You take double damage from poisons and diseases."
            has_calamaties = True

        if caller.db.intelligence <= 7:
            calamaties += "\n| You can only speak Common."
            has_calamaties = True

        if caller.db.intelligence <= 5:
            calamaties += "\n| You cannot read or write."
            has_calamaties = True

        if has_calamaties:
            calamaties += "\n+--------------------------------------------------------"

        effects = "| Effects:"
        has_effects = False

        if len(caller.db.auras) > 0:
            for a in caller.db.auras:
                if not a.db.hidden and a.db.known_effects:
                    effects += f'\n| {a.key}: {a.db.modifier_description}'
                    has_effects = True

        if has_effects:
            effects += "\n+--------------------------------------------------------"

        str_modifier = calculate_ability_modifier(caller.db.strength)
        str_effect = "to melee atk/dmg rolls."

        agi_modifier = calculate_ability_modifier(caller.db.agility)
        agi_effect = "to AC, ranged atk, initiative, reflex save"

        stam_modifier = calculate_ability_modifier(caller.db.stamina)
        stam_effect = "to max HP, fortitude save"

        pers_modifier = calculate_ability_modifier(caller.db.personality)
        pers_effect = "to willpower save"

        int_modifier = calculate_ability_modifier(caller.db.intelligence)
        luck_modifier = calculate_ability_modifier(caller.db.luck)

        caller.msg(modifiers_sheet.format(
            strength=f'{str_modifier}'.rjust(2, " "),
            agility=f'{agi_modifier}'.rjust(2, " "),
            stamina=f'{stam_modifier}'.rjust(2, " "),
            personality=f'{pers_modifier}'.rjust(2, " "),
            intelligence=f'{int_modifier}'.rjust(2, " "),
            luck=f'{luck_modifier}'.rjust(2, " "),
            str_effect=str_effect,
            agi_effect=agi_effect,
            stam_effect=stam_effect,
            pers_effect=pers_effect,
            augur_effect=augur_effect,
            calamaties=calamaties,
            known_effects=effects
        ))


class CmdEquipment(Command):
    """
    view equipment

    Usage:
      equipment
      equip

    Shows your equipment.
    """
    key = "equipment"
    aliases = ["equip"]
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        items = caller.contents
        if not items:
            string = "You are not wearing anything."
        else:
            table = self.styled_table(border="header")
            worn_items = {}
            for item in items:
                if item.attributes.has("current_worn_location"):
                    if item.is_currently_worn():
                        if item.db.current_worn_location not in worn_items:
                            worn_items[item.db.current_worn_location] = []

                        worn_items[item.db.current_worn_location].append(
                            item
                        )

            for i in range(3, 16):
                if WearLocation(i) in worn_items:
                    for item in worn_items[WearLocation(i)]:
                        table.add_row(
                            "[{}]".format(str(WearLocation(i))),
                            "{}|n".format(
                                utils.crop(raw_ansi(item.name), width=50)
                            ),
                        )

            string = f"|wYou are wearing:\n{table}"

        caller.msg(string)
