import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {MatInputModule} from "@angular/material/input";
import {MatFormFieldModule} from "@angular/material/form-field";
import {FormBuilder, FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {AuthService} from "../../../core/services/auth.service";
import {UserLoginDto} from "../../../models/user/user-login-dto";

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, MatIconModule, MatButtonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit {
  @Output() close = new EventEmitter();
  public loginForm: FormGroup = new FormGroup({});
  hide = true;

  constructor(private fb: FormBuilder, private authService: AuthService) {
  }

  public closeModal() {
    this.close.emit();
  }

  public ngOnInit() {
    this.initializeForm();
  }

  private initializeForm() {
    this.loginForm = this.fb.group({
      email: [
        '',
        [Validators.required, Validators.email, Validators.minLength(5), Validators.maxLength(50)],
      ],
      password: ['', [Validators.required, Validators.minLength(6), Validators.maxLength(25)]],
    });
  }

  public login() {
    const user: UserLoginDto = this.loginForm.value;

    this.authService.login(user)
      .subscribe({
        next: () => {
          this.closeModal();
        }
      })
  }

  getErrorMessage() {
    if (this.loginForm.hasError('required')) {
      return 'You must enter a value';
    }

    return this.loginForm.hasError('email') ? 'Not a valid email' : '';
  }
}
