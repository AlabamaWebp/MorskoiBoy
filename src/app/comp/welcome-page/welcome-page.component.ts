import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-welcome-page',
  standalone: true,
  imports: [],
  templateUrl: './welcome-page.component.html',
  styleUrl: './welcome-page.component.scss'
})
export class WelcomePageComponent {

  constructor(private route: Router) {
    
  }

  nickname: string = localStorage.getItem("name") ? localStorage.getItem("name") as string : Date.now() + "";

  btnClick() {
    if (this.nickname.length == 0) {
      localStorage.removeItem("name");
    }
    else {
      localStorage.setItem("name", this.nickname)
      this.route.navigateByUrl("game");
    }
  }

}
