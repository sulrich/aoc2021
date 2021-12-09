#!/usr/bin/env python

import sys
import numpy as np


def load_input(infile):
    with open(infile) as f:
        lines = f.readlines()

    return lines


def bitlist_to_int(diag_list):
    return int("".join(str(x) for x in diag_list), 2)


def parse_input(input):
    input = input.strip()
    (a, b) = input.split(" -> ")
    start = tuple(int(x) for x in a.split(","))
    end = tuple(int(x) for x in b.split(","))

    return start, end


class Map:
    DIM_ROWS = 1000
    DIM_COLS = 1000

    def __init__(self) -> None:
        self.grid = np.zeros((Map.DIM_ROWS, Map.DIM_COLS), dtype=int)

    def x_update(self, start, end):
        y = start[1]
        if start[0] < end[0]:
            a = start[0]
            b = end[0]
        else:
            b = start[0]
            a = end[0]

        for x in range(a, b + 1):
            self.grid[x, y] = self.grid[x, y] + 1

    def y_update(self, start, end):
        x = start[0]
        if start[1] < end[1]:
            a = start[1]
            b = end[1]
        else:
            b = start[1]
            a = end[1]

        for y in range(a, b + 1):
            self.grid[x, y] = self.grid[x, y] + 1

    def get_points(self):
        points = np.count_nonzero(self.grid > 1)
        return points


def main(inputs_file):
    inputs = load_input(inputs_file)

    vent_map = Map()

    for i in inputs:
        start, end = parse_input(i)
        if start[0] == end[0]:
            print(start, end)
            vent_map.y_update(start, end)
        elif start[1] == end[1]:
            print(start, end)
            vent_map.x_update(start, end)

    print(vent_map.grid)
    print(vent_map.get_points())


if __name__ == "__main__":
    main(str(sys.argv[1]))
