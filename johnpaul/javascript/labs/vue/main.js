const { createApp } = Vue

const app = createApp({
  data() {
    return {
      convertNumber: '',
      numPhrase: {
        single_digits: {
          0: "zero",
          1: "one",
          2: "two",
          3: "three",
          4: "four",
          5: "five",
          6: "six",
          7: "seven",
          8: "eight",
          9: "nine"
        },
        tens_digits: {
          0: "",
          1: "eleven",
          2: "twelve",
          3: "thirteen",
          4: "fourteen",
          5: "fifteen",
          6: "sixteen",
          7: "seventeen",
          8: "eighteen",
          9: "nineteen"
        },

        double_digits: {
          0: "",
          1: "ten",
          2: "twenty",
          3: "thirty",
          4: "forty",
          5: "fifty",
          6: "sixty",
          7: "seventy",
          8: "eighty",
          9: "ninety"
        },
      }
    }
  },
  methods: {
    convert() {
      let num = this.convertNumber
      let numStr = num.toString()
      let numLength = numStr.length
      let numPhrase = ''
      let numArray = numStr.split('')

      if (numLength == 1) {
        numPhrase = this.numPhrase.single_digits[numArray[0]]
      } else if (numLength == 2) {
        if (numArray[0] == 1) {
          numPhrase = this.numPhrase.tens_digits[numArray[1]]
        } else {
          numPhrase = this.numPhrase.double_digits[numArray[0]] + '-' + this.numPhrase.single_digits[numArray[1]]
        }
      } else if (numLength == 3) {
        numPhrase = this.numPhrase.single_digits[numArray[0]] + ' hundred'
        if (numArray[1] == 1) {
          numPhrase += ' and ' + this.numPhrase.tens_digits[numArray[2]]
        } else if (numArray[1] == 0) {
          numPhrase += ' and ' + this.numPhrase.single_digits[numArray[2]]
        } else {
          numPhrase += ' and ' + this.numPhrase.double_digits[numArray[1]] + '-' + this.numPhrase.single_digits[numArray[2]]
        }
      }
      console.log(numPhrase);
    }
  }
})
app.mount('#app')