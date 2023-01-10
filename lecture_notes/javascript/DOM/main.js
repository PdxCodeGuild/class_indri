// Get an element by id
let titleById = document.getElementById("title")

// Get an element by className
let titleByClass = document.getElementsByClassName("heading")

// Get an element by QuerySelector
let titleByQuery = document.querySelector('.heading')
let titlesByQuery = document.querySelectorAll('.heading')

titleByQuery.textContent = "Class Indri is the best class!"
// titleByQuery.style = "color: red; background-color: gray; font-size: 38px;"
// titleByQuery.classList.add("new-heading")
// titleByQuery.classList.remove("heading")
// titleByQuery.classList.toggle("hello")
// console.log(titleByClass)

let favColor = document.querySelector("#favColor")

let colorBtn = document.querySelector("#colorBtn")

// Add Event Listener
// First argument is type of event
// Second argument is function to run when event gets triggered

function handleClick(){
    let color = favColor.value
    document.body.style = `background-color: ${color}`
    
    favColor.value = ""
}

colorBtn.addEventListener("click", handleClick)

// add keypress event for enter on input
favColor.addEventListener("keydown", function(event){
    if(event.key === "Enter"){
        handleClick()
    }
})