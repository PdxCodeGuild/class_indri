from flask import Flask, render_template, request, redirect
import requests
import html

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def calculate_results():
    result = request.form['Value'], request.form['Unit']
    return result


app.run(debug=True)
