import os
import sqlite3

SONGS_FOLDER = "songs"
DB_FILE = "songs.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    filename TEXT NOT NULL UNIQUE
)
""")

for root, dirs, files in os.walk(SONGS_FOLDER):
    for filename in files:
        full_path = os.path.join(root, filename)
        relative_path = os.path.relpath(full_path, SONGS_FOLDER)
        title = os.path.splitext(filename)[0]

        try:
            cursor.execute(
                "INSERT INTO songs (title, filename) VALUES (?, ?)",
                (title, relative_path)
            )
            print(f"Added: {title} -> {relative_path}")
        except sqlite3.IntegrityError:
            print(f"Skipped (already exists): {relative_path}")

conn.commit()
conn.close()
