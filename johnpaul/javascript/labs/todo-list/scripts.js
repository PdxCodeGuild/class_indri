// Removed items should disappear entirely. 
// Completed items should appear at the bottom (or in a separate list) with a line through them


// add an item to the list
let textArea = document.querySelector('#inputarea')
let addBtn = document.querySelector('#addBtn')
let removeBtn = document.querySelector('#removeBtn')
let completedBtn = document.querySelector('#completedBtn')
let containerRow = document.querySelector('#containerRow')
let completedList = document.querySelector('#completedList')

function todo(){
  addBtn.addEventListener('click', function(){
    //  create checkbox element
    let checkbox = document.createElement('input');
    checkbox.id = 'checkedId';
    checkbox.type = 'checkbox';
    // checkbox.addEventListener('click', function(){
    //   console.dir(checkbox)
    // })
    // creating a paragraph element
    let paragraph = document.createElement('p');
    paragraph.innerText = inputarea.value;
    paragraph.id = "todoparagraph"
    // paragraph.addEventListener('click', function(){
    //   console.dir(paragraph)
    // })
  
    let myDiv = document.createElement('div')
    myDiv.appendChild(checkbox);
    myDiv.appendChild(paragraph);
    // append the value to the <div> id=containerRow
    containerRow.appendChild(myDiv);
    // clears the textarea after adding input
    inputarea.value = "";

  })
  
  // remove an item from the list
  removeBtn.addEventListener('click', function(){
    let itemChecked = document.querySelectorAll('#checkedId')
    for (let i = 0; i < itemChecked.length; i++) {
      if (itemChecked[i].checked == true) {
        console.dir(itemChecked[i])
        containerRow.removeChild(itemChecked[i].parentElement)
      }
    }
  })
  
  // mark an item as completed
  completedBtn.addEventListener('click', function(){
    let checkedCompleted = document.querySelector('#todoparagraph')
    completedList.append(checkedCompleted.innerText.concat(' => completed'))
    let itemChecked = document.querySelectorAll('#checkedId')
    for (let i = 0; i < itemChecked.length; i++) {
      if (itemChecked[i].checked == true) {
        console.dir(itemChecked[i])
        containerRow.removeChild(itemChecked[i].parentElement)
      }
    }
  })
}

todo()






