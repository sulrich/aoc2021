#!/usr/bin/env python

import sys


def load_input(infile):
    with open(infile) as f:
        lines = f.readlines()

    return lines


class sub_position:
    def __init__(self, dist=0, depth=0):
        self.dist = dist
        self.depth = depth

    def forward(self, distance):
        self.dist = self.dist + distance

    def up(self, distance):
        self.depth = self.depth - distance

    def down(self, distance):
        self.depth = self.depth + distance


class aim_position:
    def __init__(self, aim=0, dist=0, depth=0):
        self.aim = aim
        self.dist = dist
        self.depth = depth

    def forward(self, distance):
        self.dist = self.dist + distance
        self.depth = self.depth + (self.aim * distance)

    def up(self, distance):
        self.aim = self.aim - distance

    def down(self, distance):
        self.aim = self.aim + distance


def main(inputs_file):
    inputs = load_input(inputs_file)
    simple_position = sub_position()
    aimed_position = aim_position()

    for i in inputs:
        (action, distance) = i.split()
        if action == "forward":
            simple_position.forward(int(distance))
            aimed_position.forward(int(distance))
        elif action == "up":
            simple_position.up(int(distance))
            aimed_position.up(int(distance))
        elif action == "down":
            simple_position.down(int(distance))
            aimed_position.down(int(distance))

    print("simple position")
    print("  distance:", simple_position.dist, "depth:", simple_position.depth)
    print("  solution:", simple_position.dist * simple_position.depth)

    print("aimed position")
    print("  distance:", aimed_position.dist, "depth:", aimed_position.depth)
    print("  solution:", aimed_position.dist * aimed_position.depth)


if __name__ == "__main__":
    main(str(sys.argv[1]))
