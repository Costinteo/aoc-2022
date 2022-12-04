#!/usr/bin/env python3
from util import *

# A + X -> DRAW (A == X)
# A + Y -> WIN  (1 + 2 = 3 odd)  (3 - 1 = 2)
# A + Z -> LOSE (1 + 3 = 4 even) (4 - 1 = 3)
# B + X -> LOSE (2 + 1 = 3 odd)  (3 - 2 = 1) (diff from parity of first move)
# B + Y -> DRAW (B == Y)
# B + Z -> WIN  (2 + 3 = 5 odd)  (5 - 2 = 3) (diff from parity of first move)
# well, can't find a rule... so hardcoding the score table?

SCORE_TABLE = {
        "A X" : 4,   # draw 1
        "A Y" : 8,   # win 2
        "A Z" : 3,   # lose 3
        "B X" : 1,   # lose 1
        "B Y" : 5,   # draw 2
        "B Z" : 9,   # win 3
        "C X" : 7,   # win 1
        "C Y" : 2,   # lose 2
        "C Z" : 6,   # draw 3
}

WIN_TABLE = {
    "X" : 0, # lose
    "Y" : 3, # draw
    "Z" : 6  # win
}

SYMBOL_SCORE_TABLE = {
    "A" : 1, # rock
    "B" : 2, # paper
    "C" : 3  # scissors
}

PICK_TABLE = {
    "A X" : "C",
    "A Y" : "A",
    "A Z" : "B",
    "B X" : "A",
    "B Y" : "B",
    "B Z" : "C",
    "C X" : "B",
    "C Y" : "C",
    "C Z" : "A"
}

# solution looks complicated, probably would have been better to just use some ifs lol


def main() -> None:
    lines = list(map(lambda l : l.rstrip('\n'), INPUT_FILE.readlines()))
    print("Total score according to my strategy guide is ", sum([SCORE_TABLE[l] for l in lines]), sep='')
    print("Total score according to elf's strategy guide is ", sum([WIN_TABLE[l.split()[1]] + SYMBOL_SCORE_TABLE[PICK_TABLE[l]] for l in lines]), sep='')


if __name__ == "__main__":
    main()

