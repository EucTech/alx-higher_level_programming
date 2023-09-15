#!/usr/bin/python3
"""a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", user=username, passwd=pwd,
                           db=db_name, port=3306)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' 
            ORDER BY id ASC;")

    states = cursor.fetchall()

    for row in states:
        print(row)

    cursor.close()
    conn.close()
