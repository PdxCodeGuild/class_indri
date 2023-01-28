


const { createApp } = Vue;

const app = createApp({
  delimiters: ['[[', ']]'],
  data() {
    return {
      students: [],
    }
  },
  methods: {
    getStudents() {
      axios.get('http://localhost:8000/apiApp/v1/')
        .then((data) => {
          this.students = data.data
          console.log(data);
        })
    }
  },
  created() {
    this.getStudents()
  }
})
app.mount('#app')