import re
from collections import defaultdict

def parse_bag_description(string):
    string = string.replace(".", "").replace(" ", "")
    string = string.replace("bags", "").replace("bag", "")
    string = re.sub(r"\d+", "", string)
    description = string.split("contain")

    outer = description[0]
    inner = description[1].split(",")

    return {"outer": outer, "inner": inner}


if __name__ == "__main__":
    input_filename = "day_07/input"
    #input_filename = "day_07/input_debug"
    with open(input_filename) as fp:
        input_data = fp.read().split("\n")

    bag_descriptions = [parse_bag_description(line) for line in input_data]

    l = set()
    l.add("shinygold")
    while True:
        new_l = set(l)
        for c in l:
            for bag in bag_descriptions:
                if c in bag["inner"]:
                    new_l.add(bag["outer"])
        if new_l == l:
            break
        l = new_l

    print(f"Number of colors that eventually can contain mine: {len(l)-1}")
    
    pass
