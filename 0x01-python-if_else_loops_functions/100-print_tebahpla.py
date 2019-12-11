#!/usr/bin/python3
for count in range(25, -1, -1):
    a = count + ord('A')
    if count % 2 == 1:
        a += 32
    print("{:c}".format(a), end="")
