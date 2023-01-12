let todo = document.querySelector('#todo')
let btn = document.querySelector('#btn')
let todoList = document.querySelector('#todo-item')
let doneList = document.querySelector('#done-item')
let todos = []
btn.addEventListener('click', function(){
    todos += todo.value + ' <button>Done!</button>'
    todoList.innerHTML = todos
})

todoList.addEventListener('click', function(){
    todos.forEach();{
        // somehow get the button generated from the todo input to remove its own element from the todo list and move it to the done list, when clicked
        if (){}

    }

})

