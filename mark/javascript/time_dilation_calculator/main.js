// Time Dilation Calculator
// Δt_relative = Δt * γ = Δt * √(1 – v²/c²)


// c refers to the speed of light
const c = "670616629.38" //converted to miles per hour.

// v refers to the speed of the observer who’s traveling
let v = (prompt("Look! An alien space craft! How fast is it going? (miles per hour, max 670616629.38): ") % c)

// Δt refers to the time which has passed as measured by the observer who isn’t moving
let t = prompt("How long have you been looking at it? (Hour(s)): ")

// γ refers to the Lorentz factor.
velocity = Math.pow(v, 2)
constant = Math.pow(c, 2)
let y = (1/Math.sqrt(1 - velocity/constant))

// Δt_relative refers to the time which has passed. It’s measured by the observer who’s traveling
let relative = (t * y)
let difference = (relative - t)

alert("The UFO has experienced " + difference + " more hours than you have.")