let time, date, hmsTime;

let timeText = document.getElementById("timeText");
let dateText = document.getElementById("dateText");

setTimeout(startClock(), 1000 - new Date().getMilliseconds());

function startClock() {
  clock = setInterval(updateTime, 1000);
}

function updateTime() {
  time = new Date().toLocaleString();
  let temp = time.split(",");
  dateText.textContent = temp[0];
  timeText.textContent = temp[1];
}
