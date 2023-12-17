import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ClientPageComponent} from "./client-page/client-page.component";
import {ListsComponent} from "./lists/lists.component";
import {TransactionCreateComponent} from "./transaction-create/transaction-create.component";
import {LoanCreateComponent} from "./loan-create/loan-create.component";

const routes: Routes = [
  {
    path: '',
    component: ClientPageComponent,
    children: [
      {
        path: 'lists',
        component: ListsComponent
      },
      {
        path: 'create-transaction',
        component: TransactionCreateComponent
      },
      {
        path: 'create-loan',
        component: LoanCreateComponent
      },
      { path: '', redirectTo: 'lists', pathMatch: 'full' }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ClientRoutingModule { }
