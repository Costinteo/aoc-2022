#!/usr/bin/env python3
from util import *

def count_pair_overlaps(lines : list[str]) -> int:
    count = 0
    for l in lines:
        a, b, x, y = list(map(int, l.replace('-', ',').split(',')))
        count += ((x - a) * (y - b) <= 0)
    return count

def count_all_overlaps(lines : list[str]) -> int:
    count = 0
    for l in lines:
        a, b, x, y = list(map(int, l.replace('-', ',').split(',')))
        count += ((x - b) * (y - a) <= 0)
    return count
        
        

def main() -> None:
    lines = list(map(lambda x : x.rstrip('\n'), INPUT_FILE.readlines()))
    print(f"Pair overlaps count: {count_pair_overlaps(lines)}")
    print(f"All overlaps count: {count_all_overlaps(lines)}")

if __name__ == "__main__":
    main()

