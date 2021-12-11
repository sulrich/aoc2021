#!/usr/bin/env python

import sys
import numpy as np


def load_input(infile):
    with open(infile) as f:
        lines = f.readlines()

    map = []
    for i in lines:
        i = i.strip()
        l = [int(x) for x in i]
        map.append(l)

    # inf = [9 for _ in range(xdim)]  # cheat by appending inf
    # map.insert(0, inf)
    # map.append(inf)

    return map


def local_minima(map):
    b_map = np.zeros(map.shape, dtype=bool)
    for y, x in np.ndindex(map.shape):
        h, v = False, False
        if 0 < x < map.shape[1] - 1:
            if map[y, x - 1] > map[y, x] < map[y, x + 1]:
                h = True
        elif x == 0:
            if map[y, x] < map[y, x + 1]:
                h = True
        if x == map.shape[1] - 1:
            if map[y, x] < map[y, x - 1]:
                h = True

        if 0 < y < map.shape[0] - 1:
            if map[y - 1, x] > map[y, x] < map[y + 1, x]:
                v = True
        elif y == 0:
            if map[y, x] < map[y + 1, x]:
                v = True
        if y == map.shape[0] - 1:
            if map[y, x] < map[y - 1, x]:
                v = True

        if h and v:
            b_map[y, x] = True
        else:
            b_map[y, x] = False

    return b_map


def main(inputs_file):
    inputs = load_input(inputs_file)

    field = np.array(inputs)

    minima = local_minima(field)
    coords = np.where(minima)
    risk = [x + 1 for x in field[coords]]

    print(sum(risk))


if __name__ == "__main__":
    main(str(sys.argv[1]))
