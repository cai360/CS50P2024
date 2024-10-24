from flask import Flask, render_template, request, redirect, url_for
from calendar import Calendar


app = Flask(__name__, template_folder="templates")

dates = [{"date": "just try it"}]


@app.route("/")
def index():
    name = "JOY"
    return render_template("index.html", name = name, dates = date)


@app.route("/add_date", methods = ["post"])
def add_date():
    date = request.form['date_number']
    dates.append({"date" : date_number,})
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug = True)
