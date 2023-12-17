import {Component, Input} from '@angular/core';
import {LoanDto} from "../../../models/loan/loan-dto";
import {MatExpansionModule} from "@angular/material/expansion";
import {NgIf} from "@angular/common";

@Component({
  selector: 'app-loan',
  standalone: true,
  imports: [
    MatExpansionModule,
    NgIf
  ],
  templateUrl: './loan.component.html',
  styleUrl: './loan.component.css'
})
export class LoanComponent {
  panelOpenState = false;
  @Input() loan?: LoanDto;
}
