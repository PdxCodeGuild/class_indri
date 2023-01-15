
let userInput = document.querySelector("#new-todo-input")
let addTodoButton = document.querySelector("#new-todo-button")
let todosDiv = document.querySelector("#todos")
let todonesDiv = document.querySelector("#todones")
let todos = []
let todones = []

function addTodo(){
    todos.push(userInput.value)
    userInput.value = ""
    console.log("TODOS:", todos)
    renderTodos()
}

function renderTodos(){
    // empty todosDiv of all todos
    todosDiv.innerHTML = ""
    // loop over all todos and add them to the dom
    for(let i in todos){
        let p = document.createElement("p")
        let doneButton = document.createElement("button")
        let removeButton = document.createElement("button")

        doneButton.addEventListener("click", function(){
            p.classList.add("animate")

            let moveDistance = (todonesDiv.offsetTop + todonesDiv.clientHeight) - p.offsetTop
            let tween = gsap.to(".animate", {
                duration: 2,
                y: moveDistance,
                ease: "none"
            })
            tween.play()

            
            setTimeout(function(){
                p.classList.remove("animate")
                
                p.removeChild(doneButton)
                p.classList.add("completed")
                todonesDiv.appendChild(p)
                todos.splice(i, 1)
                todones.push(p.firstChild.textContent)
                tween.revert()
            }, 2000)

        })

        removeButton.addEventListener("click", function() {
            // .remove to remove child from its parent
            todos.splice(i, 1)
            p.remove()
        })

        p.textContent = todos[i]
        doneButton.textContent = "✓"
        removeButton.textContent = "𝒳"

        p.appendChild(doneButton)
        p.appendChild(removeButton)

        todosDiv.appendChild(p)
    }
}

addTodoButton.addEventListener("click", addTodo)