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
from evennia import Command
from evennia.utils.ansi import raw as raw_ansi
from evennia.utils import utils

from world.definitions.itemdefs import WearLocation
from typeclasses.characters import calculate_ability_modifier


class CmdInventory(Command):
    """
    view inventory

    Usage:
      inventory
      inv

    Shows your inventory.
    """

    key = "inventory"
    aliases = ["inv", "i"]
    locks = "cmd:all()"
    arg_regex = r"$"

    def func(self):
        """check inventory"""
        items = self.caller.contents
        if not items:
            string = "You are not carrying anything."
        else:
            from evennia.utils.ansi import raw as raw_ansi

            table = self.styled_table(border="header")
            for item in items:
                if item.attributes.has("current_worn_location"):
                    if item.is_currently_worn():
                        # do not display messages as being in inventory if they
                        # are being worn
                        continue

                if item in self.caller.db.auras:
                    # ignore auras
                    continue

                table.add_row(
                    f"|C{item.name}|n",
                    "{}|n".format(
                        utils.crop(raw_ansi(item.db.desc), width=50) or ""
                    ),
                )
            string = f"|wYou are carrying:\n{table}"
        self.caller.msg(string)


class CmdSheet(Command):
    key = "sheet"

    def func(self):
        caller = self.caller
        stat_sheet = """
+--------------------------------------------------------
| Name: {name}
| Age: {age}, Race: {race}, Gender: {gender}
| Birth Augur: {augur}
| Occupation: {occupation}
| Alignment: {align}
| Wealth: {gold}gp, {silver}sp, {copper}cp
| Level: {level}, XP: {xp}
+--------------------------------------------------------
| Str  : {strength}  |  HP : {cur_hp} (max: {max_hp})
| Agi  : {agility}  |  AC : {ac}
| Stam : {stamina}  |  Speed : {speed}
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
            lang_str = lang.display_name
            lang_len = len(lang_str)
            line_length = 52
            if first_line:
                line_length = 40

            if (len(current_line) + lang_len) > line_length:
                if first_line:
                    first_line = False

                languages += current_line.rstrip().rstrip(",")
                current_line = "\n|   "

            current_line = f'{current_line}{lang_str}, '

        languages += current_line.rstrip().rstrip(",")

        augur_str = caller.db.birth_augur.display_name[1]
        modified_strength = caller.get_modified_strength()
        modified_agility = caller.get_modified_agility()
        modified_stamina = caller.get_modified_stamina()
        modified_personality = caller.get_modified_personality()
        modified_intelligence = caller.get_modified_intelligence()
        modified_luck = caller.get_modified_luck()
        modified_speed = caller.get_modified_speed()
        modified_hp = caller.get_modified_hp()
        modified_ac = caller.get_modified_ac()

        caller.msg(stat_sheet.format(
            name=caller.name,
            age=caller.db.age,
            race=caller.db.race.display_name,
            level=caller.db.level,
            xp=caller.db.xp,
            gender=caller.db.gender,
            occupation=caller.db.occupation.display_name,
            align=caller.db.alignment.display_name,
            augur=augur_str,
            strength=f'{modified_strength}'.rjust(2, " "),
            agility=f'{modified_agility}'.rjust(2, " "),
            stamina=f'{modified_stamina}'.rjust(2, " "),
            personality=f'{modified_personality}'.rjust(2, " "),
            intelligence=f'{modified_intelligence}'.rjust(2, " "),
            luck=f'{modified_luck}'.rjust(2, " "),
            max_hp=f'{modified_hp}'.rjust(2, " "),
            cur_hp=f'{caller.db.current_hp}'.rjust(2, " "),
            languages=languages,
            ac=f'{modified_ac}'.rjust(2, " "),
            gold=f'{caller.db.gold}'.rjust(3, " "),
            silver=f'{caller.db.silver}'.rjust(3, " "),
            copper=f'{caller.db.copper}'.rjust(3, " "),
            speed=f'{modified_speed}'.rjust(2, " ")
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

        calamaties = \
            "+--------------------------------------------------------"

        has_calamaties = False
        if caller.db.strength <= 5:
            calamaties += \
                "\n| You can only hold a weapon or a shield, not both."

            has_calamaties = True

        if caller.db.stamina <= 5:
            calamaties += \
                "\n| You take double damage from poisons and diseases."

            has_calamaties = True

        if caller.db.intelligence <= 7:
            calamaties += "\n| You can only speak Common."
            has_calamaties = True

        if caller.db.intelligence <= 5:
            calamaties += "\n| You cannot read or write."
            has_calamaties = True

        if has_calamaties:
            calamaties += \
                "\n+--------------------------------------------------------"

        effects = "| Effects:"
        has_effects = False

        if len(caller.db.auras) > 0:
            for a in caller.db.auras:
                if not a.db.hidden and a.db.known_effects:
                    effects += f'\n| {a.key}: {a.db.modifier_description}'
                    has_effects = True

        if has_effects:
            effects += \
                "\n+--------------------------------------------------------"
        else:
            effects += "\n| None"
            effects += \
                "\n+--------------------------------------------------------"

        str_modifier = calculate_ability_modifier(caller.db.strength)
        str_effect = "to melee atk/dmg rolls"

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

            wearlocs = list(WearLocation)
            for loc in wearlocs:
                if loc in worn_items:
                    for item in worn_items[loc]:
                        table.add_row(
                            "[{}]".format(loc.display_name),
                            "{}|n".format(
                                utils.crop(raw_ansi(item.name), width=50)
                            ),
                        )

            string = f"|wYou are wearing:\n{table}"

        caller.msg(string)
