from flask import Flask, jsonify, render_template, request
import sqlite3
from make_db import make_song_db, dict_factory

app = Flask(__name__)
make_song_db()

@app.route("/")
def index():
    return render_template("index.html")




@app.route("/search")
def search():
    q = request.args.get("q", "")

    if q:
        with sqlite3.connect("songs.db") as conn:
            conn.row_factory = dict_factory
            songs_db = conn.cursor()
            songs = songs_db.execute(
                "SELECT * FROM songs WHERE title LIKE ?",(f"%{q}%",)).fetchall()
    else: songs = []
    return jsonify(songs)



 
@app.route("/Player", methods=["POST"])
def music_player():
    song = request.form.get("song", "")
    






if __name__ == "__main__":
    app.run(debug=True,TEMPLATES_AUTO_RELOAD=True)