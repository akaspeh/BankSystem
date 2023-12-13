import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ClientPageComponent} from "./client-page/client-page.component";
import {TransactionsComponent} from "./transactions/transactions.component";
import {LoansComponent} from "./loans/loans.component";

const routes: Routes = [
  {
    path: '',
    component: ClientPageComponent,
    children: [
      {
        path: 'transactions',
        component: TransactionsComponent
      },
      {
        path: 'loans',
        component: LoansComponent
      },
      { path: '', redirectTo: 'transactions', pathMatch: 'full' }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ClientRoutingModule { }
