from flask import Flask, jsonify, render_template, request ,send_from_directory
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
    search_by = request.args.get("search_by", "")

    if q:
        if search_by == "album":
            with sqlite3.connect("songs.db") as conn:
                            conn.row_factory = dict_factory
                            songs_db = conn.cursor()
                            songs = songs_db.execute(
                                "SELECT * FROM songs WHERE album like ?",(f"%{q}%",)).fetchall()
        else:
            with sqlite3.connect("songs.db") as conn:
                conn.row_factory = dict_factory
                songs_db = conn.cursor()
                songs = songs_db.execute(
                    "SELECT * FROM songs WHERE title LIKE ?",(f"%{q}%",)).fetchall()
    else: songs = []
    return jsonify(songs)


 
@app.route("/Player/<int:song_id>")
def player(song_id):
    if song_id:
        with sqlite3.connect("songs.db") as conn:
            conn.row_factory = dict_factory
            songs_db = conn.cursor()
            song = songs_db.execute(
                "SELECT * FROM songs WHERE id=?",(song_id,)).fetchone()
        if song:
            return render_template("player.html", found= True, song=song)
        else:
            return render_template("player.html", found= False)
    else: 
        return render_template("player.html", found= False)



@app.route('/songs/<path:filename>')
def songs(filename):
    return send_from_directory('songs', filename)






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)