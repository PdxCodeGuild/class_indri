let locationInput = document.querySelector('#locationInput')
let submitBtn = document.querySelector('#submitBtn')
let weatherResult = document.querySelector('#weatherResult')


function getLocation(){
  navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude)
    console.log(position.coords.longitude)
  })
}

submitBtn.addEventListener('click', getLocation())

