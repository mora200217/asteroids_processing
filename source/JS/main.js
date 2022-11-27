// main.js 

// variables 
let w, h; 
// constantes 


function setup(){
    createCanvas(window.innerWidth, window.innerHeight); 
    w = window.innerWidth; 
    h = window.innerHeight; 
}

function draw(){
    background(0); 
    fill(255); 
    ellipse(w/2, h/2, 20, 20); 
}

/**
 * Listener de reajuste de dimensión de canvas. 
 * 
 */
function windowResized() {
    resizeCanvas(window.innerWidth, window.innerHeight);
    w = window.innerWidth; 
    h = window.innerHeight; 
  }