if __name__ == "__main__":
    with open("test_13.in") as f:
        input = [x.strip() for x in f.readlines()]

    buses = input[1].split(',')

    time = 0
    found = False
    while not found:
        t = time
        for bus in buses:
            if t % int(bus) == 0:
                t += 1