if __name__ == "__main__":
    with open("day_10/10.in") as f:
        jolts = [int(x.strip()) for x in f.readlines()]

    jolts.sort()
    jolts.append(max(jolts) + 3)

    connections = {}
    rev_jolts = list(reversed([0] + jolts))
    
    for i, jolt in enumerate(rev_jolts):
        connects_to = []
        for next_jolt in rev_jolts[i+1::]:
            if jolt - next_jolt > 3:
                break
            connects_to.append(next_jolt)
        connections[jolt] = connects_to
        
    paths = {0 : 1}

    for j in jolts:
        paths[j] = 0
        for c in connections[j]:
            paths[j] += paths[c] 

    print(paths[jolts[-1]])