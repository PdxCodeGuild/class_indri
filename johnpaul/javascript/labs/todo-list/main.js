// Removed items should disappear entirely. 
// Completed items should appear at the bottom (or in a separate list) with a line through them


// add an item to the list
let InputArea = document.querySelector('#inputarea')
let addBtn = document.querySelector('#addBtn')
let removeBtn = document.querySelector('#removeBtn')
let completedBtn = document.querySelector('#completedBtn')
let containerRow = document.querySelector('#containerRow')
let completedList = document.querySelector('#completedList')

let p = document.createElement('p')
p.innerText = InputArea.value
let cBox = document.createElement('checkbox')

newTodo = []
completeItems = []



function todo(){
   newTodo.push(InputArea)
}
todo()

addBtn.addEventListener('click', todo){}
