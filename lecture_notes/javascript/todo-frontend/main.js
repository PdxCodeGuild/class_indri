
const { createApp } = Vue

const app = createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            message: "Hello from Vue from DRF",
            todos: []
        }
    },
    methods: {
        getAllTodos() {
            axios.get("http://localhost:8000/api/v1")
            .then((data) => {
                this.todos = data.data
            })
        },
        getCurrentWeather() {
            axios.get("")
        }
    },
    created() {
        this.getAllTodos()
    }
})

app.mount("#app")