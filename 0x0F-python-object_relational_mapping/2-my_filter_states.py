#!/usr/bin/python3

"""task 2 python"""


import mySQLdb

import sys


    cur.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)



cur = db.cursor()

states = cur.fetchall()

    for state in states:
        print(state)
