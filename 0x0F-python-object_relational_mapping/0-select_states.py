#!/usr/bin/python3
import MySQLdb
"""This module connects to a db, creates a curor, exocutes and prints output"""


conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                       passwd="root", db="hbtn_0e_0_usa", charset="utf8")
curs = conn.cursor()
curs.execute("SELECT * FROM states ORDER BY states.id ASC")
total_rows = curs.fetchall()
for row in total_rows:
    print(row)
curs.close()
conn.close()
