#!/usr/bin/env python3
from util import *

# global list of all elves calories
ELVES_CALORIES = []

def calc_calories() -> None:
    kcal = 0
    idx = 0
    for l in INPUT_FILE: 
        if l == "\n":
            ELVES_CALORIES.append([idx, kcal])
            idx += 1
            kcal = 0
            continue
        kcal += int(l.rstrip('\n'))


def main() -> None:
    calc_calories()
    ELVES_CALORIES.sort(key=lambda x : x[1], reverse=True)
    print(f"Top 3 elves are carrying:\n{[kcal for idx, kcal in ELVES_CALORIES[:3]]}")
    print(f"Total: {sum([kcal for idx, kcal in ELVES_CALORIES[:3]])}")


if __name__ == "__main__":
    main()

