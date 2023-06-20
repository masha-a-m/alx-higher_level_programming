#!/usr/bin/python3

""" task 1 statibg all stqtes that begin with n"""


"""importation of sys"""

import sys 
import MySQLdb

"""then my SQL"""

if __name__ == '__main__':

"""password, database, username"""

    db = MySQLdb.connect(user=sys.argv[1] 
		      passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute()
	 """cur execute"""
    states = cur.fetchall()

    for state in states:
        print(state)
