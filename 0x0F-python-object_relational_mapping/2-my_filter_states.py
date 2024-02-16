#!/usr/bin/python3

"""This module lists all states starting with N
from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    """filters a lists of all states"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE '{}%'
                ORDER BY states.id ASC""".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
