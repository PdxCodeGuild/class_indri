let locationInput = document.querySelector('#locationInput')
let submitBtn = document.querySelector('#submitBtn')
let weatherResult = document.querySelector('#weatherResult')
let divResult = document.querySelector('#divResult')
let spanCityName = document.querySelector('#spanCityName')


submitBtn.addEventListener('click', getLocation);
function getLocation(){
  divResult.innerHTML = ''
  let cityName = locationInput.value

  console.log(cityName);
  // navigator.geolocation.getCurrentPosition(position => {
  //   locLat = position.coords.latitude
  //   locLong = position.coords.longitude
    // console.log(locLat, locLong);
    axios ({
      method: 'get',
      url: `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=imperial&appid=${API_key}`
    }).then(response => {
      // Handle successful response
      let numTemp = document.createElement('p')
      numTemp.id = 'numTemp'
      numTemp.textContent = 'Temperature:' + ' ' +response.data.main.temp+'˚F'
  

      let locName = document.createElement('p')
      locName.id = 'locName'
      locName.textContent = 'City:' + ' ' +response.data.name

      
      
      //converting unix time to date
      let unixTime = response.data.dt
      let date = new Date(unixTime * 1000)
      let day = date.getDate()
      let month = date.getMonth()
      let year = date.getFullYear()
      let hours = date.getHours()
      let minutes = "0" + date.getMinutes()

      let formattedTime = month + '/' + day + '/' + year + ' ' + hours + ':' + minutes.substr(-2)
      spanCityName.textContent = response.data.name+ ' '+ 'as of'+ ' '+formattedTime
      console.dir(spanCityName.textContent);


      let feelsLikeTemp = document.createElement('p')
      feelsLikeTemp.id = 'feelsLike'
      feelsLikeTemp.textContent = 'Feels like:' + " " +response.data.main.feels_like+'˚F'
      
      let tempMax = document.createElement('p')
      tempMax.id = 'tempMax'
      tempMax.textContent = 'High:' + " " +response.data.main.temp_max+'˚F'

      let tempMin = document.createElement('p')
      tempMin.id = 'tempMin'
      tempMin.textContent = 'Low:' + " " +response.data.main.temp_min+'˚F'

      let humidity = document.createElement('p')
      humidity.id = 'humidity'
      humidity.textContent = 'Humidity:' + " " +response.data.main.humidity+'%'

      let weatherIcon = document.createElement('img')
      weatherIcon.id = 'weatherIcon'
      weatherIcon.src = `http://openweathermap.org/img/w/${response.data.weather[0].icon}.png`

      divResult.append(weatherIcon)
      divResult.append(numTemp)
      divResult.append(feelsLikeTemp)
      divResult.append(tempMax)
      divResult.append(tempMin)
      divResult.append(humidity)
  
      console.log(response.data);
    }).catch(error => {
      // Handle error
      console.log(error);
    });
  // })
  locationInput.value = ''
}

