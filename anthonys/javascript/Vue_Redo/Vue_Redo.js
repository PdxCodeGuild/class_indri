// Pull 'createApp' out of 'Vue' so we no longer need to say Vue.createApp
const { createApp } = Vue



// Create a Vue application
const app = createApp({

    data() {
        return {
            choices: ["rock", "paper", "scissors"],
            userChoice: null,
            outcome: ""
        }
    },

    methods: {
        gamefuction(userChoice) {
            let computer = Math.floor(Math.random() * this.choices.length)
            computer = this.choices[computer]
            if (userChoice == computer){
                this.outcome = "You tied!"
                this.userChoice = userChoice
                this.computer = computer
            } else if (userChoice == "rock" && computer == "scissors" || userChoice == "paper" && computer == "rock" || userChoice == "scissors" && computer == "paper") {
                this.outcome = "You Win!"
                this.userChoice = userChoice
                this.computer = computer
            } else if (userChoice === "rock" && computer === "paper" ||  userChoice === "paper" && computer === "scissors" || userChoice === "scissors" &&  computer == 'rock'){
                this.outcome = "You Lose!"
                this.userChoice = userChoice
                this.computer = computer
            }
        }
    }
})
app.mount('#app')




