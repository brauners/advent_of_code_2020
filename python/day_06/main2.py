from collections import defaultdict

def func(arg):
    pass

if __name__ == "__main__":
    input_filename = "day_06/input"
    #input_filename = "day_06/input_debug"
    
    with open(input_filename) as fp:
        groups = fp.read().split("\n\n")

    sum_of_yes_answers = 0
    for group in groups:
        group = group.split("\n")
        group_answers = defaultdict(int)
        group_size = len(group)
        for person in group:
            for answer in person:
                group_answers[answer] += 1

        for answer, count in group_answers.items():
            if count == group_size:
                sum_of_yes_answers += 1
 
    print(f"The sum is: {sum_of_yes_answers}")
