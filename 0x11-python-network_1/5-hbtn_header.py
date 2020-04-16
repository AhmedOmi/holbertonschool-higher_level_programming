
#!/usr/bin/python3
""" Response header value """
import requests
from sys import argv

if __name__ == "__main__":
    x = requests.get(argv[1])
    print(x.headers.get('X-Request-Id'))
