import psycopg2
from psycopg2.extensions import cursor
import os
import datetime
def init_db():
    conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS')
        )
    cur = conn.cursor()
    add_db(conn,cur)
def add_db(conn,cur: cursor):
    cur.execute(""" 
                INSERT INTO files (id, dateof)
                VALUES (%s, %s);
                 """,
                (1, datetime.date(2025,12,5)))
    conn.commit()


