

let choices = ['rock, paper, scissors']

function greeting(){
    alert(`Hello, lets play a rock paper scissors game?`)
}

function userInput(){
    let userInput =prompt('Input your choice of rock, paper, or scissors').toLowerCase()
    return userInput
}


function game(userInput)
    const aiChoice = array[Math.floor(Math.random() * choices.length)]
    if (aiChoice=== userInput){
        alert('You Tie!')
    } else if (aiChoice === 'rock' && userInput === 'scissors' || aiChoice === 'paper' && userInput === 'rock' || aiChoice === 'scissors' && userInput === 'paper'){
        alert('You Lose!')
    } else {
        alert('You Win!')
    }

greeting()
userInput()