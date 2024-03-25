let [hours, minutes, seconds, ms] = [0, 0, 0, 0];

timer = null;
timerActive = false;
let display = document.getElementById("displayText");
let startButton = document.getElementById("startButton");
let stopButton = document.getElementById("stopButton");
let resetButton = document.getElementById("resetButton");

// Key Listeners
document.addEventListener("keyup", (event) => {
  if (event.code === "Space") {
    if (timerActive == false) {
      start();
    } else {
      stopTimer();
    }
  }
});

document.addEventListener("keyup", (event) => {
  if (event.code === "KeyR") {
    reset();
  }
});

// Button Functionality
function start() {
  if (timerActive == false) {
    timerActive = true;
    timer = setInterval(stopwatch, 4);
    startButton.className = "btn btn-secondary";
    stopButton.className = "btn btn-danger";
    resetButton.className = "btn btn-primary";
  }
}

function stopTimer() {
  clear();
}

function reset() {
  clear();
  [hours, minutes, seconds, ms] = [0, 0, 0, 0];
  updateScreen();
  resetButton.className = "btn btn-secondary";
}

function clear() {
  clearInterval(timer);
  timerActive = false;
  startButton.className = "btn btn-primary";
  stopButton.className = "btn btn-secondary";
}

//Stopwatch Functionality
function stopwatch() {
  ms += 4;
  if (ms >= 1000) {
    ms -= 1000;
    seconds++;
    if (seconds == 60) {
      minutes++;
      if (minutes == 60) {
        hours++;
      }
    }
  }
  updateScreen();
}

function updateScreen() {
  display.textContent = formatTime(hours, minutes, seconds, ms);
}

function formatTime(hours, minutes, seconds, ms) {
  return `${("0" + hours).slice(-2)}:${("0" + minutes).slice(-2)}:${(
    "0" + seconds
  ).slice(-2)}:${("00" + ms).slice(-3)}`;
}
