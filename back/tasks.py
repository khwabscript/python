import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    # conn = sqlite3.connect(db_file)
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_tasks(conn, usl1, usl2, order):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT condition FROM talks WHERE " + usl1 + " AND " + usl2 + " ORDER BY " + order + " ASC")

    rows = cur.fetchall()

    for row in rows:
        print(str(row[0]))

f = open('input.txt')
lines = f.readlines()
# print(lines)
# print(create_connection('discussion.db'))
conn = create_connection(lines[0].replace('\n', ''))
with conn:
    # print("1. Query task by priority:")
    select_all_tasks(conn, lines[1].replace('\n', ''), lines[2].replace('\n', ''), lines[3].replace('\n', ''))
