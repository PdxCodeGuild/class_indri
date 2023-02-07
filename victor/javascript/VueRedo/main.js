const { createApp } = Vue


const app = createApp({
    
    data() {
        return {
            options: ["🤘", "🖐", "✌️"],
            userChoice: null,
            result: ""
        }
    },
    methods: {
        play(userChoice) {
            let opponentChoice = Math.floor(Math.random() * this.options.length)
            opponentChoice = this.options[opponentChoice]
            if (userChoice == "🤘" && opponentChoice == "🖐" || userChoice == "🖐" && opponentChoice == "✌️" || userChoice == "✌️" && opponentChoice == "🤘"){
                this.result = "You Lose!"
                this.userChoice = userChoice
                this.opponentChoice = opponentChoice
            } else if (userChoice == "🤘" && opponentChoice == "✌️" || userChoice == "✌️" && opponentChoice == "🖐" || userChoice == "🖐" && opponentChoice == "🤘") {
                this.result = "You Win!"
                this.userChoice = userChoice
                this.opponentChoice = opponentChoice
            } else if (userChoice == opponentChoice){
                this.result = "It's a draw!"
                this.userChoice = userChoice
                this.opponentChoice = opponentChoice
            }
        }
    }
})

app.mount('#app')