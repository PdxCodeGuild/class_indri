let player_choice = prompt("Choose Rock Paper or Scissors:")

alert(`You have chosen ${player_choice}`)

let choices = ["rock", "paper", "scissors"]
let computer_choice_index = Math.floor(Math.random() * choices.length)
let computer_choice = choices[computer_choice_index]

alert(`The computer has chosen ${computer_choice}`)

if (player_choice === computer_choice) {
    alert("It is a tie!")
}
else if (player_choice === "rock" && computer_choice === "paper" ) {
    alert("You have lost!")
}
else if (player_choice === "rock" && computer_choice === "scissors" ) {
    alert("You have won!")
}
else if (player_choice === "paper" && computer_choice === "rock" ) {
    alert("You have won!")
}
else if (player_choice === "paper" && computer_choice === "scissors" ) {
    alert("You have lost!")
}
else if (player_choice === "scissors" && computer_choice === "paper" ) {
    alert("You have won!")
}
else if (player_choice === "scissors" && computer_choice === "rock" ) {
    alert("You have lost!")
}
