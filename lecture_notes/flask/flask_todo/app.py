from flask import Flask, render_template, request, redirect

# Passing __name__ to Flask creates our flask application
app = Flask(__name__)

todos = [
    { 'text': 'Walk the dog', 'priority': 2 }
]

# @app.route allows us to create urls that when requested will execute a function
@app.route("/") # localhost:5000/
def index():

    todos.sort(key=lambda todo: todo['priority'], reverse=True)

    # render_template will send an html file to the user who made the request
    # templates must be stored in a folder called `templates`
    # We can pass parameters to our template by adding additional params to render_template
    return render_template("todos.html", todos=todos)


# Routes by default accept GET requests. To allow a route to accept a POST request, we add the methods param
@app.route("/add-todo", methods=["POST"])
def add_todo():
    todo = request.form['todo_text']
    priority = request.form['priority']
    todos.append({
        'text': todo,
        'priority': int(priority)
    })
    return redirect("/")


# By using <string:variable_name> we can create dynamic routes.
# The variable from our route is passed into our function
@app.route("/remove-todo/<string:todo_text>")
def remove_todo(todo_text):
    for todo in todos:
        if todo['text'] == todo_text:
            todos.remove(todo)
            break
    return redirect("/")


# Demo route
@app.route("/greet/<string:name>")
def greet(name):
    colors = ["red", "green", "blue", "purple", "orange"]
    return render_template("index.html", name=name, temp=70, colors=colors)


app.run(debug=True)