let locationInput = document.querySelector('#locationInput')
let submitBtn = document.querySelector('#submitBtn')
let weatherResult = document.querySelector('#weatherResult')
let divResult = document.querySelector('#divResult')


submitBtn.addEventListener('click', getLocation);
function getLocation(){
  let cityName = locationInput.value
  // navigator.geolocation.getCurrentPosition(position => {
  //   locLat = position.coords.latitude
  //   locLong = position.coords.longitude
    // console.log(locLat, locLong);
    axios ({
      method: 'get',
      url: `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=imperial&appid=${API_key}`
    }).then(response => {
      // Handle successful response
      let locName = document.createElement('p')
      locName.id = 'locName'
      locName.textContent = 'City:' + ' ' +response.data.name
      console.log(locName);

      let numTemp = document.createElement('p')
      numTemp.id = 'numTemp'
      numTemp.textContent = 'Temperature:' + ' ' +response.data.main.temp+'F'
      console.log(numTemp);

      let feelsLikeTemp = document.createElement('p')
      feelsLikeTemp.id = 'feelsLike'
      feelsLikeTemp.textContent = 'Feels like:' + " " +response.data.main.feels_like+'F'
      console.log(feelsLikeTemp);

      divResult.append(locName)
      divResult.append(numTemp)
      divResult.append(feelsLikeTemp)
  
      console.log(response.data);
    }).catch(error => {
      // Handle error
      console.log(error);
    });
  // })
  
}

