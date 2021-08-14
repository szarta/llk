#!/usr/bin/env python3
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
import sys
import argparse
import logging
import glob
import yaml

__version__ = "%(prog)s 1.0.0 (Rel: 13 Aug 2021)"
default_log_format = "%(filename)s:%(levelname)s:%(asctime)s] %(message)s"


def load_yaml(filepath):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

    return None


def get_prototype_header():
    header = '''"""
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
from world.definitions.itemdefs import FillLevel
from world.definitions.itemdefs import MaterialType
from world.definitions.itemdefs import WearLocation
from world.definitions.light import LightGenerationType
from world.definitions.chardefs import Language


'''
    return header


material_mapping = {
    "wood": "MaterialType.Wood",
    "wooden": "MaterialType.Wood",
    "steel": "MaterialType.Steel",
    "clay": "MaterialType.Clay",
    "ivory": "MaterialType.Ivory",
    "iron": "MaterialType.Iron",
    "wax": "MaterialType.Wax",
    "parchment paper": "MaterialType.ParchmentPaper",
    "hemp": "MaterialType.Hemp",
    "linen": "MaterialType.Linen",
    "mithril": "MaterialType.Mithril",
    "burlap": "MaterialType.Burlap",
    "leather": "MaterialType.Leather",
    "glass": "MaterialType.Glass",
    "ruby": "MaterialType.Ruby",
    "hide": "MaterialType.Hide",
    "bronze": "MaterialType.Bronze",
    "silk": "MaterialType.Silk",
    "cotton": "MaterialType.Cotton",
    "wool": "MaterialType.Wool",
    "woolen": "MaterialType.Wool",
    "flannel": "MaterialType.Flannel",
    "gold": "MaterialType.Gold",
    "glass": "MaterialType.Glass",
    "denim": "MaterialType.Denim"
}

language_mapping = {
    "dragon": "Language.Dragon",
    "elf": "Language.Elf"
}

wearloc_mapping = {
    "held": "WearLocation.Held",
    "legs": "WearLocation.Legs",
    "arms": "WearLocation.Arms",
    "torso": "WearLocation.Torso",
    "head": "WearLocation.Head",
    "neck": "WearLocation.Neck",
    "feet": "WearLocation.Feet",
    "body": "WearLocation.Body",
    "shoulders": "WearLocation.Shoulders",
    "hands": "WearLocation.Hands",
    "waist": "WearLocation.Waist",
    "fingers": "WearLocation.Fingers",
    "back": "WearLocation.Back"
}

fill_mapping = {
    "full": "FillLevel.Full",
    "empty": "FillLevel.Empty"
}

light_mapping = {
    "weak-ambient": "LightGenerationType.WeakAmbientLight",
    "average-ambient": "LightGenerationType.AverageAmbientLight"
}


def get_translated_wear_locations(wearloc_list):
    ret = ""
    for loc in wearloc_list:
        actual_loc = wearloc_mapping[loc]
        ret += f'        {actual_loc},\n'

    ret = ret.rstrip().rstrip(",")
    ret += '\n'
    return ret


def get_translated_key(element):
    # for now we only have <material /> as a replacement target
    # could have more later
    actual_key = element["key"]

    if "material" in element:
        actual_key = actual_key.replace(
            "<material />", element["material"]
        )

    return actual_key


def get_indefinite_article(word):
    lower_word = word.lower()

    an_exceptions = [
        "honest",
        "honorable"
    ]

    a_exceptions = [
        "union",
        "united",
        "unicorn",
        "used",
        "one"
    ]

    # could already have article attached
    if lower_word not in ["an", "the", "a"]:
        if lower_word[0] in ['a', 'e', 'i', 'o', 'u']:
            # probably an, check for an_exceptions
            if lower_word not in an_exceptions:
                return "an"
        else:
            # probably a, check for a exceptions
            if lower_word not in a_exceptions:
                return "a"
    else:
        return word


def get_generated_desc(element):
    actual_desc = get_translated_key(element)

    first_word = actual_desc.split(" ")[0]
    prefix = get_indefinite_article(first_word).title()

    actual_desc = f'{prefix} {actual_desc}.'
    return actual_desc


def get_translated_desc(element):
    actual_desc = ""

    if "desc" in element:
        if "material" in element:
            actual_desc = element["desc"].replace(
                "<material />", element["material"]
            )
        else:
            actual_desc = element["desc"]

    else:
        actual_desc = get_generated_desc(element)

    return actual_desc


def get_element_string(element):
    translated_key = get_translated_key(element)
    typeclass = element["base"]
    element_string = f'    "typeclass": "{typeclass}",\n'
    element_string += f'    "key": "{translated_key}",\n'

    if "material" in element:
        actual_material = material_mapping[element["material"]]
        element_string += f'    "material": {actual_material},\n'

    desc = get_translated_desc(element)
    element_string += f'    "desc": "{desc}",\n'

    if "props" in element:
        for prop in element["props"].keys():
            actual_prop = prop.replace("-", "_")
            val = element["props"][prop]
            if prop == "fill-level":
                level = fill_mapping[val]
                element_string += f'    "{actual_prop}": {level},\n'
            elif prop == "possible-wear-locations":
                element_string += f'    "{actual_prop}": [\n'
                element_string += get_translated_wear_locations(val)
                element_string += '    ]\n'
            elif prop == "light-type":
                light_level = light_mapping[val]
                element_string += f'    "{actual_prop}": {light_level},\n'
            elif prop == "language":
                lang = language_mapping[val]
                element_string += f'    "{actual_prop}": {lang},\n'
            else:
                if f'{val}'.isnumeric():
                    element_string += f'    "{actual_prop}": {val},\n'
                else:
                    element_string += f'    "{actual_prop}": "{val}",\n'

    element_string = element_string.rstrip().rstrip(",")
    element_string += '\n'
    return element_string


def gather_and_write_prototypes(proto_yaml_dir, proto_output_dir):

    prototype_types = [
        "containers",
        "implements",
        "misc",
        "food",
        "armor",
        "clothes",
        "weapons"
    ]

    prototypes = {}
    for t in prototype_types:
        prototypes[t] = []

    # Step 1: Gather prototypes
    for proto_file in glob.glob(f'{proto_yaml_dir}/*.yml'):
        y = load_yaml(proto_file)
        for t in prototype_types:
            if t in y:
                for element in y[t]:
                    prototypes[t].append(element)

    # Step 2: Validate prototypes

    # Step 3: Write prototypes
    for t in prototype_types:
        if t in prototypes:
            with open(f'{proto_output_dir}/{t}.py', "w") as f:
                f.write(get_prototype_header())
                for element in prototypes[t]:
                    logging.debug(f'Parsing {element["name"]}')
                    f.write(f'{element["name"]}' + " = {\n")
                    f.write(get_element_string(element))
                    f.write("}\n\n")


def main(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")

    parser.add_argument("--version", action="version", version=__version__,
                        help="show the version and exit")

    args = parser.parse_args()

    logging.basicConfig(format=default_log_format)
    if(args.verbose):
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    prototype_yaml_path = "definitions/generators/prototypes/"
    prototype_output_path = "prototypes/"

    gather_and_write_prototypes(prototype_yaml_path, prototype_output_path)


if __name__ == "__main__":
    main(sys.argv[1:])
