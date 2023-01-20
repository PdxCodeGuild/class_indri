let userLocation = document.querySelector('#user-location')
let outsideTemp = document.querySelector('#outside-temp')
let weatherConditions = document.querySelector('#weather-conditions')
let windConditions = document.querySelector('#wind-conditions')



const compass = [
        {minDegree: 0, maxDegree:22.5 , direction: "N"},
        {minDegree: 22.6, maxDegree: 67.5, direction: "NE"},
        {minDegree: 67.6, maxDegree:112.5 , direction: "E"},
        {minDegree: 112.6, maxDegree:157.5 , direction: "SE"},
        {minDegree: 157.6, maxDegree:202.5 , direction: "S"},
        {minDegree: 202.6, maxDegree:247.5 , direction: "SW"},
        {minDegree: 247.6, maxDegree:292.5 , direction: "W"},
        {minDegree: 292.6, maxDegree:337.5 , direction: "NW"},
        {minDegree: 337.6, maxDegree:360 , direction: "N"},
]



navigator.geolocation.getCurrentPosition(returnWeather)

function returnWeather(position) {    
    axios({
        method: 'post',
        url: 'https://api.openweathermap.org/data/2.5/weather',
        params: {
            lat : position.coords.latitude,
            lon : position.coords.longitude,
            appid : weather_key
        }})
        .then(function(data) {
            // return data
            let weatherData = (data.data)
            
            // location name
            userLocation.textContent = weatherData.name


            // temps
            let tempKelvin = weatherData.main.temp
            let tempCelsius = (Math.round(tempKelvin - 273.15))
            let tempFahrenheit = (Math.round(tempCelsius) * 9 / 5 + 32)
            
            outsideTemp.textContent = `${tempFahrenheit}º`
            
            // weather
            weatherConditions.textContent = weatherData.weather[0].description
            
            // wind
            let windSpeed = weatherData.wind['speed']
            let windDeg = Math.abs(weatherData.wind['deg'])
            let windDirection = ""

            heading = Math.abs(windDeg % 360)

            compass.forEach((object) => {

                if (heading == object.minDegree || heading == object.maxDegree){
                    console.log(object.direction)
                    windDirection = object.direction;}

                if (heading > object.minDegree && heading < object.maxDegree) {
                    console.log(object.direction)
                    windDirection = object.direction;}
            
                }
            )

            windConditions.textContent = `Wind Speed: ${windSpeed}mph, Heading: ${windDeg}º, Direction: ${windDirection}`

            console.log(weatherData)
        })
}

// 