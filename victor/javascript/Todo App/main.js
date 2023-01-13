let input = document.querySelector('#todo')
let btn = document.querySelector('#btn')
let parent = document.querySelector('.todo-list')
let doneList = document.querySelector('#done-item')
let todos = []
let completed = []
btn.addEventListener('click', function(){
    let todo = document.createElement('li')
    let todoBtn = document.createElement('button')
    todoBtn.textContent = 'Done!'
    todo.textContent = input.value + " "
    parent.appendChild(todo)
    todo.appendChild(todoBtn)
    let doneBtn = document.querySelector('.todo-btn')
    doneBtn.addEventListener('click', function(){
        todo.removeChild(todoBtn)
        doneList.appendChild(todo)
        parent.removeChild(todo)
    })

    input.value = ""
})

// todoItem.addEventListener('click', function(){
//     todos.forEach();{
//         // somehow get the button generated from the todo input to remove its own element from the todo list and move it to the done list, when clicked
//         // if (){}

//     }

// })

