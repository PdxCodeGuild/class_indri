let userLocation = document.querySelector('#user-location')
let userTime = document.querySelector('#user-time')
let currentTemp = document.querySelector('#outside-temp')
let minMaxTemp = document.querySelector('#min-max-temp')
let weatherConditions = document.querySelector('#weather-conditions')
let windConditions = document.querySelector('#wind-conditions')

let weatherForecast = document.querySelector('#weather-forecast')


const compass = [
        {minDegree: 0, maxDegree:22.5 , direction: "North"},
        {minDegree: 22.6, maxDegree: 67.5, direction: "NorthEast"},
        {minDegree: 67.6, maxDegree:112.5 , direction: "East"},
        {minDegree: 112.6, maxDegree:157.5 , direction: "SouthEast"},
        {minDegree: 157.6, maxDegree:202.5 , direction: "South"},
        {minDegree: 202.6, maxDegree:247.5 , direction: "SouthWest"},
        {minDegree: 247.6, maxDegree:292.5 , direction: "West"},
        {minDegree: 292.6, maxDegree:337.5 , direction: "NorthWest"},
        {minDegree: 337.6, maxDegree:360 , direction: "North"},
]


// Current Weather
navigator.geolocation.getCurrentPosition(currentWeather)

function currentWeather(position) {    
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
            
            // location
            userLocation.textContent = weatherData.name

            // time
            let dateTime = new Date(weatherData.dt * 1000)
            let hour = dateTime.getHours()
            if (hour > 12) {
                hour = (hour%12),
                period = "PM"
            }
            else {
                period = "AM"
            }
            let minute = dateTime.getMinutes()
            userTime.textContent = `${hour}:${minute} ${period}`


            // temps
            let temp = weatherData.main.temp
            let minTemp = weatherData.main.temp_min
            let maxTemp = weatherData.main.temp_max
            
            // TODO add toggle to switch between F and C
            // convert to celsius
            function toCelsius(kelvin) {
                return (Math.round(kelvin - 273.15))
            }

            // convert to fahrenheit
            function toFahrenheit(kelvin) {
                return (Math.round((kelvin - 273.15) * 9 / 5 + 32))
            }

            currentTemp.textContent = `${toFahrenheit(temp)}º F`
            minMaxTemp.textContent = `High: ${toFahrenheit(maxTemp)}º F | Low: ${toFahrenheit(minTemp)}º F`
            
            // weather
            weatherConditions.textContent = weatherData.weather[0].description
            
            // weather icon
            let iconCode = weatherData.weather[0].icon
            let weatherIcon = document.createElement("img");
            weatherIcon.src =`https://openweathermap.org/img/wn/${iconCode}@2x.png`;

            weatherConditions.appendChild(weatherIcon)
            
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

            windConditions.textContent = `Wind: ${windSpeed}mph from the ${windDirection}`

            console.log(weatherData)
        })
}


// Forecast Weather
navigator.geolocation.getCurrentPosition(forecastWeather)

function forecastWeather(position) {    
    axios({
        method: 'post',
        url: 'https://api.openweathermap.org/data/2.5/forecast',
        params: {
            lat : position.coords.latitude,
            lon : position.coords.longitude,
            appid : weather_key
        }})
        .then(function(data) {
            // return data
            let forecastData = (data.data)
            console.log(forecastData)
            
            for (let i in forecastData.list){

                // forecast data is in 3 hour steps. Return only 12 hour steps.
                if (i == 0 || i % 4 == 0) {
                
                    // each forecast gets its own div
                    let dailyForecast = document.createElement('div')
                    weatherForecast.appendChild(dailyForecast)

                    // date
                    let dateTime = new Date(forecastData.list[i].dt * 1000)

                    let forecastDate = document.createElement('p')
                    forecastDate.innerHTML = dateTime
                    dailyForecast.appendChild(forecastDate)

                    // temp
                    let forecastTemp = document.createElement('h1')
                    
                    let temp = forecastData.list[i].main.temp
                    let minTemp = forecastData.list[i].main.temp_min
                    let maxTemp = forecastData.list[i].main.temp_max
                    
                    function toCelsius(kelvin) {
                        return (Math.round(kelvin - 273.15))
                    }
        
                    function toFahrenheit(kelvin) {
                        return (Math.round((kelvin - 273.15) * 9 / 5 + 32))
                    }
        
                    
                    forecastTemp.innerHTML = `${toFahrenheit(temp)}º F`
                    dailyForecast.appendChild(forecastTemp)
                    
                    
                    // weather
                    let dailyWeather = document.createElement('h3')
                    dailyWeather.innerHTML = forecastData.list[i].weather[0].description
                    dailyForecast.appendChild(dailyWeather)
                    
                    // weather icon
                    let iconCode = forecastData.list[i].weather[0].icon
                    let weatherIcon = document.createElement("img");
                    weatherIcon.src =`https://openweathermap.org/img/wn/${iconCode}@2x.png`;
                    dailyWeather.appendChild(weatherIcon)



                    weatherForecast.appendChild(dailyForecast)
            }
        }})
}