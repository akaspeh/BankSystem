import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {MatButtonModule} from "@angular/material/button";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatIconModule} from "@angular/material/icon";
import {MatInputModule} from "@angular/material/input";
import {FormBuilder, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {RegistrationService} from "../../../core/services/registration.service";
import {NgIf} from "@angular/common";
import {UserLoginDto} from "../../../models/user/user-login-dto";
import {UserSigninDto} from "../../../models/user/user-signin-dto";
import {RegistrationDto} from "../../../models/user/registration-dto";
import {Router} from "@angular/router";

@Component({
  selector: 'app-signin',
  standalone: true,
  imports: [
    MatButtonModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    ReactiveFormsModule,
    NgIf
  ],
  templateUrl: './signin.component.html',
  styleUrl: './signin.component.css'
})
export class SigninComponent implements OnInit{
  @Output() close = new EventEmitter();
  public signinForm: FormGroup = new FormGroup({});
  hide = true;

  constructor(private fb: FormBuilder, private registration: RegistrationService, private router: Router) {
  }

  public closeModal() {
    this.close.emit();
  }

  public ngOnInit() {
    this.initializeForm();
  }

  private initializeForm() {
    this.signinForm = this.fb.group({
      email: [
        '',
        [Validators.required, Validators.email, Validators.maxLength(50)],
      ],
      password: ['', [Validators.required, Validators.minLength(6), Validators.maxLength(25)]],
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      phone: ['', [Validators.required]],
      address: ['', [Validators.required]]
    });
  }

  createAccount() {
    if (this.signinForm.valid) {
      const newUser: UserSigninDto = this.signinForm.value;

      this.registration.regClient(newUser)
        .subscribe({
          next: (registrationDto: RegistrationDto) => {
            if (registrationDto.status === 'wrong email') {
              this.signinForm.controls['email'].setErrors({'invalidEmail': true});
              console.log('Wrong email')
            } else {
              this.closeModal();
              this.router.navigate(['/home/login']);
            }
          }
        })
    } else {
      console.log('Form is invalid. Cannot perform login.');
    }
  }

  getErrorMessage(controlName: string) {
    const control = this.signinForm.get(controlName);

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
