import sqlite3
import json

DB_FILE = 'terraform.db'

def create_connection(db_file=DB_FILE):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn


def db_init():
    conn = create_connection()
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS state")
    c.execute("CREATE TABLE state (id varchar(3) primary key, data json)")
    save_state({"version": 1})
    conn.commit()


def save_state(state):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT or REPLACE INTO state VALUES (?, ?)", ["state", json.dumps(state)])
    conn.commit()


def get_state():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM state WHERE id='state'")
    data = c.fetchone()
    if data is not None and len(data) == 2:
        return data[1]

def remove_state():
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE * FROM state WHERE id='state")
    conn.commit()