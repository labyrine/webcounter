from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/place", methods=["POST"])
def place():
    try:
        placed_value = int(request.form["value"])
    except (ValueError, TypeError):
        return redirect("/")

    cnt.place(placed_value)
    return redirect("/")
