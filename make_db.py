import sqlite3

conn = sqlite3.connect("songs.db")
db = conn.cursor()
db.execute("CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY,title TEXT NOT NULL,filename TEXT NOT NULL UNIQUE);")
conn.commit()


print("done")