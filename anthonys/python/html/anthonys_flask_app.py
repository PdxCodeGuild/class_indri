from flask import Flask, render_template, request, redirect
import string
import random
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('flask.html')

@app.route('/results', methods=["Post"])
def password_maker():
    #I am using the string method to get digits and letters. Then I those values into a varaible 
    user_input=int(request.form['password'])
    print(user_input)
    characters= string.ascii_letters+string.digits+string.punctuation
    #Created a gobal varible for random generated characters in the loop to go into
    password=''
    #This will cuase loop to start and will need when password eachs 10 characters
    while len(password) < user_input:
        random_choice=random.choice(characters)
        #Adding a random generated character each time the while loop runs
        password+= random_choice
    return render_template("results.html", made_password=password)


if __name__=='__main__':
    app.run(debug=True)


