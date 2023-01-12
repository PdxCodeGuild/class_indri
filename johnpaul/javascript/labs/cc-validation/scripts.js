
/* 
Let's write a function which returns whether a string containing a credit card number is valid as a boolean.
The steps are as follows:
*/


// Convert the input string into a list of ints
let userEnteredInput = document.querySelector("#userCcInputed");
let validateBtn = document.querySelector('#validateBtn');

validateBtn.addEventListener("click", function(){
   // using .split('') turns the user input into individual value of an array
   let userInput = userEnteredInput.value.split('')
   // Slice off the last digit. That is the check digit.
   let checkedDigit = userInput.pop()
   // Reverse the digits.
   let reverseDigit = userInput.reverse()
   // Double every other element in the reversed list.
   let sum = 0
    for (let num in reverseDigit){
      if (num % 2 == 0){
         reverseDigit[num] *= 2
      }
      // Subtract nine from numbers over nine.
      if (reverseDigit[num] > 9) {
         reverseDigit[num] -= 9
      }
      // Sum all values.
      sum += reverseDigit[num]
      console.log(sum)
   }
})

















// Take the second digit of that sum.






// If that matches the check digit, the whole card number is valid.