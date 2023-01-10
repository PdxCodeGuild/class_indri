let choices = [ 'rock', 'paper', 'scissors']

function greeting(){
    alert(`Hello, lets play a rock paper scissors game.`)
}

function userInput(){
    let userInput =prompt('Input your choice of rock, paper, or scissors').toLowerCase()
    return userInput
}


function game(userInput){
    const aiChoice = choices[Math.floor(Math.random() * 3)]
    console.log(aiChoice, userInput)
    if (aiChoice===userInput){
        playagain=prompt(`Computer chose ${aiChoice}, You Tie! Do you want to again? Yes/No`).toLowerCase()
        return playagian
    } else if (aiChoice === 'rock' && userInput === 'scissors' || aiChoice === 'paper' && userInput === 'rock' || aiChoice === 'scissors' && userInput === 'paper'){
        playagain=prompt(`Computer chose ${aiChoice}, You Lose! Do you want to again? Yes/No`).toLowerCase()
        return playagain
    } else {
        playagain=prompt(`Computer chose ${aiChoice}, You Win! Do you want to play again? Yes/No`).toLowerCase()
        return playagain
    }
}
greeting()
const userChoice=userInput()
let result =game(userChoice)
do {
    userInput()
    result=game()
  }
  while (result =="yes");