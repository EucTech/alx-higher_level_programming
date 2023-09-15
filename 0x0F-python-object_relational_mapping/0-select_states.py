#!/usr/bin/python3
"""
     a script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="euctech",
        db="hbtn_0e_0_usa"
    )

    # cursor for excuting queries
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    conn.close()
