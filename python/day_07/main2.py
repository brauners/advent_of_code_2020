import re


def parse_bag_description(string):
    string = string.replace(".", "").replace(" ", "")
    string = string.replace("bags", "").replace("bag", "")
    # string = re.sub(r"\d+", "", string)
    description = string.split("contain")

    outer = description[0]
    inner = description[1].split(",")

    inner_bags = []
    for bag in inner:
        match = re.match("(\d+)(.*)", bag)
        number = match[1]
        color = match[2]
        inner_bags.append({color: number})
        pass

    return outer, inner_bags


if __name__ == "__main__":
    input_filename = "day_07/input"
    # input_filename = "day_07/input_debug"
    with open(input_filename) as fp:
        input_data = fp.read().split("\n")

    bag_descriptions = {parse_bag_description(line) for line in input_data}
    pass

    bags_to_check = ["shinygold"]
    total_number = 0
    while True:
        new_bags = []
        for parent_bag in bags_to_check:
            for child_bag in bag_descriptions[parent_bag]:
                new_bags.append(child_bag.color)

