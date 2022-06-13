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
Point = namedtuple("Point", ["x", "y"])


def cart_to_pol(x, y):
    rho = math.sqrt(x ** 2 + y ** 2)
    phi = math.atan2(y, x)
    return (rho, math.degrees(phi))


def pol_to_cart(rho, phi):
    x = rho * math.cos(phi)
    y = rho * math.sin(phi)
    return (x, y)


def move_in_world(instruction, pos_ship, pos_waypoint):
    x, y = pos_ship
    wx, wy = pos_waypoint

    direction, value = instruction

    if direction == "N":
        wx, wy = wx, wy + value

    elif direction == "E":
        wx, wy = wx + value, wy

    elif direction == "S":
        wx, wy = wx, wy - value

    elif direction == "W":
        wx, wy = wx - value, wy

    elif direction == "F":
        dx = wx - x
        dy = wy - y
        x = x + dx * value
        y = y + dy * value
        wx = x + dx
        wy = y + dy

    elif direction == "R":
        # rotate the waypoint around the ship right
        rho, phi = cart_to_pol(wx - x, wy - y)
        phi = phi - value
        dx, dy = pol_to_cart(rho, math.radians(phi))
        wx = x + dx
        wy = y + dy

    elif direction == "L":
        # rotate the waypoint around the ship left
        rho, phi = cart_to_pol(wx - x, wy - y)
        phi = phi + value
        dx, dy = pol_to_cart(rho, math.radians(phi))
        wx = x + dx
        wy = y + dy

    return Point(x, y), Point(wx, wy)


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

    start_pos_ship = Point(0, 0)
    current_pos_ship = start_pos_ship

    pos_waypoint = Point(10, 1)

    for instruction in instructions:
        current_pos_ship, pos_waypoint = move_in_world(
            instruction, current_pos_ship, pos_waypoint
        )

    distance = manhattan_distance(
        start_pos_ship.x, start_pos_ship.y, current_pos_ship.x, current_pos_ship.y
    )
    print(distance)
