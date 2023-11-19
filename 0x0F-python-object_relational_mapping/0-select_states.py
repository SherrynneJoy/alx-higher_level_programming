#!/usr/bin/python3
"""This module connects to a db, creates a curor, exocutes and prints output"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    curs = conn.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id ASC")
    total_rows = curs.fetchall()
    for row in total_rows:
        print(row)
    curs.close()
    conn.close()
