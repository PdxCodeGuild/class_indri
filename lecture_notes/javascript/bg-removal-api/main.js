
const uploadButton = document.querySelector("#upload-button")
const uploadInput = document.querySelector("#upload-input")


uploadButton.addEventListener("click", function(){
    // Get access to image
    let image_url = uploadInput.value
    submitImage(image_url)
    
})

// Send image to api
function submitImage(image){
    console.log(image)
    axios({
        method: "post",
        url: "https://api.remove.bg/v1.0/removebg",
        data: {
            "image_url": image
        },
        headers: {
            "X-API-Key": API_KEY
        }
    }).then(function(data){
        // Display result
        console.log(data)
        let img = document.createElement("img")
        img.src = 'data:image/jpeg;base64,' + btoa(data.data)
        document.body.append(img)

    })
}