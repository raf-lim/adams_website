import { Card } from "./card.js";

export class Game {
  static images = [];
  static cards = [];
  static board = document.querySelector(".game-board");
  static startBtn = document.querySelector(".startBtn");
  static timer = document.getElementById("timer");
  static startTime = null;
  static interval = null;
  static revealedCards = [];
  static matchedPairs = 0;

  static shuffle(cards) {
    for (let i = cards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [cards[i], cards[j]] = [cards[j], cards[i]];
    }
    return cards;
  }

  static checkMatch() {
    if (this.revealedCards[0].image === this.revealedCards[1].image) {
      this.revealedCards[0].matchFound();
      this.revealedCards[1].matchFound();
      this.matchedPairs++;

      if (this.matchedPairs === 9) {
        clearInterval(this.interval);
        alert(
          "Congratulations! Your time is: " +
            this.timer.textContent +
            " seconds"
        );
        this.revealedCards.length = 0;
        this.matchedPairs = 0;
        this.startBtn.style.display = "block";
        this.timer.textContent = 0;
        this.createCards();
        this.createBoard();
      }
    } else {
      this.revealedCards[0].hide();
      this.revealedCards[1].hide();
    }
    this.revealedCards = [];
  }

  static runStopwatch() {
    this.startTime = Date.now();
    this.interval = setInterval(() => {
      this.timer.textContent = ((Date.now() - this.startTime) / 1000).toFixed(
        2
      );
    }, 100);
  }

  static createCards() {
    this.cards.length = 0;
    this.cards = this.images
      .concat(this.images)
      .map((image) => new Card(image));
  }

  static createBoard() {
    this.board.innerHTML = "";
    this.shuffle(this.cards).forEach((card) => {
      this.board.appendChild(card.element);
      card.hide();
    });
  }

  static start(images) {
    this.images = images;
    this.createCards();
    this.createBoard();
    this.startBtn.style.display = "block";
    this.startBtn.addEventListener("click", (e) => {
      this.cards.forEach((card) => card.unhide());
      setTimeout(() => {
        this.cards.forEach((card) => card.hide());
        this.runStopwatch();
      }, 3000);
      e.target.style.display = "none";
    });
  }
}
