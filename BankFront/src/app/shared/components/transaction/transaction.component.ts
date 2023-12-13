import {Component, Input} from '@angular/core';
import {MatExpansionModule} from "@angular/material/expansion";
import {TransactionDto} from "../../../models/transaction/transaction-dto";
import {NgIf} from "@angular/common";

@Component({
  selector: 'app-transaction',
  standalone: true,
  imports: [
    MatExpansionModule,
    NgIf
  ],
  templateUrl: './transaction.component.html',
  styleUrl: './transaction.component.css'
})
export class TransactionComponent {
  panelOpenState = false;
  @Input() transaction?: TransactionDto;
}
