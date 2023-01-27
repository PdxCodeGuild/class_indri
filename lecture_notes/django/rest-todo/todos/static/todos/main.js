
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
        getPosts(){
            axios.get("https://jsonplaceholder.typicode.com/posts")
            .then((data) => {
                console.log(data)
            })
        }
    },
    created() {
        this.getAllTodos()
        this.getPosts()
    }
})

app.mount("#app")