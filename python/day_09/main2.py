def has_pair_for_target_sum(numbers, target_sum):
    seen = set()
    for n in numbers:
        required = target_sum - n
        if required in seen:
            return True
        seen.add(n)
    return False


def find_invalid_number(data, length_preamble):
    for i in range(length_preamble, len(data)):
        current_number = data[i]
        preamble = data[i - length_preamble : i]
        if not has_pair_for_target_sum(preamble, current_number):
            return current_number
    return None


def find_contiguous_set_for_target_sum(numbers, target_sum):
    for idx, _ in enumerate(numbers):
        for j in range(idx + 2, len(numbers)):
            current_numbers = numbers[idx : j]
            if sum(current_numbers) == target_sum:
                return current_numbers
            if sum(current_numbers) > target_sum:
                break
    return []


if __name__ == "__main__":
    input_filename = "day_09/input"
    # input_filename = "day_09/input_debug"
    with open(input_filename) as fp:
        data = [int(l) for l in fp.read().split()]

    # Find the number which does not have a pair in front of it
    # that sums to that number
    length_preamble = 25
    invalid_number = find_invalid_number(data, length_preamble)

    # Find contiguous set of at least two numbers that sum to invalid_number
    continuous_set = find_contiguous_set_for_target_sum(data, invalid_number)
    
    encryption_weakness = min(continuous_set) + max(continuous_set)

    print(continuous_set)
    print(f"Encryption weakness: {encryption_weakness}")
