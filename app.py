from flask import Flask , render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")

    else:
        q = request.form.get("q", "error ?")
        return render_template("search.html", q=q)


 
if __name__ == "__main__":
    app.run(debug=True)