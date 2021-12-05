#!/usr/bin/env python

import sys


def load_input(infile):
    with open(infile) as f:
        lines = f.readlines()

    return lines


def item_incrases(inputs):
    prev_input = 0
    increases = 0

    for idx, i in enumerate(inputs):
        i = int(i)
        if i > prev_input and idx != 0:
            increases += 1

        prev_input = i

    return increases


def sliding_window_increases(inputs, win_size):
    prev_window = 0
    increases = 0

    for idx, i in enumerate(range(len(inputs) - win_size + 1)):
        window = inputs[i : i + win_size]  # sliding window
        window = list(map(int, window))  # convert to int()
        window_sum = sum(window)
        if window_sum > prev_window and idx != 0:  # skip the first one
            increases += 1

        prev_window = window_sum

    return increases


def main(inputs_file):
    inputs = load_input(inputs_file)

    single_increases = item_incrases(inputs)
    print("single increases:", single_increases)
    window_increases = sliding_window_increases(inputs, 3)
    print("window increases:", window_increases)


if __name__ == "__main__":
    main(str(sys.argv[1]))
