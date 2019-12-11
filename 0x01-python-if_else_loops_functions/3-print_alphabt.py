#!/usr/bin/python3
for count in range(ord('a'), ord('z') + 1):
    if count != ord('q') and count != ord('e'):
        print("{:c}".format(count), end="")
