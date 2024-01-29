// Convert time to a format of hours, minutes, seconds, and milliseconds

var minute = 0;
var second = 0;

getTotalTime();
getTotalQuestion()



function timeToString(time) {
	
  let diffInHrs = time / 3600000;
  let hh = Math.floor(diffInHrs);

  let diffInMin = (diffInHrs - hh) * 60;
  let mm = Math.floor(diffInMin);

  let diffInSec = (diffInMin - mm) * 60;
  let ss = Math.floor(diffInSec);

  let diffInMs = (diffInSec - ss) * 100;
  let ms = Math.floor(diffInMs);

  let formattedMM = mm.toString().padStart(2, "0");
  let formattedSS = ss.toString().padStart(2, "0");
  let formattedMS = ms.toString().padStart(2, "0");

  return `${formattedMM}:${formattedSS}:${formattedMS}`;
}

// Declare variables to use in our functions below

let startTime;
let elapsedTime = 0;
let timerInterval;

// Create function to modify innerHTML

function print(txt) {
  document.getElementById("display").innerHTML = txt;
}

// Create "start", "pause" and "reset" functions

function start() {
  startTime = Date.now() - elapsedTime;
  timerInterval = setInterval(function printTime() {
    elapsedTime = Date.now() - startTime;
    print(timeToString(elapsedTime));
  }, 10);
  showButton("PAUSE");
}

function pause() {
  clearInterval(timerInterval);
  showButton("PLAY");
}

function reset(time) {
  
  
  let diffInHrs = time / 3600000;
  let hh = Math.floor(diffInHrs);

  let diffInMin = (diffInHrs - hh) * 60;
  minute = Math.floor(diffInMin);

  let diffInSec = (diffInMin - minute) * 60;
  second = Math.floor(diffInSec);
  
  
  clearInterval(timerInterval);
  print("00:00:00");
  elapsedTime = 0;
  showButton("PLAY");
}

var modal = document.querySelector("#modal_chronometer")
var modal_btn_cancel = document.querySelector("#cancel_modal")
var body = document.querySelector("body")



// Create function to display buttons

function showButton(buttonKey) {
  const buttonToShow = buttonKey === "PLAY" ? playButton : pauseButton;
  const buttonToHide = buttonKey === "PLAY" ? pauseButton : playButton;
  buttonToShow.style.display = "block";
  buttonToHide.style.display = "none";
}
// Create event listeners

let playButton = document.getElementById("playButton");
let pauseButton = document.getElementById("pauseButton");
let resetButton = document.getElementById("resetButton");

playButton.addEventListener("click", start);
pauseButton.addEventListener("click", pause);
resetButton.addEventListener("click", function() {
	reset(elapsedTime);
});
resetButton.addEventListener("click", function() {
	modal.style.display = "initial";
	
	var minute_area = document.querySelector("#minute")
	var second_area = document.querySelector("#second")
	
	minute_area.value = minute
	second_area.value = second
})
modal_btn_cancel.addEventListener("click", function() {
	modal.style.display = "none";
})




function getTotalTime() {
	
	times = document.querySelectorAll("#chronometer-table tbody tr");

	var seconds = 0;
	times.forEach((time) => {
		let sure = time.children[3].textContent;
		let minute = Number(sure.split(":")[0])
		let second = Number(sure.split(":")[1])
		
		seconds += minute * 60 + second
	});
	
	var minute = Math.floor(seconds / 60);
	var second = seconds % 60
	
	var timeTotal = document.querySelector("#time-total")

	timeTotal.textContent = `${minute} dakika ${second} saniye`;
}

function getTotalQuestion() {
	
	times = document.querySelectorAll("#chronometer-table tbody tr");

	var questions = 0;
	times.forEach((time) => {
		let question = Number(time.children[4].textContent);
		questions += question
	});
	
	
	
	var questionTotal = document.querySelector("#chrono-question-total")

	questionTotal.textContent = `${questions} soru`;
	
}