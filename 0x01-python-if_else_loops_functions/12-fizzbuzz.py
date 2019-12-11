#!/usr/bin/python3
def fizzbuzz():
    for count in range(1, 101):
        if count % 3 == 0:
            print("Fizz", end='')
        if count % 5 == 0:
            print("Buzz", end='')
        if count % 3 > 0 and count % 5 > 0:
            print("{:d}".format(count), end='')
        print(" ", end='')
