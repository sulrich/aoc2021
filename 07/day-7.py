#!/usr/bin/env python

import sys


def load_input(infile):
    with open(infile) as f:
        lines = f.readlines()

    return lines


def main(inputs_file):
    inputs = load_input(inputs_file)

    crabs = inputs[0].strip()
    crabs = [int(x) for x in crabs.split(",")]

    min_gas = float("inf")
    var_gas = float("inf")

    for crab in range(min(crabs), max(crabs)):  # range of crab distances
        dists = [abs(crab - p) for p in crabs]
        # use gauss formula for the variable fuel
        var_fuel = [(n * (n + 1)) / 2 for n in dists]

        min_gas = min(min_gas, sum(dists))
        var_gas = min(var_gas, sum(var_fuel))
        print(min_gas, var_gas)


if __name__ == "__main__":
    main(str(sys.argv[1]))
