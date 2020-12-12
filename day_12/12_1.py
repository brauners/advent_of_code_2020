
import math
#           N
#           y
#           |
#           |
#           |
# W ------------------- x E
#           |
#           |
#           |
#           S



def move_in_world(a, b, current_pose):
    x, y, h = current_pose

    if a == "N":
        return (x, y + b, h)
    elif a == "E":
        return (x + b, y, h)
    elif a == "S":
        return (x, y - b, h)
    elif a == "W":
        return (x - b, y, h)
    elif a == "F":
        dx = round(math.cos(math.radians(h))) * b
        dy = round(math.sin(math.radians(h))) * b
        return (x + dx, y + dy, h)
    elif a == "R":
        return (x, y, (h - b)%360)
    elif a == "L":
        return (x, y, (h + b)%360)

def manhattan(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return dx + dy


if __name__ == "__main__":
    with open("12.in") as f:
        input = [x.strip() for x in f.readlines()]

    start_pose = (0, 0, 0)
    pose = start_pose

    for i in input:
        d, v = i[0], int(i[1:])
        pose = move_in_world(d, v, pose)
    
    print(manhattan(start_pose[0], start_pose[1], pose[0], pose[1]))
