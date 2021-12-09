#!/usr/bin/env python

import sys
import pprint
from collections import defaultdict


def load_input(infile):
    with open(infile) as f:
        lines = f.readlines()

    return lines


def bitlist_to_int(diag_list):
    return int("".join(str(x) for x in diag_list), 2)


def process_population(pop):
    tmp_pop = []
    for fidx, f in enumerate(pop):
        if f == 0:
            pop[fidx] = 6
            tmp_pop.append(8)
        else:
            pop[fidx] = f - 1

    pop = pop + tmp_pop
    return pop


def process_pop_fast(pop):
    # create a dict of ages
    tmp_ages = defaultdict()
    for i in range(0, 9):
        tmp_ages[i] = 0

    for age in pop:
        if age == 0:
            tmp_ages[6] = tmp_ages[6] + pop[age]
            tmp_ages[8] = pop[age]
        else:
            tmp_age = age - 1
            tmp_ages[tmp_age] = tmp_ages[tmp_age] + pop[age]

    return tmp_ages


def main(inputs_file, days):
    inputs = load_input(inputs_file)

    population = inputs[0].strip()
    population = [int(x) for x in population.split(",")]
    pop = defaultdict()
    for i in range(0, 9):
        pop[i] = 0

    for k in population:
        pop[k] += 1

    for day in range(1, days + 1):
        # population = process_population(population)
        pop = process_pop_fast(pop)

    print("day: ", days, "pop:", sum(pop.values()))


if __name__ == "__main__":
    main(str(sys.argv[1]), int(sys.argv[2]))
