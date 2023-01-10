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

// # ask the user for the value
// const value = prompt("Enter a value to convert to meters: ")
let userValue = document.querySelector("#userValue")
// # ask the user for the unit
// const unit = prompt("Enter a unit (): ")
let userUnit = document.querySelector("#userUnit")

// # Convert the user value from user unit to meters
// # return the result
function returnResult(){
    let value = userValue.value
    let unit = userUnit.value
    let result = (value * convert[unit])
    let resulttest = isNaN(result)
    
    // console.log(resulttest)
    
    if (resulttest === false){
        alert(value + " " + unit + " is " + result + " meters")}
    else
        alert("Invalid! Try again.")

    userValue.value = ""
    userUnit.value = ""
}

convertBtn.addEventListener("click", returnResult)

// we do not need to control for enter input here
// Because the convert button is inside a form, whenever Enter is pressed it will click the button

// converterForm.addEventListener("keydown", function(event){
//     if(event.key === "Enter"){
//         returnResult()
//     }
// })