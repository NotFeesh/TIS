let [hours, minutes, seconds] = [0, 0, 0];
let hourInput = document.getElementById("hours");
let minuteInput = document.getElementById("minutes");
let secondInput = document.getElementById("seconds");

let timer = null;
let timerActive = false;

let display = document.getElementById("displayText");

let timerSound = new Audio("alarmsound.mp3");

document.addEventListener("keyup", (event) => {
  if (event.code === "Enter") {
  }
});

setup();

function setup() {
  stopTimer();
  timerSound.pause();
  hours = hourInput.value == null ? 0 : hourInput.value;
  minutes = minuteInput.value == null ? 0 : minuteInput.value;
  seconds = secondInput.value == null ? 0 : secondInput.value;
  updateScreen();
}

function updateScreen() {
  display.textContent = `${hours}:${("00" + minutes).slice(-2)}:${(
    "00" + seconds
  ).slice(-2)}`;
}

function start() {
  if (!timerActive) {
    timerActive = true;
    timer = setInterval(timerLogic, 1000);
  }
}

function stopTimer() {
  if (timerActive) {
    timerActive = false;
    clearInterval(timer);
  }
}

function timerLogic() {
  seconds--;
  if (seconds < 0) {
    seconds = 59;
    minutes--;
    if (minutes < 0) {
      minutes = 59;
      hours--;
      if (hours < 0) {
        [hours, minutes, seconds] = [0, 0, 0];
        stopTimer();
        timerSound.play();
      }
    }
  }
  updateScreen();
}
