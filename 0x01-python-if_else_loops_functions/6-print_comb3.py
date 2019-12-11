#!/usr/bin/python3
for c1 in range(10):
    for c2 in range(c1, 10):
        if c1 < c2:
            print("{:d}{:d}".format(c1, c2),
                  end="\n" if c1 is 8 and c2 is 9 else ", ")
