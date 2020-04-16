#!/usr/bin/python3
""" POST an email """
from urllib import request, parse
import sys

if __name__ == "__main__":
    d = parse.urlencode({"email": sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], d) as response:
        print(response.read().decode('utf-8'))
