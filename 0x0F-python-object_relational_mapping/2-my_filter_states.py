#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""


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

    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                   ORDER BY id ASC""".format(state))

    states = cursor.fetchall()

    for row in states:
        print(row)

    cursor.close()
    conn.close()
