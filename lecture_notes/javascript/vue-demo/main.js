
// Pull 'createApp' out of 'Vue' so we no longer need to say Vue.createApp
const { createApp } = Vue

// Create a Vue application
const app = createApp({
    // Data stores all of our global app variables
    data() {
        return {
            message: "Let's learn Vue!",
            bestClass: "Indri",
            grade: null,
        }
    },
    computed: {
        textColor() {
            if(this.grade >= 80){
                return "green"
            } else if (this.grade >= 60){
                return "yellow"
            } else {
                return "red"
            }
        }
    }
})

// Finally, mount the app to an element with id app
app.mount("#app")