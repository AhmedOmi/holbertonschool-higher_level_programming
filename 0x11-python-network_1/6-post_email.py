#!/usr/bin/python3
""" Post an email """
import requests
from sys import argv

if __name__ == "__main__":
    x = requests.post(argv[1], data={'email': argv[2]})
    print(x.text)
