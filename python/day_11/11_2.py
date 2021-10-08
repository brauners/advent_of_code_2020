
def neighbour_coords(area, x, y, w, h):
    coords = []
    t_x = 0
    t_y = 0
    directions = [  (-1, -1), ( 0, -1), ( 1, -1),
                    (-1,  0),           ( 1,  0),
                    (-1,  1), ( 0,  1), ( 1,  1)]
    
    for d in directions:
        mag = 0
        while True:
            mag += 1
            t_x = x + d[0] * mag
            t_y = y + d[1] * mag
            # check boundaries
            if (t_x < 0 or t_y < 0) or (t_x >= w or t_y >= h): 
                break

            if area[t_y][t_x] in ["L", "#"]:
                coords.append((t_x, t_y))
                break
    return coords

def neighbours(area, x, y):
    width = len(area[0])
    height = len(area)
    coords = neighbour_coords(area, x, y, width, height)

    count = 0
    for co in coords:
        x = co[0]
        y = co[1]
        if area[y][x] == "#":
            count += 1
    return count

def diff(one, another):
    d = 0
    for r, row in enumerate(one):
        for c, col in enumerate(row):
            if not one[r][c] == another[r][c]:
                d += 1
    return d

def print_pretty(area):
    for row in area:
        print(row)

def count_occupied(area):
    count = 0
    for r, row in enumerate(area):
        for c, col in enumerate(row):
            if area[r][c] == "#":
                count += 1
    return count

if __name__ == "__main__":
    with open("11_1.in") as f:
        area = [x.strip() for x in f.readlines()]

    while True:
        next_area = []

        for y, row in enumerate(area):
            new_col = ''
            for x, col in enumerate(row):
                if area[y][x] == "L" and neighbours(area, x, y) == 0:
                    new_col += "#"
                elif area[y][x] == "#" and neighbours(area, x, y) >= 5:
                    new_col += "L"
                else:
                    new_col += area[y][x]

            next_area.append(new_col)

        print_pretty(next_area)

        print("")

        if diff(area, next_area) == 0:
            print(count_occupied(area))
            break
        area = next_area.copy()

