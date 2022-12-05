#!/usr/bin/env python3
from util import *

# honestly this implementation sucks really hard
# but stupid hacks all the way
# (don't software develop like this, plz)

STACKS = []

def create_stacks(lines : list[str]) -> None:
    global STACKS
    STACKS = []
    for i, l in enumerate(lines):
        if " 1 " in l:
            break
        # stupid hack: each line has 4 * stack_count characters
        if i == 0:
            STACKS = [[] for _ in range(len(l)//4 + 1)]
        for j in range(1, len(l), 4):
            if l[j] != ' ':
                STACKS[j//4].append(l[j])
    STACKS = list(map(list, map(reversed, STACKS)))


def execute_moves(lines : list[str], crate_mover_version : int = 9000) -> None:
    global STACKS
    for l in lines:
        if "move" not in l:
            continue

        n, x, y = list(map(int, l.replace("move ", '').replace("from ", '').replace("to ", '').split()))
        # move crates
        if crate_mover_version == 9000:
            STACKS[y-1] += list(reversed(STACKS[x-1][len(STACKS[x-1])-n:]))
        elif crate_mover_version == 9001:
            STACKS[y-1] += STACKS[x-1][len(STACKS[x-1])-n::1]
        # pop crates
        STACKS[x-1] = STACKS[x-1][:-n]


def print_tops() -> None:
    global STACKS
    print("The tops of the stack are: ", end='')
    for st in STACKS:
        if (len(st)):
           print(st[-1], end='')
    print()


def main() -> None:
    global STACKS
    lines = list(map(lambda x : x.rstrip('\n'), INPUT_FILE.readlines()))
    create_stacks(lines)
    execute_moves(lines, crate_mover_version=9000)
    print_tops()
    create_stacks(lines)
    execute_moves(lines, crate_mover_version=9001)
    print_tops()

if __name__ == "__main__":
    main()
