
def find_last_index(iterable, value):
    try:
        index = len(iterable) - 1 - iterable[::-1].index(value)
    except ValueError:
        return None
    return index


if __name__ == "__main__":
    input_filename = "day_15/input"
    # input_filename = "day_15/input_debug"
    with open(input_filename) as fp:
        s = fp.readline()
        numbers = [int(x) for x in s.split(",")]
 
    MAX_TURNS = 202000
    MAX_TURNS = 30000000

    for turn in range(len(numbers) + 1, MAX_TURNS + 1):
        recent = numbers[-1]
        index = find_last_index(numbers[:-1], recent)

        if index is None:
            numbers.append(0)
        else:
            last_spoken = turn - 1
            most_recently_spoken = index + 1
            numbers.append(last_spoken - most_recently_spoken)
        pass
    
    print(f"{turn}th number spoken: {numbers[-1]}")
