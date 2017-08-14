from sqlite3 import connect
from contextlib import contextmanager
        
@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    print('created table')
    try:
        yield
    finally:
        cur.execute('drop table points')
        print('dropped table')
            
with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        cur.execute('insert into points (x, y) values(2, 2)')
        for row in cur.execute("select x, y from points"):
            print(row)