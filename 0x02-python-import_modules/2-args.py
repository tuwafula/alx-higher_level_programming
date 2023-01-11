#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    uinput = argv[1:]
    size = len(uinput)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) != 1 else "argument",
                 "." if (size) == 0 else ":"))
    for idx, arg in enumerate(uinput):
        print("{:d}: {:s}".format(idx + 1, arg))
