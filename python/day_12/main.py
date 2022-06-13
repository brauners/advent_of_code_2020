import math
from collections import namedtuple

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

Instruction = namedtuple("Instruction", ["dir", "val"])
Pose = namedtuple("Pose", ["x", "y", "heading"])


def move_pose(instruction, pose):
    dx, dy, dh = 0, 0, 0

    if instruction.dir == "N":
        dy = instruction.val
    elif instruction.dir == "E":
        dx = instruction.val
    elif instruction.dir == "S":
        dy = -instruction.val
    elif instruction.dir == "W":
        dx = -instruction.val
    elif instruction.dir == "F":
        dx = round(math.cos(math.radians(pose.heading))) * instruction.val
        dy = round(math.sin(math.radians(pose.heading))) * instruction.val
    elif instruction.dir == "R":
        dh = -instruction.val
    elif instruction.dir == "L":
        dh = +instruction.val

    return Pose(pose.x + dx, pose.y + dy, (pose.heading + dh) % 360)


def manhattan_distance(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return dx + dy


if __name__ == "__main__":
    input_filename = "day_12/input"
    # input_filename = "day_12/input_debug"
    with open(input_filename) as fp:
        input_data = [x.strip() for x in fp.readlines()]

    instructions = [Instruction(line[0], int(line[1:])) for line in input_data]

    start_pose = Pose(0, 0, 0)
    current_pose = start_pose

    for instruction in instructions:
        current_pose = move_pose(instruction, current_pose)
    
    distance = manhattan_distance(
        start_pose.x, start_pose.y, current_pose.x, current_pose.y
    )
    print(distance)

