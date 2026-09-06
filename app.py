from flask import Flask , render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():

    if request.method =="GET":
        return render_template("index.html")
        
    else:
        q = request.form.get("q", "error ?")
        conn = sqlite3.connect("songs.db")
        conn.row_factory = sqlite3.Row
        songs_db = conn.cursor()
        songs_dic = songs_db.execute(
            "SELECT * FROM songs WHERE title LIKE ?",(f"%{q}%",)).fetchall()
        for song in songs_dic:
            print(song["title"], song["filename"])
        return render_template("search.html", q=q, songs_dic= songs_dic)










if __name__ == "__main__":
    app.run(debug=True,TEMPLATES_AUTO_RELOAD=True)