#!/usr/bin/python3
"""
A script that lists all states
with a name starting with N
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the states
    """
    db_connect = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
