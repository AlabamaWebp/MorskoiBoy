import { NgFor } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-game-wrapper',
  standalone: true,
  imports: [NgFor],
  templateUrl: './game-wrapper.component.html',
  styleUrl: './game-wrapper.component.scss'
})
export class GameWrapperComponent {
  @Input() data: any;
}
