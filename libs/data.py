import sqlite3

con = sqlite3.connect("data/main.db")
cur = con.cursor()

def init():
    cur.execute("CREATE TABLE IF NOT EXISTS config (username STRING, pat STRING)")

def save_login(data):
    cur.execute("INSERT INTO config (username, pat) VALUES (?, ?)", (data[0], data[1]))
    con.commit()

def get_login():
    return cur.execute("SELECT username, pat FROM config").fetchall() or [(None, None)]