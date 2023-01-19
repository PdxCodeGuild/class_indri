// Pick a Python lab and re-do it in JavaScript. 
// You should first try to write them using JavaScript's prompt and alert in place of Python's input and print.


// unit_converter
let convert = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m" : 1,
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254
}

// get input from value box
let userValue = document.querySelector("#userValue")
// get input from unit box
let userUnit = document.querySelector("#userUnit")

// # Convert the user value from user unit to meters
// # return the result
function returnResult(){
    event.preventDefault();
    let value = userValue.value
    let unit = userUnit.value
    let result = (value * convert[unit])
    let resulttest = isNaN(result)
    
    // console.log(resulttest)
    
    if (resulttest === false){
        displayResult.textContent = `${value} ${unit} is ${result} meters`}
    else
        alert("Invalid! Try again.")
        
        userValue.value = ""
    }
    
convertBtn.addEventListener("click", returnResult)

// we do not need to control for enter input here
// Because the convert button is inside a form, whenever Enter is pressed it will click the button

// converterForm.addEventListener("keydown", function(event){
//     if(event.key === "Enter"){
//         returnResult()
//     }
// })