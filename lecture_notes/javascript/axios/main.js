
let limit = prompt("How many pokemon?")
let pokeURL = "https://pokeapi.co/api/v2/pokemon"

function getPokemon(pokeURL) {
    axios.get(pokeURL, {
        params: {
            limit: limit,
            offset: 0
        }
    })
    .then(function(response) {
        console.log(response)
    })
    .catch(function(err){
        console.info(err)
    })
}

// axios({
//     method: "get",
//     url: pokeURL,
//     params: {
//         limit: limit,
//         offset: 0
//     }
// }).then(function(response) {
//     console.log(response)
// }).catch(function(err){
//     console.info(err)
// })
