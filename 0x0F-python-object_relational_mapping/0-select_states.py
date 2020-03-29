#!/usr/bin/python3
"""select states"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    l = "localhost"
    p = 3306
    a1 = argv[1]
    a2 = argv[2]
    a3 = argv[3]
    db = MySQLdb.connect(host=l, port=p, user=a1, passwd=a2, db=a3)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
