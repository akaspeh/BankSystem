import {Component, OnInit} from '@angular/core';
import {BaseComponent} from "../../../core/base/base.component";
import {UserDto} from "../../../models/user/user-dto";
import {ClientService} from "../../../core/services/client.service";
import {AuthService} from "../../../core/services/auth.service";
import {LoanListDto} from "../../../models/loan/loan-list-dto";
import {takeUntil} from "rxjs";
import {MatExpansionModule} from "@angular/material/expansion";
import {LoanComponent} from "../../../shared/components/loan/loan.component";
import {NgForOf} from "@angular/common";

@Component({
  selector: 'app-loans',
  standalone: true,
  imports: [
    MatExpansionModule,
    LoanComponent,
    NgForOf
  ],
  templateUrl: './loans.component.html',
  styleUrl: './loans.component.css'
})
export class LoansComponent extends BaseComponent implements OnInit {
  public loans?: LoanListDto;
  public currentUser?: UserDto;

  public ngOnInit() {
    this.getCurrentUser();
    this.getLoans();
  }

  constructor(private clientService: ClientService, private authService: AuthService) {
    super();
  }

  private getLoans() {
    if (this.currentUser) {
      this.clientService.getAllLoans(this.currentUser.id)
        .pipe(takeUntil(this.unsubscribe$))
        .subscribe({
          next: transactions => {
            this.loans = transactions;
          }
        });
    }
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
