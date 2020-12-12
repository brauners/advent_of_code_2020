

if __name__ == "__main__":
    with open("10_test.in") as f:
        jolts = [int(x.strip()) for x in f.readlines()]

    jolts.sort()

    last_jolt = max(jolts) + 3

    combinations = [0]

    for j in jolts:
        tmp = []
        for c in combinations:
            if j - c < 4:
                tmp.append(j)
                tmp.append(c)
        combinations = tmp.copy()

    tmp = []
    for c in combinations:
        if last_jolt - c < 4:
            tmp.append(last_jolt)
    combinations = tmp.copy()




    print(len(combinations))
