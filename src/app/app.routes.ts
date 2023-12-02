import { Routes } from '@angular/router';
import { WelcomePageComponent } from './comp/welcome-page/welcome-page.component';
import { GamePageComponent } from './comp/game-page/game-page.component';

 

export const routes: Routes = [
    {path: "", component: WelcomePageComponent},
    {path: "game", component: GamePageComponent}
];
