
let limit = prompt("How many pokemon?")
let offset = 0

// The defacto way to make http requests is using Fetch
let pokeURL = `https://pokeapi.co/api/v2/pokemon?limit=${limit}&offset=${offset}`

fetch(pokeURL)
.then(function(response) {
    return response.json()
})
.then(function(data) {
    console.log(data)
})
.catch(function(err){
    console.info(err)
})
