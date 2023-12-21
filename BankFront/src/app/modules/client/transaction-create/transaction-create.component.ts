import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {MatListModule} from "@angular/material/list";
import {UserDto} from "../../../models/user/user-dto";
import {NgClass, NgForOf, NgIf} from "@angular/common";
import {ClientDetailsComponent} from "../../../shared/components/client-details/client-details.component";
import {MatTabsModule} from "@angular/material/tabs";
import {FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";
import {MatFormFieldModule} from "@angular/material/form-field";
import {ClientService} from "../../../core/services/client.service";
import {AuthService} from "../../../core/services/auth.service";
import {MatDialog} from "@angular/material/dialog";
import {Router} from "@angular/router";
import {BaseComponent} from "../../../core/base/base.component";
import {takeUntil} from "rxjs";
import {UserListDto} from "../../../models/user/user-list-dto";
import {ConfirmDialogComponent} from "../../../shared/components/confirm-dialog/confirm-dialog.component";
import {MatButtonModule} from "@angular/material/button";
import {TransactionCreationDto} from "../../../models/transaction/transaction-creation-dto";
import {MatInputModule} from "@angular/material/input";
import {UserBalanceDto} from "../../../models/user/user-balance-dto";

@Component({
  selector: 'app-transaction-create',
  standalone: true,
  imports: [
    MatInputModule,
    MatListModule,
    NgForOf,
    ClientDetailsComponent,
    NgClass,
    MatTabsModule,
    MatFormFieldModule,
    NgIf,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
  ],
  templateUrl: './transaction-create.component.html',
  styleUrl: './transaction-create.component.css'
})
export class TransactionCreateComponent extends BaseComponent implements OnInit{
  @Output() close = new EventEmitter();
  public transactionForm: FormGroup = new FormGroup({});
  public users?: UserListDto;
  public selectedTab = new FormControl(0);
  public selectedUserId: number | null = null;
  public currentUser?: UserDto;
  public userBalance?: UserBalanceDto;

  constructor(private fb: FormBuilder, private clientService: ClientService,
              private authService: AuthService, public dialog: MatDialog,
              private router: Router) {
    super()
  }

  public closeModal() {
    this.close.emit();
  }
  ngOnInit(): void {
    this.getCurrentUser();
    this.getUserBalance();
    this.initializeForm();
  }

  private initializeForm() {
    this.transactionForm = this.fb.group({
      amount: [null, [Validators.required, Validators.min(1), Validators.max(<number>this.userBalance?.balance)]],
      //amount: [null, [Validators.required, Validators.min(1)]],
      description: ['']
    })
  }

  private createTransaction() {
    if (this.transactionForm.valid && this.currentUser && this.selectedUserId) {
      const transaction: TransactionCreationDto = this.transactionForm.value;
      transaction.userIdSender = this.currentUser.id;
      transaction.userIdReceiver = this.selectedUserId;
      console.log('create transaction')
      this.clientService.createTransaction(transaction).
      subscribe({
        next: (response) => {
          console.log('Transaction created successfully', response);
          this.closeModal();
          this.router.navigate(['/client']);
        },
        error: (error) => {
          console.error('Error creating transaction', error);
        }
      });

    }
  }

  public selectUser(user: UserDto): void {
    this.selectedUserId = user.id;
    this.selectedTab.setValue(1);
  }

  public search(event: any) {
    const inputValue: string = event.target['value'];
    if (inputValue.length > 0) {
      console.log('Searching for: ', inputValue);
      this.clientService.findClients(inputValue).
      pipe(takeUntil(this.unsubscribe$))
        .subscribe({
          next: userList => {
            this.users = userList;
            this.users.items = this.users.items.filter(user => user.id !== this.currentUser?.id);
            this.users.items = this.users.items.filter(user => user.role !== 'admin');
          }
        });
    }
  }

  public openDialog() {
    if (!this.selectedUserId) {
      this.selectedTab.setValue(0);
      return;
    }
    if (this.transactionForm.valid) {
      const dialogRef = this.dialog.open(ConfirmDialogComponent);

      dialogRef.afterClosed().subscribe(result => {
        console.log(`Dialog result: ${result}`);
        if (result) {
          this.createTransaction();
        }
      });
    } else {
      this.transactionForm.controls['amount'].setErrors({'noValue': true});
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
  private getUserBalance() {
    if (this.currentUser) {
      this.clientService.getBalance(this.currentUser.id)
        .pipe(takeUntil(this.unsubscribe$))
        .subscribe({
          next: balance => {
            this.userBalance = balance;
            // Оновлення значення максимального балансу у формі
            const amountControl = this.transactionForm.get('amount');
            if (amountControl) {
              amountControl.setValidators([Validators.required, Validators.min(1), Validators.max(this.userBalance?.balance)]);
              amountControl.updateValueAndValidity();
            }
          }
        })
    }
  }
}
