



navigator.geolocation.getCurrentPosition(returnPosition)

function returnPosition(position) {
    lat = position.coords.latitude
    long = position.coords.longitude
    console.log(`Lat: ${lat} Long: ${long}`)
}

    axios({
        method: 'post',
        url: 'https://api.openweathermap.org/data/2.5/weather',
        params: {
            lat : 35.962719796966304,
            lon : -114.84043915487283,
            appid : weather_key
        }})
    .then(function(data) {
        console.log(data.data.main.temp)
    })

