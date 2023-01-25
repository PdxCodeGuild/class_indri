// This gets the latitude and longitude
const locationDiv =document.querySelector('#location')
const generateLocation =document.querySelector('#generateLocation')


generateLocation.addEventListener("click", function(){
 
 navigator.geolocation.getCurrentPosition(async position => {
        let latitude=(position.coords.latitude)
        let longitude=(position.coords.longitude)
        let weather= await getweather(latitude, longitude)
        renderdiv(weather)
    })
})

function getweather(latitude, longitude){
    let weatherURL=`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${keys}&units=imperial`
   const weatherResults = fetch(weatherURL)
    .then(function(response) {
        return response.json()
    })
    .then(function(weatherData) {
        return weatherData
    })
    .catch(function(err){
        console.info(err)
    }) 
    return weatherResults
}


function renderdiv(weather){
     // Adding to DOM
    let unix_timestamp = weather.dt
    let dateTime = new Date(unix_timestamp*1000)
    let date= document.createElement('p')
    date.textContent=`Date: ${dateTime}`
    locationDiv.appendChild(date)

    let city =document.createElement('p')
    city.textContent=`City: ${weather.name}`
    locationDiv.appendChild(city)

    let sky =document.createElement('p')
    sky.textContent=`Weather: ${weather.weather[0].main}: ${weather.weather[0].description}`
 
    
    locationDiv.appendChild(sky)

    let temp =document.createElement('p')
    temp.textContent=`Tempature: ${weather.main.temp}`
    locationDiv.appendChild(temp)

    let icon=document.createElement('img')
    icon.setAttribute('src', `http://openweathermap.org/img/wn/${weather.weather[0].icon}.png`)
    locationDiv.appendChild(icon)
}
