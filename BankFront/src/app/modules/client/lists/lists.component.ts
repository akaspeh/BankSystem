import { Component } from '@angular/core';
import {MatTabsModule} from "@angular/material/tabs";
import {RouterOutlet} from "@angular/router";
import {TransactionsComponent} from "../transactions/transactions.component";
import {LoansComponent} from "../loans/loans.component";

@Component({
  selector: 'app-lists',
  standalone: true,
  imports: [
    MatTabsModule,
    RouterOutlet,
    TransactionsComponent,
    LoansComponent
  ],
  templateUrl: './lists.component.html',
  styleUrl: './lists.component.css'
})
export class ListsComponent {

}
