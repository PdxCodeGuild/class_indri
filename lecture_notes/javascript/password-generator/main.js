let characterSelect = document.querySelector("#characterSelect")
let generateBtn = document.querySelector("#generateBtn")
let uppercase = document.querySelector("#uppercase")
let numbers = document.querySelector("#numbers")
let specialCharacters = document.querySelector("#specialCharacters")
let output = document.querySelector("#output")


for(let i = 0; i < 32; i++){
    let option = document.createElement('option')
    option.textContent = i + 1
    option.value = i + 1

    characterSelect.appendChild(option)
}

generateBtn.addEventListener("click", function() {
    let alphabet = "abcdefghijklmnopqrstuvwxyz"

    if(uppercase.checked){
        alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    }

    if(numbers.checked){
        alphabet += "1234567890"
    }

    if(specialCharacters.checked){
        alphabet += "!@#$%^&*()_+-=`~,./<>?;':"
    }

    let password = ""
    for(let i = 0; i < characterSelect.value; i++){
        let index = Math.floor(Math.random() * alphabet.length)  // 33
        password += alphabet[index]
    }

    output.textContent = password
})


let buttons = document.querySelectorAll(".numberBtn")

// for(let button of buttons){
//     button.addEventListener("click", function() {
//         console.log(button.textContent)
//     })
// }

buttons.forEach(function(button){
    button.addEventListener("click", function() {
        console.log(button.textContent)
    })
})