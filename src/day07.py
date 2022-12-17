#!/usr/bin/env python3
from util import *


PWD = '/'
TREE_SIZE = 0
TREE = {
        #    "PATH" : { "FILENAME": "SIZE", "DIRNAME": "DIRLABEL" },
}

def cd(dir : list[str]) -> None:
    global PWD
    for d in dir:
        if d == "..":
            PWD = PWD[:PWD.rfind('/')]
        elif d == "/":
            PWD = "/"
        else:
            PWD = f"{PWD.rstrip('/')}/{d}"

def ls(contents : list[str]) -> None:
    global PWD, TREE
    for i, f in enumerate(contents):
        # the stupidest hack to ensure files have a dot in them
        if "dir" not in f:
            contents[i] = contents[i] + "."
        if "$" in f:
            contents = contents[:i]
            break
    TREE[PWD] = dict(map(lambda f : list(reversed(f.split())), contents))


COMMANDS = {
    "cd" : cd,
    "ls" : ls
}

def print_tree() -> None:
    print(f"Total Size: {TREE_SIZE}")
    for k,v in TREE.items():
        print(k)
        for f, size in v.items():
           print(f"  {f}, {size}")

def parse_logs(lines : list[str]) -> None:
    for i, line in enumerate(lines):
        tokens = line.split()
        cmd = ""
        arg = ""
        if "$" in tokens:
            cmd = tokens[1]
            arg = tokens[2:] if tokens[2:] else lines[i+1:]
        if cmd:
            COMMANDS[cmd](arg)

def calc_size() -> None:
    global TREE, TREE_SIZE
    list_tree = [[k,v] for k, v in TREE.items()]
    list_tree = sorted(list_tree, key=lambda x: x[0].count('/'), reverse=True)
    for dir, data in list_tree:
        parent_dir = dir[:dir.rfind('/')]
        child_dir = dir[dir.rfind('/')+1:]
        if parent_dir and child_dir:
            TREE[parent_dir][child_dir] = sum([int(size) if size != "dir" else 0 for size in data.values()])
    for f, size in TREE["/"].items():
        if size == "dir":
            TREE["/"][f] = sum(list(map(int, TREE[f"/{f}"].values())))
    TREE_SIZE = sum(list(map(int, TREE["/"].values())))

# calculates the total size of all dirs of max size max_size
def calc_size_dirs(max_size : int) -> int:
    # if filename has a dot then it's not a dir
    # this is a hack so I don't have to change some oneliners and also to simplify the data structure
    return sum([int(size) if "." not in f and int(size) <= max_size else 0 for list_dirs in TREE.values() for f, size in list_dirs.items()])

def find_delete_dir_size(min_size : int) -> int:
    global TREE
    return sorted([int(s) if "." not in f and int(s) >= min_size else TREE_SIZE for list_dirs in TREE.values() for f, s in list_dirs.items()])[0]

def main() -> None:
    filesystem_size = 70000000
    max_dir_size = 100000
    needed_size = 30000000

    lines = list(map(lambda x: x.rstrip('\n'), INPUT_FILE.readlines()))
    parse_logs(lines)
    calc_size()
#    print_tree()
    print(f"Total tree size: {TREE_SIZE}, total size of dirs smaller than 100000: {calc_size_dirs(max_dir_size)}")
    free_size = filesystem_size - TREE_SIZE
    delete_size = needed_size - free_size
    print(f"Directory to delete has size: {find_delete_dir_size(delete_size)}")


if __name__ == "__main__":
    main()
