#!/usr/bin/python3

"""This module lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    """lists all states"""
    db=_mysql.connect(
            host="localhost",
            port=3306,
            username="yvonnegichovi",
            password="",
            database="hbtn_0e_0_usa")
