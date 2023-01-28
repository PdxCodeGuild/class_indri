
const { createApp } = Vue

const app = createApp ({
    delimiters: ['[[',']]'],
    data() {
            return {
                studentList: []
        }
    },
    methods: {
        getStudentList() {
            axios.get("http://127.0.0.1:8000/api/v1")
            .then((data) => {
                this.studentList = data.data
            })
        },
    },
    created() {
        this.getStudentList()
    }
})

app.mount('#app')