function rollDice() {
    const dice = [...document.querySelectorAll(".die-list")];
    dice.forEach(die => {
        toggleClasses(die);
        die.dataset.roll = getRandomNumber();
    });
}

function toggleClasses(die) {
    die.classList.toggle("odd-roll");
    die.classList.toggle("even-roll");
}

function getRandomNumber() {
    $.get(
        {
            url: "/roll",
            success: function (data) {
                value = Math.floor(data["value"]);
            },
            async: false
        }
    )
    console.log(value);
    return value;
}

document.getElementById("roll-button").addEventListener("click", rollDice);
