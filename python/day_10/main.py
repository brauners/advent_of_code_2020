from operator import sub

if __name__ == "__main__":
    input_filename = "day_10/input"
    # input_filename = "day_10/input_debug"
    with open(input_filename) as fp:
        input_data = [int(l) for l in fp.read().split()]

    jolts = sorted(input_data)

    # Add outlet and device value
    jolts = [0] + jolts + [max(jolts) + 3]

    steps = list(map(sub, jolts[1:], jolts[:-1]))

    solution = steps.count(1) * steps.count(3)
    print(
        f"Number of 1-jolt differences multiplied by the number of 3-jolt differences: {solution}"
    )

