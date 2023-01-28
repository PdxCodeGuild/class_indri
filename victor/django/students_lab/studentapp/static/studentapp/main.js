
const { createApp } = Vue

const app = createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            message: "Hello from Vue from DRF",
            students: []
            
        }
    },
    methods: {
        getAllStudents() {
            axios.get("http://127.0.0.1:8000/")
            .then((data) => {
                this.students = data.data
            })
        
        }


    },
    created() {
        this.getAllStudents()
    }

})

app.mount('#app')