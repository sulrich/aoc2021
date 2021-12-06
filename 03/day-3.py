#!/usr/bin/env python

import sys
import re


def load_input(infile):
    with open(infile) as f:
        lines = f.readlines()

    return lines


def bitlist_to_int(diag_list):
    return int("".join(str(x) for x in diag_list), 2)


class Diagnostics:
    def __init__(self, diag_length):
        self.ones = [0] * diag_length
        self.zeros = [0] * diag_length

    def parse_diags(self, bitstring):
        for idx, i in enumerate(bitstring):
            i = int(i)
            if i == 1:
                self.ones[idx] = self.ones[idx] + 1
            else:
                self.zeros[idx] = self.zeros[idx] + 1

    def calc_power_rates(self):
        _gamma = []
        _epsilon = []
        for idx, _ in enumerate(self.ones):
            if self.ones[idx] > self.zeros[idx]:
                _gamma.append(1)
                _epsilon.append(0)
            else:
                _gamma.append(0)
                _epsilon.append(1)

        gamma = bitlist_to_int(_gamma)
        epsilon = bitlist_to_int(_epsilon)

        return gamma, epsilon


class FilteredDiagnostics:
    """
    - based on the first pass through the data set we know what the first
      filter will need to be.

      recurse through the continuously filtered data sets until
      we find the diag value we need foe the life support ratings

      for each iteration
      - filter based on the entry filter (a regex)
      - for matches
        - assemble the filtered data set
        - parse the diag messages to get the frequency counts
        -

    """

    def __init__(self, bound="upper"):
        self.bound = bound

    def filter(self, ds, filter):
        _ds = []  # the data set for this iteration
        _filter = ""  # the filter for the next iteration

        filter_pattern = "^" + filter

        _diags = Diagnostics(12)

        for el in ds:
            el = el.strip()
            if re.match(filter_pattern, el):
                _ds.append(el)
                _diags.parse_diags(el)

        if len(_ds) <= 1:
            return bitlist_to_int(_ds[0])
        else:
            idx = len(filter)  # use the length here to index into the stats list
            if self.bound == "upper":
                if _diags.ones[idx] >= _diags.zeros[idx]:
                    _filter = filter + "1"
                else:
                    _filter = filter + "0"
            else:
                if _diags.zeros[idx] <= _diags.ones[idx]:
                    _filter = filter + "0"
                else:
                    _filter = filter + "1"

            return self.filter(_ds, _filter)


def main(inputs_file):
    inputs = load_input(inputs_file)
    diags = Diagnostics(12)

    for i in inputs:
        i = i.strip()  # remove trailing whitespace
        diags.parse_diags(i)

    (gamma, epsilon) = diags.calc_power_rates()
    print("day 3a")
    print("-" * 30)
    print("  gamma:", gamma)
    print("epsilon:", epsilon)
    print("  power:", gamma * epsilon)

    print()
    print("day 3b")
    print("-" * 30)
    # print(diags.ones[0], diags.zeros[0])

    if diags.ones[0] > diags.zeros[0]:
        o_filter = "1"
        co2_filter = "0"
    else:
        o_filter = "0"
        co2_filter = "1"

    o_gen_rating = FilteredDiagnostics()
    o_gen = o_gen_rating.filter(inputs, o_filter)

    co2_scrubber_rating = FilteredDiagnostics(bound="lower")
    co2_scrub = co2_scrubber_rating.filter(inputs, co2_filter)
    print(" o_gen:", o_gen)
    print("   co2:", co2_scrub)
    print("rating:", o_gen * co2_scrub)


if __name__ == "__main__":
    main(str(sys.argv[1]))
