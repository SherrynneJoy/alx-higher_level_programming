#!/usr/bin/python3
"""a script that takes in the name of a state as an argument and
lists all cities of that state"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = sys.argv[4]
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states ON
               states.id=cities.state_id WHERE
               states.name=%s""", (sys.argv[4], ))
    total_rows = cur.fetchall()
    temp = list(row[0] for row in total_rows)
    print(*temp, sep=", ")
    cur.close()
    conn.close()
