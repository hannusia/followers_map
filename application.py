from flask import Flask, render_template, request
from get_map import main

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/map", methods=["POST"])
def register():
    if not request.form.get("nickname") or not request.form.get("token"):
        return render_template("failure.html")
    with open("nickname.txt", 'w') as file:
        nickname = request.form['nickname']
        token = request.form['token']
    try:
        main(nickname, token)
    except KeyError:
        return render_template('failure.html')
    return render_template("followers_map.html")


app.run(debug=True)
