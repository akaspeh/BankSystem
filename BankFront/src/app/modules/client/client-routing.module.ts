import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ClientPageComponent} from "./client-page/client-page.component";
import {ListsComponent} from "./lists/lists.component";

const routes: Routes = [
  {
    path: '',
    component: ClientPageComponent,
    children: [
      {
        path: 'lists',
        component: ListsComponent
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
