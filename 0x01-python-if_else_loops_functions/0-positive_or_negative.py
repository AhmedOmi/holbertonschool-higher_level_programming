#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive")
elif number == 0:
    print("{:d} is zero")
else:
    print("{:d} is negative")
