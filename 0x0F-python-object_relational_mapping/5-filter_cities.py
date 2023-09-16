#!/usr/bin/python3
"""Write a script that lists all cities from the
database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", user=username, passwd=pwd,
                           db=db_name, port=3306)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """, (state,))

    cities = cursor.fetchall()

    citynames = [city[0] for city in cities]
    print(', '.join(citynames))

    cursor.close()
    conn.close()
