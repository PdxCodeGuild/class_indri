from flask import Flask, render_template, request, redirect
import requests
import html

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def calculate_results(): 
    value = request.form['Value']
    unit = request.form['Unit']
    
    convert = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254
}
    result = int(value) * convert[unit]
    return render_template("index.html", result=result, value=value, unit=unit)


app.run(debug=True)
