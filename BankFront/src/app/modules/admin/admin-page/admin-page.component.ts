import {Component, OnInit} from '@angular/core';
import {BaseComponent} from "../../../core/base/base.component";
import {UserDto} from "../../../models/user/user-dto";
import {AuthService} from "../../../core/services/auth.service";
import {Router, RouterLink, RouterOutlet} from "@angular/router";
import {MatButtonModule} from "@angular/material/button";

@Component({
  selector: 'app-admin-page',
  standalone: true,
  imports: [
    MatButtonModule,
    RouterLink,
    RouterOutlet
  ],
  templateUrl: './admin-page.component.html',
  styleUrl: './admin-page.component.css'
})
export class AdminPageComponent extends BaseComponent implements OnInit {
  public currentUser?: UserDto;
  ngOnInit(): void {
    this.getCurrentUser()
  }

  constructor(private authService: AuthService, private router: Router) {
    super();
  }

  public logout() {
    this.authService.logout();
    this.router.navigate(['/home']);
  }

  private getCurrentUser() {
    this.authService.currentUser$.subscribe({
      next: user => {
        if (user) {
          this.currentUser = user;
        }
      }
    })
  }

}
