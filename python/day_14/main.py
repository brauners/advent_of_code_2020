import re

# def change_value(value, mask):
#     value = format(value, "036b")
#     new_value = []
#     for v, m in zip(value, mask):
#         if m in "01":
#             new_value.append(m)
#         else:
#             new_value.append(v)

#     return int("".join(new_value), 2)


REGEX = r"((mask = (?P<mask>[X10]*))|(mem\[(?P<address>\d*)\] = (?P<value>\d*)))"


def overwrite_bitwise(op1, op2, overwrite_mask):
    # Create a perfect inversion, disregard signs
    inverted_overwrite_mask = ~overwrite_mask & 2**36-1   1010 0101
    # Set all the bits to 0 that will be overwritten
    value = op1 & inverted_overwrite_mask
    # Set the 1 bits
    value += op2

    return value


if __name__ == "__main__":
    input_filename = "day_14/input"
    # input_filename = "day_14/input_debug"

    with open(input_filename) as fp:
        data = fp.read().splitlines()

    mask = ""
    mem = {}
    for line in data:
        m = re.match(REGEX, line)

        if m.group("mask") is not None:
            mask = m.group("mask")

        if m.group("address") is not None:
            address = int(m.group("address"))
            value = int(m.group("value"))

            # Create mask where bits to overwrite are 1
            overwrite_mask = int(mask.replace("0", "1").replace("X", "0"), 2)
            cleaned_mask = int(mask.replace("X", "0"), 2)

            value = overwrite_bitwise(value, cleaned_mask, overwrite_mask)

            mem[address] = value




    print(f"Sum of values in memory: {sum(mem.values())}")