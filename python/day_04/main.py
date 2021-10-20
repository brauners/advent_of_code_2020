#!/usr/bin/python3
from configparser import ConfigParser
import re


def moddify_input_string(string):
    string = string.replace(" ", "\n").replace(":", ": ")
    return string

def chunk_to_passport(chunk):
    chunk = "[passport]\n" + chunk
    passport = ConfigParser()
    passport.read_string(chunk)
    return passport["passport"]

def is_valid_passport(passport):
    
    def is_6_digit_hex(s):
        if not s.startswith("#"):
            return False
        s = s.replace("#", "")
        try:
            int(s, 16)
        except ValueError:
            return False
        return len(s) == 6
    
    def is_valid_height(string):
        valid = False
        if "cm" in string:
            value = int(string.replace("cm", ""))
            valid = 150 <= value <=193
        if "in" in string:
            value = int(string.replace("in", ""))
            valid = 59 <= value <= 76
        return valid

    rules = {
        "byr": lambda s: 1920 <= int(s) <= 2002,
        "iyr": lambda s: 2010 <= int(s) <= 2020,
        "eyr": lambda s: 2020 <= int(s) <= 2030,
        "hgt": lambda s: is_valid_height(s),
        "hcl": lambda s: is_6_digit_hex(s),
        "ecl": lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda s: bool(re.fullmatch(r"\d{9}", s))
    }
    optional = ["cid"]

    valid = True
    for tag, rule in rules.items():
        valid = valid and tag in passport and rule(passport[tag])
    return valid


if __name__ == "__main__":
    with open("input") as fp:
        input_string = fp.read()

    string = moddify_input_string(input_string)

    valid_passport_count = 0
    for chunk in string.split("\n\n"):
        passport = chunk_to_passport(chunk)
        valid_passport_count += int(is_valid_passport(passport))

    with open("input_mod", "w") as fp:
        fp.write(string)
    
    print(f"Found valid passports: {valid_passport_count}")
