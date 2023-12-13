import {Component, OnInit} from '@angular/core';
import {TransactionComponent} from "../../../shared/components/transaction/transaction.component";
import {ClientService} from "../../../core/services/client.service";
import {AuthService} from "../../../core/services/auth.service";
import {UserDto} from "../../../models/user/user-dto";
import {RouterOutlet} from "@angular/router";
import {MatExpansionModule} from "@angular/material/expansion";

@Component({
  selector: 'app-client-page',
  standalone: true,
  imports: [
    TransactionComponent,
    RouterOutlet,
    MatExpansionModule
  ],
  templateUrl: './client-page.component.html',
  styleUrl: './client-page.component.css'
})
export class ClientPageComponent implements OnInit{
  public currentUser?: UserDto;

  public ngOnInit() {
    this.getCurrentUser();
  }

  constructor(private clientService: ClientService, private authService: AuthService) {
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
