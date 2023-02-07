const { createApp } = Vue


const app = createApp({
    
    data() {
        return {
            options: ["🪨", "📃", "✂️"],
            playerChoice: null,
            result: ""
        }
    },
    methods: {
        play(playerChoice) {
            let computerChoice = Math.floor(Math.random() * this.options.length)
            computerChoice = this.options[computerChoice]
            if (playerChoice == computerChoice){
                this.result = "It is a tie!"
                this.playerChoice = playerChoice
                this.computerChoice = computerChoice
            } else if (playerChoice == "🪨" && computerChoice == "📃" || playerChoice == "📃" && computerChoice == "✂️" || playerChoice == "✂️" && computerChoice == "🪨"){
                this.result = "You Lose!"
                this.playerChoice = playerChoice
                this.computerChoice = computerChoice
            } else if (playerChoice == "📃" && computerChoice == "🪨" || playerChoice == "✂️" && computerChoice == "📃" || playerChoice == "🪨" && computerChoice == "✂️") {
                this.result = "YOU WIN!!"
                this.playerChoice = playerChoice
                this.computerChoice = computerChoice
            }
        }
    }
})

app.mount('#app')