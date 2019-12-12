#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(i, "" if i == 1 else "s", "." if i == 0 else ":"))
    for count in range(i):
        print("{}: {}".format(count + 1, sys.argv[count + 1]))
