
def func(arg):
    pass

if __name__ == "__main__":
    input_filename = "day_06/input"
    input_filename = "day_06/input_debug"
    
    with open(input_filename) as fp:
        groups = fp.read().split("\n\n")

    sum_of_yes_answers = 0
    for group in groups:
        group_answers = set(iter(group.replace("\n", "")))
        sum_of_yes_answers += len(group_answers)
    
    print(f"The sum is: {sum_of_yes_answers}")
