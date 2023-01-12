

// Objects

let contact = {
    "name": "Carl",
    "number": "1234567890",
    thirdKey: "Happy Friday!"
}

// console.log(contact['name'])
// console.log(contact.name)

// console.log(contact['thirdKey'])
// console.log(contact.thirdKey)


let library_user = {
    first_name: 'Jane',
    last_name: 'Smith',
    age: 20,
    books: [{
        title: 'A Wrinkle in Time',
        author: 'Madeleine L\'Engle',
        published: 1962
    },{
        title: 'The Giving Tree',
        author: 'Shel Silverstein',
        published: 1964
    }]
}

// Log the first book under library user
// console.log(library_user['books'][0]['title'])
// console.log(library_user['books'][0].title)

// Log the second published date
// console.log(library_user.books[1].published)

let books = library_user.books

// for in iterates over indexes
for (let book in books){ // for i in range()
    console.log(book)
}

// for of iterates over elements
for (let book of books){ // for book in books
    console.log(book.author)
}

// Iterate given number of times using a counter
// let counter = 0
// while(counter < 100){
//     console.log(counter, "TGIF")
//     // counter += 1
//     counter++
//     if (counter === 32){
//         break
//     }
// }

// Iterate given number of times using a counter
for(let counter = 0; counter < 100; counter++){
    console.log("TGIF", counter)
}


// Arrays


let fruits = ["strawberry", "banana", "kiwi", "peach"]
console.log(fruits[0]) // We can use [index] just like with python, but we can not use negative indexes
console.log(fruits.at(-1)) // If se use the .at() method, we can use negative indexes

fruits[0] = "apple"

// Add element to end of array
fruits.push("dragon fruit")

// Add element to begining of array
fruits.unshift("cucumber")

console.log(fruits)

// Remove element from end of array
let lastItem = fruits.pop()

// Remove element from begining of array
let firstItem = fruits.shift()

console.log(fruits)

// Remove items starting at (first argument, number items to remove, items to add)
let removedItems = fruits.splice(1, 1, "pineapple", "blueberry", "guava", "coconut")

fruits.sort() // [ "apple", "blueberry", "coconut", "guava", "kiwi", "peach", "pineapple" ]

fruits.slice(1, 3) // [ "blueberry", "coconut" ]

fruits.reverse() // [ "pineapple", "peach", "kiwi", "guava", "coconut", "blueberry", "apple" ]

fruits.sort() // [ "apple", "blueberry", "coconut", "guava", "kiwi", "peach", "pineapple" ]

fruits.join(" - ") // "apple - blueberry - coconut - guava - kiwi - peach - pineapple"

fruits.length // 7 

