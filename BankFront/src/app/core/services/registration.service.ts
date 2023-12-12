import { Injectable } from '@angular/core';
import {HttpInternalService} from "./http-internal.service";
import {UserSigninDto} from "../../models/user/user-signin-dto";
import {RegistrationDto} from "../../models/user/registration-dto";

@Injectable({
  providedIn: 'root'
})
export class RegistrationService {
  private readonly authRoutePrefix = '/api/reg';

  constructor(private http: HttpInternalService) { }

  public regClient(userSigninDto: UserSigninDto){
    return this.http.postRequest<RegistrationDto>(`${this.authRoutePrefix}/create-account`, userSigninDto);
  }
}
