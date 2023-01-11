
// get user input (rock, paper, scissors)
const choice = prompt("Choose: rock, paper, or scissors.").toLowerCase()

// get random comp choice
const availableChoices = ["rock", "paper", "scissors"]
// get random number between 0-3 (indexes of availableChoices)
const randomIndex = Math.floor(Math.random() * 3)

const compChoice = availableChoices[randomIndex]

// determine a winner
if(compChoice === choice){
    alert("It was a tie, refresh the page to try again.")
}
else if ((choice === "rock" && compChoice === "paper") ||
         (choice === "paper" && compChoice === "scissors") ||
         (choice === "scissors" && compChoice === "rock")) {
    alert("You lose, refresh the page to try again.")
}
else {
    alert("You won! Try your luck by refreshing the page.")
}