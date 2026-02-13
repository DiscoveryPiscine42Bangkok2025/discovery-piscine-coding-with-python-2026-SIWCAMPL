#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    match args:
        case []:
            print("none")
        
        case _:
            for arg in args:
                match arg:
                    case _ if arg.endswith("ism"):
                        continue  
                    case _:
                        print(f"{arg}ism")  

if __name__ == "__main__":
    main()