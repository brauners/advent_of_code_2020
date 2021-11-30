#!/usr/bin/python3

from collections import namedtuple
from functools import reduce

"""
Convention:
origin -> top left
x-direction -> to the right
y-direction -> down
"""

Vector = namedtuple("Vector", ["x", "y"])


def sum_vectors(v1: Vector, v2: Vector):
    return Vector(v1.x + v2.x, v1.y + v2.y)


def grid_cell_is_occupied(grid, vector):
    occupied_char = "#"
    return grid[vector.y][vector.x] == occupied_char


def world_to_grid_coordinates(vector, grid):
    """
    grid repeats horizontally
    return None if vector exceeds grid size
    """
    grid_width = len(grid[0])
    grid_height = len(grid)
    if vector.y >= grid_height:
        return None
    return Vector(vector.x % grid_width, vector.y)


if __name__ == "__main__":
    with open("day_03/input") as fp:
        grid = fp.read().split()

    s1 = Vector(1, 1)
    s2 = Vector(3, 1)
    s3 = Vector(5, 1)
    s4 = Vector(7, 1)
    s5 = Vector(1, 2)
    # slopes = [s1, s2, s3, s4, s5]
    slopes = [s2]

    tree_counts = []
    for slope in slopes:
        world_pos = Vector(0, 0)
        tree_count = 0

        while True:
            grid_pos = world_to_grid_coordinates(world_pos, grid)
            if grid_pos is None:
                break
            tree_count += int(grid_cell_is_occupied(grid, grid_pos))
            world_pos = sum_vectors(world_pos, slope)

        tree_counts.append(tree_count)

    tree_counts_multiplied = reduce((lambda x, y: x * y), tree_counts)

    print(f"Trees counted: {tree_counts}")
    print(f"Multiplied: {tree_counts_multiplied}")
