#!/usr/bin/python3

from copy import deepcopy
from collections import namedtuple

"""
Convention:
origin -> top left
x-direction -> to the right
y-direction -> down
"""

legend = {"empty": "L", "occupied": "#", "floor": "."}

Vector = namedtuple("Vector", ["x", "y"])

neighbour_coordinates = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def sum_vectors(v1: Vector, v2: Vector):
    return Vector(v1.x + v2.x, v1.y + v2.y)


def print_grid(grid):
    for row in grid:
        print(row)
    print()


def count_occupied(grid):
    count = 0
    for row in grid:
        count += row.count(legend["occupied"])
    return count


def is_vector_on_grid(grid, vector):
    grid_width = len(grid[0])
    grid_height = len(grid)

    return (
        vector.x >= 0
        and vector.x < grid_width
        and vector.y >= 0
        and vector.y < grid_height
    )


def get_neighbour_values(grid, x, y):

    neighbour_values = []

    for neighbour_coo in neighbour_coordinates:
        neighbour = sum_vectors(Vector(x, y), Vector(*neighbour_coo))
        if is_vector_on_grid(grid, neighbour):
            neighbour_values.append(grid[neighbour.y][neighbour.x])

    return neighbour_values


def rules(current, neighbour_count):
    if current == legend["empty"] and neighbour_count == 0:
        return legend["occupied"]
    if current == legend["occupied"] and neighbour_count >= 4:
        return legend["empty"]
    return current


def generate_neighbour_count_grid(grid):
    neighbour_count_grid = deepcopy(grid)

    for x, _ in enumerate(grid[0]):
        for y, _ in enumerate(grid):
            neighbour_values = get_neighbour_values(grid, x, y)
            neighbour_count_grid[y][x] = neighbour_values.count(legend["occupied"])

    return neighbour_count_grid


def generate_next_grid(grid):
    new_grid = deepcopy(grid)
    neighbour_count_grid = generate_neighbour_count_grid(grid)
    change = False
    for x, _ in enumerate(grid[0]):
        for y, _ in enumerate(grid):
            new_value = rules(grid[y][x], neighbour_count_grid[y][x])
            change = change or new_value != grid[y][x]
            new_grid[y][x] = new_value
    return new_grid, change


if __name__ == "__main__":
    input_filename = "day_11/input"
    # input_filename = "day_11/input_debug"
    with open(input_filename) as fp:
        grid = [list(x.strip()) for x in fp.readlines()]

    # print_grid(grid)

    while True:
        next_grid, change_happened = generate_next_grid(grid)

        # print_grid(next_grid)

        if not change_happened:
            break

        grid = deepcopy(next_grid)

    # print_grid(grid)
    print(count_occupied(grid))
