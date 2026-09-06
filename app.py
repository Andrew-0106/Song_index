from flask import Flask , render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

def SQL(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


db = SQL("sqlite:///songs.db")




@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")

    else:
        q = request.form.get("q", "error ?")

        return render_template("search.html", q=q)


 












if __name__ == "__main__":
    app.run(debug=True)