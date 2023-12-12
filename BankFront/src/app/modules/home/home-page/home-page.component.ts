import { Component } from '@angular/core';
import {MatButtonModule} from "@angular/material/button";
import {LoginComponent} from "../login/login.component";
import {RouterLink, RouterOutlet} from "@angular/router";

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [
    MatButtonModule,
    LoginComponent,
    RouterOutlet,
    RouterLink
  ],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.css'
})
export class HomePageComponent {

}
