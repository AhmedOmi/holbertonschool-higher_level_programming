#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 1:
        print("0 arguments.")
    elif i == 2:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(i - 1))
        n = 1
        for count in range(1, i):
            print("{:d}: {:s}".format(n, sys.argv[i]))
            n += 1
