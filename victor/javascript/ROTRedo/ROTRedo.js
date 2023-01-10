/*
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.
*/

const ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


const direction = prompt("Type 'encode' to encrypt, type 'decode' to decrypt:\n").toLowerCase()
let message = prompt("Whats your message?\n ")
let shift = prompt("Enter the amount of rotation:\n")
let output = ""
// Allow the user to input the amount of rotation used in the encryption.
shift = shift % 26
if (direction === "decode"){
    shift *= -1
}

for (let char of message){
    
    if (ALPHABET.includes(char)){
        let position = ALPHABET.indexOf(char)
        let new_position = position + shift
        output += ALPHABET[new_position]
        console.log(char)
    }
}


alert(`Your ${direction}d phrase is now:\n${output}`)