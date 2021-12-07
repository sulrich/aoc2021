#!/usr/bin/env python

import sys


def load_input(infile):
    with open(infile) as f:
        lines = f.readlines()

    return lines


def bitlist_to_int(diag_list):
    return int("".join(str(x) for x in diag_list), 2)


def load_cards(card_list):
    cards = []
    card = []
    for i in card_list:
        i = i.strip()
        if i != "":
            card.append(list(int(x) for x in i.split()))
        else:
            cards.append(card)
            card = []
    return cards


class BingoCard:
    def __init__(self, card=[]) -> None:
        self.card = card
        # note that the * operator only operates on objects. nested
        # intialization need additional iteration
        self.matches = [[0] * 5 for _ in range(5)]
        self.draws = 0  # how many iterations does it take to get a bingo
        self.score = 0  # final calculated score
        self.last_draw = 0  # what's the last draw we matched on
        self.bingo = False
        return

    def check_draw(self, draw):
        self.draws += 1
        for ridx, row in enumerate(self.card):
            for cidx, cell in enumerate(row):
                if draw == cell:
                    self.matches[ridx][cidx] = 1
                    self.last_draw = draw

        return

    def check_bingo(self):
        col_sum = [0] * 5
        for row in self.matches:
            if sum(row) == 5:
                return True

            for cidx, cell in enumerate(row):
                col_sum[cidx] = col_sum[cidx] + cell

        if 5 in col_sum:
            return True

        return False

    def score_card(self):
        score = 0
        for ridx, row in enumerate(self.matches):
            for cidx, cell in enumerate(row):
                if cell == 0:
                    score = score + self.card[ridx][cidx]

        self.score = score * self.last_draw
        return

    def play_card(self, draws):
        for d in draws:
            self.check_draw(d)
            if self.draws >= 5:
                bingo = self.check_bingo()
                if bingo:
                    self.bingo = True
                    self.score_card()
                    break

        return


def main(inputs_file):
    inputs = load_input(inputs_file)

    draws = list(int(x) for x in inputs[0].split(","))
    cards = load_cards(inputs[2:])

    min_draws = 0
    min_score = 0
    min_last_draw = 0

    max_draws = 0
    max_score = 0
    max_last_draw = 0

    for card in cards:
        c = BingoCard(card)
        c.play_card(draws)
        if c.bingo:
            if min_draws == 0:
                min_draws = c.draws

            if c.draws <= min_draws:
                min_draws = c.draws
                min_score = c.score
                min_last_draw = c.last_draw

            if c.draws >= max_draws:
                max_draws = c.draws
                max_score = c.score
                max_last_draw = c.last_draw

    print("win fast")
    print(min_draws, min_score, min_last_draw)

    print("lose slow")
    print(max_draws, max_score, max_last_draw)


if __name__ == "__main__":
    main(str(sys.argv[1]))
