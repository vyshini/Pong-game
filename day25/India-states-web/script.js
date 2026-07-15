const canvas = document.getElementById("mapCanvas");
const ctx = canvas.getContext("2d");

// Canvas size = image size
const canvasWidth = 400;
const canvasHeight = 467;
canvas.width = canvasWidth;
canvas.height = canvasHeight;

// Game state
let guessedStates = [];
let allStates = [];
let gameOver = false;
let timeLeft = 180; // 3 minutes
let timerInterval = null;

// DOM elements
const startBtn = document.getElementById("startBtn");
const guessBtn = document.getElementById("guessBtn");
const guessInput = document.getElementById("guessInput");
const timerDiv = document.getElementById("timer");
const counterDiv = document.getElementById("counter");
const resultDiv = document.getElementById("result");

// Load map image
const mapImage = new Image();
mapImage.src = "asset/India-state.png";
mapImage.onload = () => {
    // Draw map at original size
    ctx.drawImage(mapImage, 0, 0, canvasWidth, canvasHeight);
    updateCounter();
    updateTimer();
};

// Load states data (pixel coordinates)
fetch("asset/states.json")
    .then(res => res.json())
    .then(data => allStates = data);

// Draw guessed state
function drawState(state) {
    ctx.fillStyle = "black";
    ctx.font = "14px Arial";
    ctx.fillText(state.state, state.x, state.y);
}

// Update counter and timer
function updateCounter() {
    counterDiv.textContent = `Guessed: ${guessedStates.length}/29`;
}
function updateTimer() {
    timerDiv.textContent = `Time: ${timeLeft}s`;
}

// Countdown timer
function countdown() {
    timerInterval = setInterval(() => {
        if (gameOver) return;

        timeLeft--;
        updateTimer();

        if (timeLeft <= 0) {
            endGame(false);
        }
    }, 1000);
}

// Handle user guess
function handleGuess() {
    if (gameOver) return;

    const answer = guessInput.value.trim().toLowerCase();
    guessInput.value = "";

    if (!answer) return;

    const state = allStates.find(s => s.state.toLowerCase() === answer);

    if (state && !guessedStates.includes(state.state)) {
        guessedStates.push(state.state);
        drawState(state);
        updateCounter();
    }

    if (guessedStates.length === 29) {
        endGame(true, true);
    }
}

// End game
function endGame(userQuit = false, allGuessed = false) {
    gameOver = true;
    clearInterval(timerInterval);
    guessInput.disabled = true;
    guessBtn.disabled = true;

    if (userQuit) {
        resultDiv.textContent = `You quit! You guessed ${guessedStates.length}/29 states.`;
    } else if (allGuessed) {
        resultDiv.textContent = `🎉 Congratulations! You guessed all 29 states!`;
    } else {
        resultDiv.textContent = `⏰ Time's up! You guessed ${guessedStates.length}/29 states.`;
    }
}

// Start game
startBtn.addEventListener("click", () => {
    startBtn.style.display = "none";
    guessInput.disabled = false;
    guessBtn.disabled = false;
    guessInput.focus();

    guessedStates = [];
    timeLeft = 180;
    gameOver = false;
    ctx.drawImage(mapImage, 0, 0, canvasWidth, canvasHeight); // reset map
    updateCounter();
    updateTimer();
    countdown();
});

// Guess button click
guessBtn.addEventListener("click", handleGuess);

// Enter key triggers guess
guessInput.addEventListener("keyup", (e) => {
    if (e.key === "Enter") handleGuess();
});