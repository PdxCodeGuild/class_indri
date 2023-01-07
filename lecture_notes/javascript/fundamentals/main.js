

// DataTypes:

/*
let age = 30                        // Number
let pizzaSlices = 4.5               // Number
let javascriptIsCool = true         // Boolean, true/false is lowercase in js
let className = "Indri"             // String
let fruits = ["apple", "banana"]    // Array (List)
let person = {                      // Object (Dictionary)
    "name": "Jordan",
    "age": 30,
    "favoriteFruit": "apple"
}

let nothing = null                  // null
let whatever = undefined            // undefined

*/

/*
Multi
line
comment
here
*/


// input/ouput

// let number = prompt("Enter a number:")

// alert("The number you entered is: " + number)


// console methods
// console.log("Have a nice day")
// console.warn("This is a warning")
// console.error("This is an error")
// console.info("This is info")

let person = {                      // Object (Dictionary)
    "name": "Jordan",
    "age": 30,
    "favoriteFruit": "apple"
}

// console.table(person)

// Arithmetic
let num1 = 4
let num2 = 6

// Operators
num1 + num2
num2 - num1
num1 * num2
num2 / num1

// Assignment operators
num1 += num2
num2 -= num1
num1 *= num2
num2 /= num1

// += 1 shorthand (++)
num1 += 1
num1++
num2 -= 1
num2--

// Math object
Math.abs(-4)        // 4
Math.floor(2.12)    // 2
Math.ceil(4.98)     // 4
Math.min(1, 2, 3, 4, 5) // 1
Math.max(1, 2, 3, 4, 5) // 5
Math.round(2.4) // 2
Math.round(2.6) // 3
Math.random() // random number between 0-1 (not including 1)
Math.floor(Math.random() * 10) // randome number between 0-10 (not including 10)


// Booleans

// true
// false

let a = 4
let b = 6

// if(a === b){
//     alert("A is equal to B")
// }
// else if (a > b){
//     alert("A is greater")
// }
// else if (a < b){
//     alert("B is greater")
// }
// else {
//     alert("Else statement")
// }

// != not equal (this will convert to same type)
// !== strict not equal (this will maintain types)


// let year = prompt("Enter the current year:")

// if (year == 2023){
//     alert("That is the correct year!")
// }
// else {
//     alert("The current year is 2023")
// }


// truthy
"Anthony is awesome"
8
["apple", "banana"]
let item = {"key": 4}
let array = []
let obj = {}

// falsey
0
null
undefined
""


let fruits // fruits = undefined  falsy

fruits = [] // truthy


// Strings

"This is a string"
'This is also a string'
`This is ANOTHER string`

// f"Some fruits i enjoy are {fruits}"
`Some fruits i enjoy are ${fruits}` // template literal 

// String methods
let message = "Hello Class Indri"

// You can use [] syntax to access a character at a given index
message[0] // "H"
message[8] // "a"

// You could also use the .at() method
message.at(0) // "H"
message.at(8) // "a"

// [-1] will always return undefined while .at(-1) will return the last character in the string
message[-1] // undefined
message.at(-1) // "i"

// Use indexOf to find the index of a given character
message.indexOf("C") // 6

// concatinate strings using + or .concat()
message = message + ". Best class ever!" // "Hello Class Indri. Best class ever!"
message = message.concat(" Learning javascript has never been easier") // "Hello Class Indri. Best class ever! Learning javascript has never been easier"

// return true if string contains given string
message.includes("Indri") // true

// transform string to uppercase
message.toUpperCase() // "HELLO CLASS INDRI. BEST CLASS EVER! LEARNING JAVASCRIPT HAS NEVER BEEN EASIER"

// transform string to lowercase
message.toLowerCase() // "hello class indri. best class ever! learning javascript has never been easier"

// split string into an array
message.split(" ") // [ "Hello", "Class", "Indri.", "Best", "class", "ever!", "Learning", "javascript", "has", "never", … ]