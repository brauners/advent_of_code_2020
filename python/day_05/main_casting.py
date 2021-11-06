import re

def convert_to_int(code):
    code = re.sub("[FL]", "0", code)
    code = re.sub("[BR]", "1", code)
    return int(code, 2)


if __name__ == "__main__":
    with open("day_05/input_debug") as fp:
        seat_codes = fp.read().split()
    
    seat_ids = [convert_to_int(seat_code) for seat_code in seat_codes]
    
    print(f"Highest seat id is: {max(seat_ids)}")
