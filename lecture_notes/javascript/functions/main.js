
// python:
// def function_name():

// greeting was hoised using the function keyword
greeting()

// Define a function
function greeting(name="Dave"){
    alert(`Hello ${name}`)
}


// Define add as a variable whose value is a function - Does not get hoisted
const add = function(a, b) {
    return a + b
}


// This function takes in a function as a parameter, then calls that function
function callOtherFunction(func){
    func()
}

// passing add function into another funciton
callOtherFunction(add)


// Arrow function - Does not get hoisted
const subtract = (a, b) => {
    return a - b
}


result = subtract(7, 2)