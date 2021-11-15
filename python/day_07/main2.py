import re

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