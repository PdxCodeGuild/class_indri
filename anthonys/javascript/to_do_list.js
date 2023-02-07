
// Get all of the varibles to intereact with javascript
let userInput = document.querySelector('#add-task-input')
let addButton= document.querySelector("#add-task-todo-button")
let toDoListDiv=document.querySelector("#to-do-list")
let doneList=document.querySelector("#done-list")

// arrays that will hold Task todo and Tasks Done
let toDoArray= []
let doneArray= []

//fuctions to make program work
function addTask(){
    toDoArray.push(userInput.value)
    userInput.value = ""
    console.log("TO Do List", toDoArray)
    makeToDoList()
}

function makeToDoList() {
    // This empties the list so there can be a blank list
    toDoListDiv.innerHTML = ""
    toDoArray.forEach((task, index) => {
        let p = document.createElement("p")
        // Creating check for each button, element created must be a html element
        let checkButton= document.createElement('button')
        let deleteButton= document.createElement('button')
        p.textContent= task
        // Make Buttons on from Javascript
        checkButton.textContent="✓"
        deleteButton.textContent = "𝒳"
        deleteButton.addEventListener('click', () => {
            removeTask(index)
        })
        checkButton.addEventListener('click',() => {
            completeTask(index)
        })
        // Adding to DOM
        p.appendChild(checkButton)
        p.appendChild(deleteButton)
    
        toDoListDiv.appendChild(p)
    })
    doneList.innerHTML = ""
    doneArray.forEach((task) => {
        let p = document.createElement("p")
        p.textContent= task
        doneList.appendChild(p)
        p.classList.add("task-completed")
    })

}

// Remove/Delete Fuction
function removeTask(index){
    toDoArray.splice(index, 1)
    makeToDoList()
}
// Makes to do task be placed in complete list
function completeTask(index){
    let taskDone=toDoArray.splice(index, 1)
    doneArray.push(taskDone)
    makeToDoList()
}


addButton.addEventListener("click", addTask)

// Let's make a simple todo-list which supports the following operations:

// add an item to the list
// remove an item from the list
// mark an item as completed
// Removed items should disappear entirely. Completed items should appear at 
// the bottom (or in a separate list) with a line through them.