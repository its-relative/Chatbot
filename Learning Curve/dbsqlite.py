import random
import datetime
import time
import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS stuffToPlot(
              unix REAL, date_time TEXT, keyword TEXT, value REAL
    )""")
    # c.close()
    # conn.close()

def insert_data():
    c.execute("""INSERT INTO stuffToPlot VALUES(
              1231, '10-12-21', 'python',9 
    )""")
    conn.commit()
    c.close()
    conn.close()


def dynamicInsertor():
    unix = time.time()
    date_time = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = "python"
    value = random.randrange(0,10)
    c.execute("""INSERT INTO stuffToPlot (unix,date_time,keyword,value)
              VALUES (?,?,?,?)
              """,
              (unix,date_time,keyword,value))
    conn.commit()

# if __name__ == "__main__":
create_table()
for i in range(10):
    dynamicInsertor()


c.close()
conn.close()
