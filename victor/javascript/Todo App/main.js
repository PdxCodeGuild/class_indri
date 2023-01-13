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
    todoBtn.className = 'todo-btn'
    
    todoBtn.addEventListener('click', function(){  
        console.dir(this)
        todo.removeChild(todoBtn)
        doneList.appendChild(todo)
    })

    input.value = ""
})

