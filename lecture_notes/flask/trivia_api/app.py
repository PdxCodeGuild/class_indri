from flask import Flask, render_template, request, redirect
import requests
import html

app = Flask(__name__)

# requests.get() is used to request data from an API
# we declared our response in the global scope so we could access it in both the index and calculate_results functions
response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
data = response.json()

# This function will execute when the user goes to localhost:5000/
@app.route("/")
def index():

    questions = []
    for i in range(len(data['results'])):
        question_text = data['results'][i]['question']
        question_text = html.unescape(question_text)
        questions.append(question_text)

    return render_template("index.html", questions=questions)


# routes normally only accept a GET request. In order to allow POST requests, we need to add it to the methods list.
# This function will execute when the user sends a post request to localhost:5000/results
@app.route("/results", methods=["POST"])
def calculate_results():
    
    # from submission from index.html can be accessed through request.form
    user_answers = request.form

    score = 0
    num_of_questions = len(data['results'])

    # Here we are iterating over all questions from our requests.get and comparing the correct answer to the answer provided by the user. If they are the same, we add +1 to their score.
    for i in range(num_of_questions):
        question_text = data['results'][i]['question']
        question_text = html.unescape(question_text)
        if question_text in user_answers:
            answer = user_answers[question_text]
            if answer == data['results'][i]['correct_answer']:
                score += 1
        

    total = (score / num_of_questions) * 100

    return render_template("results.html", total=total)



# if __name__ is __main__ then we know the file was ran directly e.g. `python app.py`
if __name__ == "__main__":
    app.run(debug=True)