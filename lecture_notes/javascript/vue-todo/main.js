

const { createApp } = Vue

const app = createApp({
    data() {
        return {
            newTodoText: "",
            todos: [
                {text: "Learn Vue", completed: false},
                {text: "Walk the dog", completed: true}
            ]
        }
    },
    methods: {
        addTodo() {
            this.todos.push({
                text: this.newTodoText,
                completed: false
            })
            this.newTodoText = ""
        },
        completeTodo(todo) {
            todo.completed = true
        },
        deleteTodo(todo){
            let index = this.todos.indexOf(todo)
            this.todos.splice(index, 1)
        }
    }
})

app.mount("#app")