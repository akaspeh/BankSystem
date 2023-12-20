import {Component, OnInit} from '@angular/core';
import {TransactionComponent} from "../../../shared/components/transaction/transaction.component";
import {ClientService} from "../../../core/services/client.service";
import {AuthService} from "../../../core/services/auth.service";
import {UserDto} from "../../../models/user/user-dto";
import {MatExpansionModule} from "@angular/material/expansion";
import {MatTabsModule} from "@angular/material/tabs";
import {NavigationEnd, Router, RouterLink, RouterOutlet} from "@angular/router";
import {MatButtonModule} from "@angular/material/button";
import {UserBalanceDto} from "../../../models/user/user-balance-dto";
import {filter, takeUntil} from "rxjs";
import {BaseComponent} from "../../../core/base/base.component";

@Component({
  selector: 'app-client-page',
  standalone: true,
  imports: [
    TransactionComponent,
    MatExpansionModule,
    MatTabsModule,
    RouterOutlet,
    MatButtonModule,
    RouterLink,
  ],
  templateUrl: './client-page.component.html',
  styleUrl: './client-page.component.css'
})
export class ClientPageComponent extends BaseComponent implements OnInit{
  public currentUser?: UserDto;
  public userBalance?: UserBalanceDto;

  public ngOnInit() {
    this.getCurrentUser();
    this.getUserBalance();
  }

  constructor(private clientService: ClientService, private authService: AuthService, private router: Router) {
    super()
    this.router.events.pipe(
      filter(event => event instanceof NavigationEnd)
    ).subscribe(() => {
      // Викликайте метод getUserBalance при кожному успішному переході
      this.getUserBalance();
    });
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
    });
    if (!this.currentUser) {
      this.router.navigate(['/home']);
    }
  }
  private getUserBalance() {
    if (this.currentUser) {
      this.clientService.getBalance(this.currentUser.id)
        .pipe(takeUntil(this.unsubscribe$))
        .subscribe({
          next: balance => {
            this.userBalance = balance;
          }
        })
    }
  }
}
