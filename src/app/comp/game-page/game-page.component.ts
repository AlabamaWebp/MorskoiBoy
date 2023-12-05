import { NgFor } from '@angular/common';
import { Component } from '@angular/core';
import { GameWrapperComponent } from '../game-wrapper/game-wrapper.component';

@Component({
  selector: 'app-game-page',
  standalone: true,
  imports: [NgFor, GameWrapperComponent],
  templateUrl: './game-page.component.html',
  styleUrl: './game-page.component.scss'
})
export class GamePageComponent {

  count = 8;
  your_buldings: build[] = base;
  enemy_buldings: build[] = base;
  cards: card[] = [];
  ngOnInit() {

  }
}

interface build {
  name: string
  hp: number
  def: number
  img: any
}

interface card {
  name: string
  strong: number
  img: any
}


// - Образование 👩‍🏫
// - Медицина 🩺
// - Культурный досуг 🎨
// - Заправки 🚗
// - Общественный транспорт 🚌
// - Спорт 🏀
// - Электроэнергия 💡
// - Водоснабжение 


const base = [
  {
    name: "Образование",
    hp: 8,
    def: 0,
    img: ""
  },
  {
    name: "Медицина",
    hp: 7,
    def: 0,
    img: ""
  },
  {
    name: "Культурный досуг",
    hp: 7,
    def: 0,
    img: ""
  },
  {
    name: "Заправка",
    hp: 5,
    def: 0,
    img: ""
  },
  {
    name: "Общественный транспорт",
    hp: 6,
    def: 0,
    img: ""
  },
  {
    name: "Спорт",
    hp: 6,
    def: 0,
    img: ""
  },
  {
    name: "Электроэнергия",
    hp: 8,
    def: 0,
    img: ""
  },
  {
    name: "Водоснабжение",
    hp: 6,
    def: 0,
    img: ""
  },
]