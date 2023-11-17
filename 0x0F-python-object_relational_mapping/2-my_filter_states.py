#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    total_rows = cur.fetchall()
    for row in total_rows:
        print(row)
    cur.close()
    conn.close()
