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

// # return the result
function returnResult(){
    event.preventDefault();
    let value = userValue.value
    let unit = userUnit.value
    // # Convert the user value from user unit to meters
    let result = (value * convert[unit])

    // test if the result is Not a Number
    let resulttest = isNaN(result)
    
    // console.log(resulttest)
    
    // if result is a number.
    if (resulttest === false){
        displayResult.textContent = `${value} ${unit} is ${result} meters`}
    else
        alert("Invalid! Try again.")
        
        // reset user value
        userValue.value = ""
    }
    
convertBtn.addEventListener("click", returnResult)