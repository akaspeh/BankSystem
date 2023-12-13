import {Component, OnInit} from '@angular/core';
import {MatExpansionModule} from "@angular/material/expansion";
import {TransactionListDto} from "../../../models/transaction/transaction-list-dto";
import {UserDto} from "../../../models/user/user-dto";
import {ClientService} from "../../../core/services/client.service";
import {AuthService} from "../../../core/services/auth.service";
import {UserIdDto} from "../../../models/user/user-id-dto";
import {TransactionComponent} from "../../../shared/components/transaction/transaction.component";
import {NgForOf} from "@angular/common";
import {BaseComponent} from "../../../core/base/base.component";
import {takeUntil} from "rxjs";

@Component({
  selector: 'app-transactions',
  standalone: true,
  imports: [
    MatExpansionModule,
    TransactionComponent,
    NgForOf
  ],
  templateUrl: './transactions.component.html',
  styleUrl: './transactions.component.css'
})
export class TransactionsComponent extends BaseComponent implements OnInit {
  public transactions?: TransactionListDto;
  public currentUser?: UserDto;

  public ngOnInit() {
    this.getCurrentUser();
    this.getTransactions();
  }

  constructor(private clientService: ClientService, private authService: AuthService) {
    super();
  }

  private getTransactions() {
    if (this.currentUser) {
      const userIdDto: UserIdDto = {
        id: this.currentUser.id
      }
      this.clientService.getAllTransactions(userIdDto)
        .pipe(takeUntil(this.unsubscribe$))
        .subscribe({
          next: transactions => {
            this.transactions = transactions;
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
