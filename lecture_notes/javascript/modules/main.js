
let buttons = document.querySelectorAll(".btn")

// buttons.forEach
buttons.forEach(function(button){
    button.addEventListener("click", function (){
        playRPS(button)
    })
})


function playRPS(button){
    let userChoice = button.textContent

    const choices = ["🪨", "📃", "✂️"]
    // ai choice
    let opponent = d3.randomInt(0, 3)()
    let text

    if(userChoice == choices[opponent]){
        button.classList.add("tie")
        text = "Tie!"
    }
    else if ((userChoice === "🪨" && choices[opponent] === "📃") ||
             (userChoice === "📃" && choices[opponent] === "✂️") ||
             (userChoice === "✂️" && choices[opponent] === "🪨")){
                let aibutton = document.querySelector(`#${choices[opponent]}`)
                aibutton.classList.add("correct")
                button.classList.add("incorrect")
                text = "You Lose."
    } else {
        button.classList.add("correct")
        text = "You win!"
    }

    addResults(text, userChoice, choices[opponent])
    
    // settimeout will wait a given amount (in milliseconds) before running a function
    setTimeout(function(){
        buttons.forEach(function(button) {
            button.classList.remove("correct")
            button.classList.remove("incorrect")
            button.classList.remove("tie")
        })
    }, 5000)
}

function addResults(text, userChoice, aiChoice){
    let parent = document.querySelector("#results")
    let p = document.createElement('p')
    // "You win! 📃 vs 🪨"
    p.textContent = `${text} ${userChoice} vs ${aiChoice}`
    parent.appendChild(p)
}
