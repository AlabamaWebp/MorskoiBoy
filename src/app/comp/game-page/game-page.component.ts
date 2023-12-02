import { NgFor, NgIf } from '@angular/common';
import { Component } from '@angular/core';
@Component({
  selector: 'app-game-page',
  standalone: true,
  imports: [NgFor, NgIf],
  templateUrl: './game-page.component.html',
  styleUrl: './game-page.component.scss'
})
export class GamePageComponent {

  // type 0 - ничего, 1 - телефон, 2 - компьютер, 3 - сервер

  scale = 5;
  razmechenie = true;

  yourTable: any = [[{type: 0}]]
  yourCells: coord[] = []
  enemyTable: any = [[{type: 0}]]
  enemyCells: coord[] = []

  ngOnInit() {
    this.fillTable(this.yourTable);
    this.fillTable(this.enemyTable);
    console.log(this.yourTable);
    
  }
  fillTable(table: any) {
    for (let i = 0; i < this.scale; i++) {
      for (let j = 0; j < this.scale; j++) {
        table[i][j] = {type: 0}
      }      
    }
  }

}

interface cells {
  type: number
}
interface coord {
  x: number
  y: number
}