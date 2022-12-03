#!/usr/bin/env python3
import sys
import string

# a small hack to automatically grab the input filename
INPUT_FILENAME = sys.argv[0].rstrip(".py").lstrip(sys.argv[0][:sys.argv[0].find("day")+3])
INPUT_FILE = open(f"../res/input_{INPUT_FILENAME}.txt")

PRIORITIES = {}
GROUP_MEMBER_COUNT=3

def set_priorities() -> None:
    for prio, letter in enumerate(string.ascii_letters):
        PRIORITIES[letter] = prio + 1

def print_common_prio(lines) -> None:
    prio_sum = 0
    for l in lines:
        used = []
        first, second = l[:len(l)//2], l[len(l)//2:]
        for c in first:
            if c in second and c not in used:
                prio_sum += PRIORITIES[c]
                used.append(c)
    print(f"Sum of priorities of common items is: {prio_sum}")


def print_badge_prio(lines) -> None:
    prio_sum = 0
    for i in range(GROUP_MEMBER_COUNT, len(lines) + 1, GROUP_MEMBER_COUNT):
        m1, m2, m3 = lines[i-GROUP_MEMBER_COUNT:i]
        for c in m1:
            if c in m2 and c in m3:
                prio_sum += PRIORITIES[c]
                break
    print(f"Sum of priorities of badges is: {prio_sum}")
            



def main() -> None:
    set_priorities()
    lines = list(map(lambda l : l.rstrip('\n'), INPUT_FILE.readlines()))
    print_common_prio(lines)
    print_badge_prio(lines)

if __name__ == "__main__":
    main()

