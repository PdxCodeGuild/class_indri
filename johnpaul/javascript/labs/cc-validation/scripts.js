
/* 
Let's write a function which returns whether a string containing a credit card number is valid as a boolean.
The steps are as follows:
*/


// Convert the input string into a list of ints
let userEnteredInput = document.querySelector("#userCcInputed");
let validateBtn = document.querySelector('#validateBtn');

validateBtn.addEventListener("click", function(){
   // using .split('') turns the user input into individual value of an array
   let newUserInput = userEnteredInput.value.split('')
   // Slice off the last digit. That is the check digit.
   newUserInput.pop()
   // Reverse the digits.
   newUserInput.reverse()
   // Double every other element in the reversed list.
   for (let nums in newUserInput){
      if (nums % 2 == 0) {
         newUserInput[nums] = newUserInput[nums]*2
         console.log(newUserInput)
      } 
      }
})




















// Subtract nine from numbers over nine.






// Sum all values.







// Take the second digit of that sum.







// If that matches the check digit, the whole card number is valid.