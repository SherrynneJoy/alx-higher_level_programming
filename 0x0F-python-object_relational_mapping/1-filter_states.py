#!/usr/bin/python3
import MySQLdb
"""This module lists all states with a name starting with N"""


if __name__ == "__main__":
    """a function that lists all states with a name starting with N"""
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                               passwd="root", db="hbtn_0e_0_usa",
                               charset="utf8")
        curs = conn.cursor()
        curs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
        total_rows = curs.fetchall()
        for row in total_rows:
            print(row)
    except MySQLdb.Error as err:
        print(f"Error: {err}")
    finally:
        curs.close()
        conn.close()
