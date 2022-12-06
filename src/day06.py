#!/usr/bin/env python3
from util import *

def detect_start_marker(stream : str, window_size : int) -> int:
    for i in range(len(stream)):
        if len(set(stream[i:i+window_size])) == len(stream[i:i+window_size]):
            return i+window_size

def main() -> None:
    start_packet_window_size = 4
    start_msg_window_size = 14
    stream = INPUT_FILE.readline().rstrip('\n')
    print(f"Start-of-packet Marker detected at position: {detect_start_marker(stream, start_packet_window_size)}")
    print(f"Start-of-message Marker detected at position: {detect_start_marker(stream, start_msg_window_size)}")

if __name__ == "__main__":
    main()
