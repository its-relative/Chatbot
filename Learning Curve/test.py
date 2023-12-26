import random
import sqlite3
import time
import datetime

conn = sqlite3.connect("new.db")
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS newdata(
                        unix REAL, date_time REAL, keyword TEXT, value REAL 
    )""")
    conn.commit()

def dynamic_entry():
    unix = time.time()
    date_time = str(datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %h:%m:%s"))
    keyword = "python"
    value = random.randrange(0,10)
    c.execute(""" INSERT INTO newdata (unix,date_time,keyword,value) VALUES(?,?,?,?)
""",(unix,date_time,keyword,value))
    # c.close()
    conn.commit()
create_table()
for i in range(10):
    dynamic_entry()

c.close()
conn.close()   