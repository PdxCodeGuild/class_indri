const input = document.querySelector("#input")
const city = document.querySelector("#city")
const cityName = document.querySelector("#cityName")
const Temp = document.querySelector("#temp")
const main = document.querySelector("#main")
const description = document.querySelector("#description")
const image = document.querySelector("#image")

input.onsubmit = (obj) => {
  obj.preventDefault();
  weatherUpdate(city.value)
  city.value = ""
};

weatherUpdate = (city) => {
  const xhr = new XMLHttpRequest()
  xhr.open(
    "GET",
    `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}`)
  

  xhr.send();
  xhr.onload = () => {
    if (xhr.status === 404) {
      alert("Error, city not found")
    } else {
      let data = JSON.parse(xhr.response)
      cityName.innerHTML = data.name
      Temp.innerHTML = Math.round(1.8 * (data.main.temp-273) + 32) + 'ºF'
      main.innerHTML = data.weather[0].main + " "
      image.src = `http://openweathermap.org/img/wn/${data.weather[0].icon}.png`
    }
  };
};













// const genBtn = document.querySelector('#btn')
// const temp = document.querySelector('#temp')
// let lat
// let lon

// function position() {
//     navigator.geolocation.getCurrentPosition(position => {
//         lat = position.coords.latitude
//         lon = position.coords.longitude
//         console.log(lat, lon)
//     })

// }

// genBtn.addEventListener('click', function(){
//     axios({
//         method: 'get',
//         url: `https://api.openweathermap.org/data/2.5/weather?lat=${33.44}&lon=${-94.04}&appid=${API_KEY}`
//       }).then(function(response) {
//         console.dir(response.data)
//         temp.innerHTML = response.main.temp
       



        // let result = document.createElement('div')
        // result.className = 'result'
        // for (let key in response.data) {
        //     let weatherSnippet = document.createElement('p')
        //     let obj = response.data[key]
        //     if (typeof obj === 'object'){
        //         for (let key in obj){
        //             let value = obj[key]
        //             console.log(typeof value)
        //             if (typeof value === 'object'){
        //                 for(let key in value) {
        //                     let p = document.createElement('p')
        //                     p.textContent = value[key]
        //                     result.appendChild(p)
        //                 }
        //             }
        //             else {
        //                 weatherSnippet.innerText = key + ': ' + value
        //                 result.appendChild(weatherSnippet)
        //             }
        //         }
                
        //     }
        //     else if (typeof obj === 'array'){
        //         weatherSnippet.innerText = obj[0]
        //         result.appendChild(weatherSnippet)
        //     }
        //     else {
        //         weatherSnippet.innerText = obj
        //         result.appendChild(weatherSnippet)
            //  }


             
            // document.body.append(result)

        // }
//       })

// })

