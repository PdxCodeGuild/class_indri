/*
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.
*/

const ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


const direction =  document.querySelector('#direction')
let message = document.querySelector('#message')
let shift = document.querySelector('#shift')
let output = ""
// Allow the user to input the amount of rotation used in the encryption.
userInput = document.querySelector('.message')
btn = document.querySelector('#submit')
function encrypt (){
    shift = shift.value % 26

    if (direction.value === "decode"){
        shift *= -1
    }
    
    for (let char of message.value){
        
        if (ALPHABET.includes(char)){
            let position = ALPHABET.indexOf(char)
            let newPosition = position + shift
            output += ALPHABET[newPosition]
            
        }
    }
    alert(`Your ${direction}d phrase is now:\n${output}`)
}
btn.onclick = encrypt
shift.addEventListener("keydown", function(event){
    if (event.key === "Enter"){
        encrypt()
    }
})