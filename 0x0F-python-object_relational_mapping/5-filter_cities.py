#!/usr/bin/python3
"""
A script that lists all cities
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the states
    """
    db_connect = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, \
                FROM cities JOIN states ON cities.state_id \
                = states.id WHERE states.name LIKE BINARY %(state_name)s \
                ORDER BY cities.id ASC", {'state_name': argv[4]})
        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))
