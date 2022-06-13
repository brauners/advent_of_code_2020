def find_pair_summing_naive(numbers, target_sum):
    """ Complexity O(n^2) """
    for i, n1 in enumerate(numbers):
        j = i + 1
        for n2 in numbers[j:]:
            if n1 + n2 == target_sum:
                return (n1, n2)
    return None


def find_pair_set(numbers, target_sum):
    """ O(n) """
    seen = set()
    for n in numbers:
        required = target_sum - n
        if required in seen:
            return (n, required)
        seen.add(n)
    return None


if __name__ == "__main__":
    with open("day_01/input", "r") as fp:
        expenses = [int(x) for x in fp.readlines()]

    target_sum = 2020
    # found = find_pair_summing_naive(expenses, target_sum)
    found =  find_pair_set(expenses, target_sum)

    print(f"Pair found is {found[0]} and {found[1]}")
    print(f"Solution to puzzle is: {found[0] * found[1]}")
