from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enter-phrase", methods=["POST"])
def enter_phrase():
    output = ""
    phrase = request.form['phrase']
    shift = int(request.form['shift'])
    shift = shift % 26
    for char in phrase:
        if char in ALPHABET:
            position = ALPHABET.index(char)
            new_position = position + shift
            output += ALPHABET[new_position]
    return render_template('answer.html', output=output)

@app.route("/try-again", methods=["POST"])
def try_again():
    answer = request.form['choice']
    if answer == 'yes':
        return render_template('index.html')
    
    return render_template('goodbye.html')
        



if __name__ == "__main__":
    app.run(debug=True)


