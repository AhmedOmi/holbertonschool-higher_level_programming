#!/usr/bin/python3
""" Filter states by user input """
import MySQLdb
from sys import argv
if __name__ == "__main__":
    a1 = argv[1]
    a2 = argv[2]
    a3 = argv[3]
    keyword = argv[4]
    db = MySQLdb.connect(host="localhost", user=a1, passwd=a2, db=a3)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name \
            REGEXP BINARY '{}' ORDER BY id ASC".format(keyword))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
