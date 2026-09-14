import sqlite3
import os


def dict_factory(cursor, row):
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def make_song_db():
    if os.path.exists("songs.db"):
        os.remove("songs.db")

    SONGS_FOLDER = "songs"
    conn = sqlite3.connect("songs.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        album TEXT NOT NULL,
        filename TEXT NOT NULL UNIQUE

    )
    """)
    for root, dirs, files in os.walk(SONGS_FOLDER):
        for filename in files:
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, SONGS_FOLDER)
            title = os.path.splitext(filename)[0]
            album = os.path.split(root)[1]
            try:
                cursor.execute(
                    "INSERT INTO songs (title, album, filename) VALUES (?, ?, ?)",
                    (title, album, relative_path)
                )
            except sqlite3.IntegrityError as e:
                print(f"HEY there is an error in the db insertion: {e}")
                pass
    conn.commit()
    conn.close()