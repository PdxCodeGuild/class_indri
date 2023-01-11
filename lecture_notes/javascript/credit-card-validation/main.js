let validateBtn = document.querySelector("#validate");
let output = document.querySelector("#output")

function validateMyCard() {
  // Get input string
  let userInput = document.querySelector("#userInput"); // Element
  userInput = userInput.value; // string

  // Convert the input string into a list of ints
  let cCard = userInput.split(""); // [string]

  for (let i in cCard) {
    cCard[i] = Number(cCard[i]);
  }
  // cCard => [int]

  // Slice off the last digit. That is the check digit.
  let checkDigit = cCard.pop();

  // Reverse the digits.
  cCard.reverse();

//   // Double every other element in the reversed list.
//   for (let i = 0; i < cCard.length; i += 2) {
//     cCard[i] = cCard[i] * 2;
//   }

//   // Subtract nine from numbers over nine.
//   for (let i in cCard) {
//     if (cCard[i] > 9) {
//       cCard[i] -= 9;
//     }
//   }

//   // Sum all values.
//   let sum = 0;
//   for (let num of cCard) {
//     sum += num;
//   }


  let sum = 0
  for(let i in cCard){
    // if index is even, multiply by 2
    if(i % 2 == 0){
        cCard[i] *= 2
    }
    // if number is over 9, subtract 9
    if(cCard[i] > 9){
        cCard[i] -= 9
    }
    // add number to sum
    sum += cCard[i]
  }


  // Take the second digit of that sum.
  let digit = sum.toString()[1];

  // If that matches the check digit, the whole card number is valid.
  if (checkDigit == digit) {
    output.textContent = "Card is valid"
    output.style = "color: green; font-weight: bold;"
} else {
    output.textContent = "Card is invalid"
    output.style = "color: red;"
  }
}

validate.addEventListener("click", validateMyCard);
