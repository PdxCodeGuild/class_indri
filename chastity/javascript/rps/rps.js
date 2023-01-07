
// get user input
const choice = prompt("Choose: rock, paper, or scissors.").toLowerCase()

// get random comp choice
const availableChoices = ["rock", "paper", "scissors"]
// get random number

const randomIndex = Math.floor(Math.random() * 3)

const compChoice = availableChoices[randomIndex]

// determine winner
if(compChoice === choice){
    alert("It is a tie, refresh to try again.")
}
else if ((choice === "rock" && compChoice === "paper") || 
(choice === "paper" && compChoice === "scissors") || 
(choice === "scissors" && compChoice === "rock")) {
    alert("You lose, refresh to try again.")
}
else {
    alert("YOU WON!!! Refresh to play again.")
}