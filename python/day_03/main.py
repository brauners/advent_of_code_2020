#!/usr/bin/python3

from collections import namedtuple
from functools import reduce


"""
Convention:
origin -> top left
x-direction -> to the right
y-direction -> down
"""

Vector = namedtuple('Vector', ['x', 'y'])

def add(v1: Vector, v2: Vector):
    return Vector(v1.x + v2.x, v1.y + v2.y)

def cell_is_occupied(grid, vector):
    occupied_char = "#"
    return grid[vector.y][vector.x] == occupied_char

def to_grid_vector(vector, grid):
    """
    grid repeats horizontally
    return None of vector exceeds grid size
    """
    grid_width = len(grid[0])
    grid_height = len(grid)
    if vector.y >= grid_height:
        return None
    return Vector(vector.x % grid_width, vector.y)


if __name__ == "__main__":
    with open("input") as fp:
        grid = fp.read().split()
    
    s1 = Vector(1, 1)
    s2 = Vector(3, 1)
    s3 = Vector(5, 1)
    s4 = Vector(7, 1)
    s5 = Vector(1, 2)
    slopes = [s1, s2, s3, s4, s5]

    tree_counts = []
    for slope in slopes:
        world_pos = Vector(0,0)
        tree_count = 0

        while True:
            grid_pos = to_grid_vector(world_pos, grid)
            if grid_pos is None:
                break
            tree_count += int(cell_is_occupied(grid, grid_pos))
            world_pos = add(world_pos, slope)
        
        tree_counts.append(tree_count)

    print(f"Trees counted: {tree_counts}")
    print(f"Multiplied: {reduce((lambda x, y: x * y), tree_counts)}")