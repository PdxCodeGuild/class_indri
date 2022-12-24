from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

metrics = { "feet": 0.3048, "miles": 1609.34, "meters": 1, "kilometers": 1000,
  "ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000 }



# The route() decorator tells Flask what URL should trigger our function
@app.route("/", methods=['GET','POST'])
def home():
  if request.method == 'POST':
    distance_entered = request.form['distance']
    units_entered = request.form['units']
    if units_entered in metrics:
      return f'{int(distance_entered)} {units_entered} is {int(distance_entered) * metrics[units_entered]} m'
  else:
    return render_template('home.html')





@app.route("/about")
def About_page():
    return render_template('about.html', title = 'About')



if __name__ == '__main__':
  app.run(debug=True)