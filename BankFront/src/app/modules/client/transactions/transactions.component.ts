import {Component, OnInit} from '@angular/core';
import {MatExpansionModule} from "@angular/material/expansion";
import {TransactionListDto} from "../../../models/transaction/transaction-list-dto";
import {UserDto} from "../../../models/user/user-dto";
import {ClientService} from "../../../core/services/client.service";
import {AuthService} from "../../../core/services/auth.service";
import {TransactionComponent} from "../../../shared/components/transaction/transaction.component";
import {NgForOf, NgIf} from "@angular/common";
import {BaseComponent} from "../../../core/base/base.component";
import {map, takeUntil} from "rxjs";
import {TransactionDto} from "../../../models/transaction/transaction-dto";

@Component({
  selector: 'app-transactions',
  standalone: true,
  imports: [
    MatExpansionModule,
    TransactionComponent,
    NgForOf,
    NgIf
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

  public reversedTransactions(): TransactionDto[] {
    return this.transactions?.items ? this.transactions.items.slice().reverse() : [];
  }

  private getTransactions() {
    if (this.currentUser) {
      this.clientService.getAllTransactions(this.currentUser.id)
        .pipe(takeUntil(this.unsubscribe$),
          map(transactions => {
            transactions.items.forEach(transaction => {
              if (transaction.sender === this.currentUser?.id) {
                transaction.amount = -1 * transaction.amount;
              }
            });
            return transactions;
          }))
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
