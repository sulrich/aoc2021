#!/usr/bin/env python

import sys


def load_input(infile):
    with open(infile) as f:
        lines = f.readlines()

    return lines


def decoder(pattern, output):
    pattern = pattern.split()
    output = output.split()

    initials = {2: "1", 3: "7", 4: "4", 7: "8"}
    decoded = {}
    for p in pattern:
        if len(p) in initials:
            decoded[initials[len(p)]] = set(p)

    sixes = [set(six) for six in pattern if len(six) == 6]
    fives = [set(five) for five in pattern if len(five) == 5]

    # list comprehensions would probably be better here ...
    for s in sixes:
        if not decoded["1"] < s:  # is not a subset of s
            decoded["6"] = s

    sixes.remove(decoded["6"])

    for s in sixes:
        if decoded["4"] < s:
            decoded["9"] = s

    sixes.remove(decoded["9"])
    decoded["0"] = sixes[0]

    for f in fives:
        if decoded["1"] < f:
            decoded["3"] = f

    fives.remove(decoded["3"])

    for f in fives:
        if f < decoded["6"]:
            decoded["5"] = f

    fives.remove(decoded["5"])
    decoded["2"] = fives[0]

    sorted_decoded_signals = {}
    for k, v in decoded.items():
        v = "".join(sorted(v))
        sorted_decoded_signals[v] = k

    res = []
    for block in output:
        block = sorted(block)
        block = "".join(block)
        res.append(sorted_decoded_signals[block])

    return int("".join(res))


def main(inputs_file):
    inputs = load_input(inputs_file)

    uniq_lengths = [2, 3, 4, 7]
    output_uniqs = 0

    decoded = []

    for i in inputs:
        patterns, outputs = i.split("|")
        for digit in outputs.split():
            if len(digit) in uniq_lengths:
                output_uniqs += 1

        decoded.append(decoder(patterns, outputs))

    print("part a:", output_uniqs)
    print("decoded sum:", sum(decoded))


if __name__ == "__main__":
    main(str(sys.argv[1]))
