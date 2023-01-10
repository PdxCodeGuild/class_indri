let choices = {
    rock: 'rock',
    paper: 'paper',
    scissors: 'scissors'}

function greeting(){
    alert(`Hello, lets play a rock paper scissors game.`)
}

function userInput(){
    let userInput =prompt('Input your choice of rock, paper, or scissors').toLowerCase()
    return userInput
}


function game(userInput){
    const aiChoice = Math.floor(Math.random() * choices.length)
    if (aiChoice=== userInput){
        playagain=prompt('You Tie! Do you want to play? Yes/No')
        return playagian
    } else if (aiChoice === 'rock' && userInput === 'scissors' || aiChoice === 'paper' && userInput === 'rock' || aiChoice === 'scissors' && userInput === 'paper'){
        playagain=prompt('You Lose! Do you want to play? Yes/No')
        return playagain
    } else {
        playagain=prompt('You Win! Do you want to play? Yes/No')
        return playagain
    }
}
greeting()
userInput()
let result =game()
do {
    userInput()
    result=game()
  }
  while (result =="Yes");