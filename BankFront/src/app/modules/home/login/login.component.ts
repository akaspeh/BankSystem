import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {MatInputModule} from "@angular/material/input";
import {MatFormFieldModule} from "@angular/material/form-field";
import {FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";
import {MatIconModule} from "@angular/material/icon";
import {MatButtonModule} from "@angular/material/button";
import {AuthService} from "../../../core/services/auth.service";
import {UserLoginDto} from "../../../models/user/user-login-dto";
import {NgIf} from "@angular/common";
import {UserWithStatusDto} from "../../../models/user/user-with-status-dto";
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, MatIconModule, MatButtonModule, NgIf],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit {
  @Output() close = new EventEmitter();
  public loginForm: FormGroup = new FormGroup({});
  hide = true;

  constructor(private fb: FormBuilder, private authService: AuthService, private router: Router) {
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
        [Validators.required, Validators.email, Validators.maxLength(50)],
      ],
      password: ['', [Validators.required, Validators.minLength(6), Validators.maxLength(25)]],
    });
  }

  public login() {
    if (this.loginForm.valid) {
      const user: UserLoginDto = this.loginForm.value;

      this.authService.login(user)
        .subscribe({
          next: (userWithStatusDto: UserWithStatusDto) => {
            if (this.authService.getStatus() === 'succeed') {
              if (userWithStatusDto.userDto.role === 'admin') {
                this.router.navigate(['/admin'])
              } else {
                this.router.navigate(['/client'])
              }
              this.closeModal();
              console.log(this.authService.getStatus())
            } else if (this.authService.getStatus() === 'failed') {
              this.loginForm.reset();
              console.log('Authentication failed');
            } else {
              this.loginForm.controls['password'].setErrors({'invalidPassword': true});
              console.log('Wrong password');
            }
          }
        })
    } else {
      console.log('Form is invalid. Cannot perform login.');
    }
  }

  getErrorMessage(controlName: string) {
    const control = this.loginForm.get(controlName);

    // @ts-ignore
    if (control.hasError('required')) {
      return 'This field is required';
    }

    // @ts-ignore
    if (controlName === 'email' && control.hasError('email')) {
      return 'Not a valid email';
    }

    return '';
  }
}
