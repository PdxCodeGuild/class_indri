// Let's make a simple todo-list which supports the following operations:
let userInput = document.querySelector("#userInput")
let todoList = document.querySelector("#todoList")
let doneList = document.querySelector('#doneList')
let submitBtn = document.querySelector("#submitBtn")
let deleteBtn = document.querySelector('#deleteBtn')
let completedBtn = document.querySelector('#completedBtn')



submitBtn.addEventListener("click", addToDo)
deleteBtn.addEventListener("click", deleteToDo)
completedBtn.addEventListener("click", completeToDo)

// add an item to the list
function addToDo(){
    event.preventDefault()

    let selected = document.createElement('input')
    let toDo = document.createElement('p')
    
    toDo.className = "toDoItem"
    toDo.textContent = userInput.value
    
    selected.type = "checkbox"
    selected.className = "selectedBox"
    
    todoList.appendChild(toDo)
    toDo.appendChild(selected)
    userInput.value = ""
}

// remove an item from the list
function deleteToDo(){
    let deleteList = todoList.querySelectorAll(".toDoItem")

    deleteList.forEach(function(toDo){
        let check = toDo.lastChild['checked']
    
        if(check == true){
            toDo.remove()
    }
    })
}

// mark an item as completed
function completeToDo(){
    let completedList = todoList.querySelectorAll(".toDoItem")

    completedList.forEach(function(toDo){
        let check = toDo.lastChild['checked']
    
        if(check == true){
            let boxDelete = toDo.lastChild
            boxDelete.remove()
            toDo.classList.add('completedStyle')
            doneList.append(toDo)
    }
    })
}

// Removed items should disappear entirely. Completed items should appear at the bottom (or in a separate list) with a line through them.