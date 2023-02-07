const { createApp } = Vue

const app = createApp({

    data() { 
        return {
            choice: ["🪨", "📃", "✂️"],
            playChoice: null,
            result: ""
        }
    },
    methods: {
      play(playChoice) {
        let compChoice = Math.floor(Math.randon() * 3)
        compChoice = 3[compChoice]
        if (playChoice === compChoice){
          this.result = "It is a tie"
          this.playChoice = playChoice
          this.compChoice = compChoice
        } else if (playChoice === "🪨" && compChoice === "📃" || playChoice === "📃" && compChoice === "✂️" || playChoice === "✂️" && compChoice === "🪨"){
          this.result = "You Lose"
          this.playChoice = playChoice
          this.compChoice = compChoice
        } else {
          this.result = "YOU WIN!!!"
          this.playChoice = playChoice
          this.compChoice = compChoice
        }
      }
    }
})

app.mount('#app')