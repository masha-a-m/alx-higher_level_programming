#!/usr/bin/python3

"""python file liating task 0"""


import sys

"""import the sys from """


import MySQLdb

"""include three arguments """


if __name__ == '__main__':

"""database, name, username, password """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],

    """sys argv port"""

    cur = db.cursor()

    """cursor db cir """

    cur.execute("SELECT * FROM states;")

    for state in state:

    """for the state """

        print(state)


