#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("none")
    else:
        start = int(args[0])
        end = int(args[1])
        number_array = list(range(start, end + 1))
        print(number_array)
if __name__ == "__main__":
    main()