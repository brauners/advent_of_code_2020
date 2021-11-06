import re

bin_values = {"F": 0, "B": 1, "R": 1, "L": 0}


def decode(code):
    if not code:
        return 0
    exponent = len(code) - 1
    head, tail = code[0], code[1:]
    digit = bin_values[head]
    value = digit * 2**exponent
    return value + decode(tail)


if __name__ == "__main__":
    with open("day_05/input_debug") as fp:
        seat_codes = fp.read().split()

    seat_ids = []
    for seat_code in seat_codes:
        row = decode(seat_code[:7])
        col = decode(seat_code[7:])
        seat_id = row * 8 + col
        seat_ids.append(seat_id)

    
    print(f"Highest seat id is: {max(seat_ids)}")
