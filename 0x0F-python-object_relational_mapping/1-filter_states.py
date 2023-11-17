#!/usr/bin/python3
import MySQLdb
"""This module lists all states with a name starting with N"""


def states_with_N(username, password, database):
    """a function that lists all states with a name starting with N"""
    conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                           passwd="root", db="hbtn_0e_0_usa", charset="utf8")
    curs = conn.cursor()
    curs.execute(
