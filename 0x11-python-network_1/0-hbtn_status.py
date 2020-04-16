#!/usr/bin/python3
"""
Write a Python script that fetches https://intranet.hbtn.io/status
"""
from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as response:
    read = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(read), read, read.decode('utf-8')))
