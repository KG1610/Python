console.log('Connected')

//Restart Game Button
var restart = document.querySelector("#b")

//Grab all squares
var squares = document.querySelectorAll("td")

//clear all the squares
function ClearBoard() {
    for (var i = 0; i < squares.length; i++ ) {
    squares[i].textContent = ''
    }
}

restart.addEventListener('click', ClearBoard)

