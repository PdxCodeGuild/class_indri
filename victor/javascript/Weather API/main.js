navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude)
    console.log(position.coords.longitude)
})
let lat = position.coords.latitude
let lon = position.coords.longitude

axios({
    method: 'get',
    url: `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}lon=${lon}&exclude=hourly,daily&appid=${API_KEY}`
    
  }).then((response) => {
    console.log(response.data)
  })
