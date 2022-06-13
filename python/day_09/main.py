def has_pair_for_target_sum(numbers, target_sum):
    seen = set()
    for n in numbers:
        required = target_sum - n
        if required in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    input_filename = "day_09/input"
    # input_filename = "day_09/input_debug"
    with open(input_filename) as fp:
        input_data = [int(l) for l in fp.read().split()]

    len_preamble = 25

    for i in range(len_preamble, len(input_data)):
        current_number = input_data[i]
        preamble = input_data[i - len_preamble : i]
        if not has_pair_for_target_sum(preamble, current_number):
            print(f"{current_number} is not correct.")
            break
