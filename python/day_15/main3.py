

# start_numbers = parse_input("advent_of_code/2020/advent_of_code_day15/input.txt")
start_numbers = [1,20,8,12,0,14]
numbers_spoken = {number: i + 1 for i, number in enumerate(start_numbers[:-1])}

last_spoken_number = start_numbers[-1]
for i in range(len(start_numbers), 30000000):
    try:
        number_to_speak = i - numbers_spoken[last_spoken_number]
    except KeyError:
        number_to_speak = 0

    numbers_spoken[last_spoken_number] = i
    last_spoken_number = number_to_speak

print(f"Part 2: {last_spoken_number}")