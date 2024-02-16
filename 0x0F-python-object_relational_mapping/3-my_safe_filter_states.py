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
    query = ("""SELECT * FROM states WHERE name = %s
                ORDER BY states.id ASC""")
    try:
        cur.execute(query, (sys.argv[4],))
        states = cur.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        cur.close()
        db.close()
