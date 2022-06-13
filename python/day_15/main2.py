


if __name__ == "__main__":
    input_filename = "day_15/input"
    # input_filename = "day_15/input_debug"
    with open(input_filename) as fp:
        s = fp.readline()
        starting_numbers = [int(x) for x in s.split(",")]
 
    MAX_TURNS = 10
    MAX_TURNS = 30000000
    

    numbers = {val: turn for turn, val in enumerate(starting_numbers[:-1], 1)}
    current = starting_numbers[-1]

    for turn in range(len(starting_numbers) + 1, MAX_TURNS + 1):
        most_recently_spoken = numbers.get(current)
        numbers[current] = turn - 1


        if most_recently_spoken is None:
            # Recent number has not been seen before
            current = 0
        else:
            last_spoken = turn - 1
            current = last_spoken - most_recently_spoken
    
    print(f"{turn}th number spoken: {current}")
