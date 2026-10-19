import sqlite3, json

con = sqlite3.connect("data/main.db")
cur = con.cursor()

def init():
    cur.execute("CREATE TABLE IF NOT EXISTS config (username STRING, pat STRING)")
    cur.execute("INSERT INTO config (username, pat) VALUES (?, ?)", ("", ""))
    return cur.execute("SELECT username, pat FROM config").fetchall()

def save_login(data):
    cur.execute(f"INSERT INTO config VALUES({data[0]}, {data[1]})")
    con.commit()