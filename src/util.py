#!/usr/bin/env python3
import sys

# a small hack to automatically grab the input filename
INPUT_FILENAME = sys.argv[0].rstrip(".py").lstrip(sys.argv[0][:sys.argv[0].find("day")+3])
INPUT_FILE = open(f"../res/input_{INPUT_FILENAME}.txt")
