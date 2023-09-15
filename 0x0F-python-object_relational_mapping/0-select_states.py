#!/usr/bin/python3
"""
    a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=pwd,
        db=db_name
    )

    # cursor for excuting queries
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states")
    
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    conn.close()
