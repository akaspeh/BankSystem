import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatInputModule} from "@angular/material/input";
import {MatSelectModule} from "@angular/material/select";
import {MatDatepickerModule} from "@angular/material/datepicker";
import {MatIconModule} from "@angular/material/icon";
import {MatNativeDateModule} from '@angular/material/core';
import {FormBuilder, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {ClientService} from "../../../core/services/client.service";
import {AuthService} from "../../../core/services/auth.service";
import {LoanCreationDto} from "../../../models/loan/loan-creation-dto";
import {MatButtonModule} from "@angular/material/button";
import {NgForOf} from "@angular/common";
import {MatDialog} from "@angular/material/dialog";
import {ConfirmDialogComponent} from "../../../shared/components/confirm-dialog/confirm-dialog.component";
import {UserDto} from "../../../models/user/user-dto";
import {Router} from "@angular/router";


@Component({
  selector: 'app-loan-create',
  standalone: true,
  imports: [
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatDatepickerModule,
    MatIconModule,
    MatNativeDateModule,
    ReactiveFormsModule,
    MatButtonModule,
    NgForOf
  ],
  templateUrl: './loan-create.component.html',
  styleUrl: './loan-create.component.css'
})
export class LoanCreateComponent implements OnInit {
  @Output() close = new EventEmitter();
  public loanForm: FormGroup = new FormGroup({});
  interestRates = [
    { value: 0.05, display: '5%' },
    { value: 0.10, display: '10%' },
    { value: 0.15, display: '15%' }
  ];
  public availableYears: number[] | undefined;
  public currentUser?: UserDto;

  constructor(private fb: FormBuilder, private clientService: ClientService,
              private authService: AuthService, public dialog: MatDialog,
              private router: Router) {
  }

  public closeModal() {
    this.close.emit();
  }
  ngOnInit(): void {
    this.getCurrentUser();
    this.initializeForm();
    this.setAvailableYears();
  }

  private initializeForm() {
    this.loanForm = this.fb.group({
      amount: [null, [Validators.required, Validators.min(0)]],
      interestRate: [null, Validators.required],
      closingDate: ['', Validators.required]
    })
  }
  private setAvailableYears(): void {
    const currentYear = new Date().getFullYear() + 1;
    this.availableYears = Array.from({ length: 10 }, (_, index) => currentYear + index);
  }

  public createLoan() {
    if (this.loanForm.valid && this.currentUser) {
      const currentDay = new Date();
      const newLoan: LoanCreationDto = this.loanForm.value;
      newLoan.closingDate = `${currentDay.getDate()}-${currentDay.getMonth() + 1}-${newLoan.closingDate}`;
      newLoan.userId = this.currentUser.id;
      this.clientService.createLoan(newLoan).
      subscribe({
        next: (response) => {
          console.log('Loan created successfully', response);
          this.closeModal();
          this.router.navigate(['/client']);
        },
        error: (error) => {
          console.error('Error creating loan', error);
        }
      });
      this.closeModal()
      this.router.navigate(['/client']);
    }
  }
  public openDialog() {
    if (this.loanForm.valid) {
      const dialogRef = this.dialog.open(ConfirmDialogComponent);

      dialogRef.afterClosed().subscribe(result => {
        console.log(`Dialog result: ${result}`);
        if (result) {
          this.createLoan();
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
