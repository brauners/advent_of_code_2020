def find_pair_set(numbers, target_sum):
    """ O(n) """
    seen = set()
    for n in numbers:
        if target_sum - n in seen:
            return (n, target_sum - n)
        seen.add(n)
    return None


def find_triplet_naive(numbers, target_sum):
    """ Complexity O(n^3) """
    for _i, a in enumerate(numbers):
        i = _i + 1
        for _j, b in enumerate(numbers[i:]):
            j = i + _j + 1
            for c in numbers[j:]:
                if a + b + c == target_sum:
                    return (a, b, c)
    return None


def find_triplet(numbers, target_sum):
    """ O(n^2) """
    for _i, n in enumerate(numbers):
        current_target = target_sum - n
        i = _i + 1
        if found := find_pair_set(numbers[i:], current_target):
            return (n, *found)


if __name__ == "__main__":
    with open("day_01/input", "r") as fp:
        expenses = [int(x) for x in fp.readlines()]

    target_sum = 2020
    found = find_triplet_naive(expenses, target_sum)

    if found is not None:
        print(f"Triplet found is {found[0]} and {found[1]} and {found[2]}")
        print(f"Solution to puzzle is: {found[0] * found[1] * found[2]}")
    else:
        print("No solution found.")
