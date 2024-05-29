import { Game } from "./game.js";

export class Card {
  constructor(image) {
    this.image = image;
    this.matched = false;
    this.element = document.createElement("div");
    this.element.classList.add("card");
    this.element.style.backgroundImage = `url(${this.image})`;
    this.element.addEventListener("click", this.reveal.bind(this));
  }

  hide() {
    this.element.style.backgroundImage = "";
    this.element.classList.remove("revealed");
  }

  unhide() {
    this.element.style.backgroundImage = `url(${this.image})`;
    this.element.classList.add("revealed");
  }

  reveal() {
    if (!this.matched && Game.revealedCards.length < 2) {
      this.unhide();
      Game.revealedCards.push(this);
      if (Game.revealedCards.length === 2) {
        setTimeout(() => Game.checkMatch(), 500);
      }
    }
  }

  matchFound() {
    this.matched = true;
    this.element.classList.add("matched");
  }
}
