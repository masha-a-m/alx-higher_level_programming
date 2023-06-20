#!/usr/bin/python3

"""task 2 python"""

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.a    rgv[2],

import mySQLdb

import sys

if __name__ == '__main__':
                         db=sys.argv[3], port=3306)


    cur.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))

cur = db.cursor()

states = cur.fetchall()

    for state in states:
        print(state)
