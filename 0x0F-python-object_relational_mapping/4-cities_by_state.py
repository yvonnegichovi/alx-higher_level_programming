#!/usr/bin/python3

"""This module lists all cities from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    """lists all cities"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
