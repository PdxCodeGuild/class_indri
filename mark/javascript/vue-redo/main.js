const {createApp } = Vue

const app = createApp({
    data() {
        return {
            user: null,
            comp: null,
            choices: [
                "rock",
                "paper",
                "scissors",
            ],
            gameLog: [],
        }
    },
    methods: {

        playGame(choice){
            user = choice.target.name; // user choice is the button they click
            comp = this.choices[(Math.floor(Math.random() *3))]; // computer choice is random from choices array.
            
            if(user == comp){ // if user choice equals computer choice, the game is a tie.
                this.gameLog.push({"user": user, "computer": comp, "result":"Tie"})

            } else if ( // if the computer choice beats the user choice, you lose. 
                user == "rock" && comp == "paper" ||
                user == "paper" && comp =="scissors" ||
                user == "scissors" && comp == "rock" )
                { this.gameLog.push({"user": user, "computer": comp, "result":"You Lose"})

            } else { // if its not a tie and the computer did not win, then you win!
                this.gameLog.push({"user": user, "computer": comp, "result":"You Win!"})

            } 
        }
    },
    computed: {
        displayLog(){ // generate newest game results at the top of the game log. 
            return this.gameLog.slice().reverse();
        },
    }
})

app.mount('#app')