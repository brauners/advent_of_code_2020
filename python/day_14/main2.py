import re
import itertools


def replace_all(string, char, replacements):
    """Replace all occurences of char in string with the elements from replacements"""
    ret = []
    replacements = list(replacements)
    for c in string:
        ret.append(c if c != char else replacements.pop())
    return "".join(ret)


def possible_masks(mask):
    x_count = mask.count("X")
    for permutation in itertools.product("01", repeat=x_count):
        possible_mask = replace_all(mask, "X", permutation)
        yield possible_mask


def overwrite_bitwise(op1, op2, overwrite_mask):
    # Create a perfect inversion, disregard signs
    inverted_overwrite_mask = ~overwrite_mask & 2 ** 36 - 1
    # Set all the bits to 0 that will be overwritten
    value = op1 & inverted_overwrite_mask
    # Set the 1 bits
    value += op2

    return value


REGEX = r"((mask = (?P<mask>[X10]*))|(mem\[(?P<address>\d*)\] = (?P<value>\d*)))"


if __name__ == "__main__":
    input_filename = "day_14/input"
    # input_filename = "day_14/input_debug_2"

    with open(input_filename) as fp:
        data = fp.read().splitlines()

    mask = ""
    masks = []
    mem = {}
    for line in data:
        m = re.match(REGEX, line)

        if m.group("mask") is not None:
            mask = m.group("mask")

        if m.group("address") is not None:
            address = int(m.group("address"))
            value = int(m.group("value"))

            overwrite_mask = int(mask.replace("X", "1"), 2)

            for possible_mask in possible_masks(mask):
                # overwrite_mask = int(possible_mask.replace("X", "1"), 2)
                possible_mask = int(possible_mask, 2)
                possible_address = overwrite_bitwise(
                    address, possible_mask, overwrite_mask
                )
                mem[possible_address] = value
            pass

    print(f"Sum of values in memory: {sum(mem.values())}")
