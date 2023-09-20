function rollDice() {
    const dice = [...document.querySelectorAll(".die-list")];
    dice.forEach(die => {
        toggleClasses(die);
        die.dataset.roll = getRandomNumber(1, 6);
    });
}

function toggleClasses(die) {
    die.classList.toggle("roll");
}

function getRandomNumber(min, max) {
    // TODO: Replace this function by a call to webserver
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.getElementById("roll-button").addEventListener("click", rollDice);
