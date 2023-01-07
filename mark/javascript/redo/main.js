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


// # ask the user for the number
const value = prompt("Enter a value to convert to meters: ")

// # ask the user for the unit
const unit = prompt("Enter a unit (ft, mi, km, yd, in): ")

// # Convert the user distance from user unit to meters
let result = (value * convert[unit])

// #return the result
alert(value + " " + unit + " is " + result + " meters")