import { Injectable } from '@angular/core';
import {HttpInternalService} from "./http-internal.service";
import {UserSigninDto} from "../../models/user/user-signin-dto";
import {UserDto} from "../../models/user/user-dto";

@Injectable({
  providedIn: 'root'
})
export class RegistrationService {
  private readonly authRoutePrefix = '/api/reg';

  constructor(private http: HttpInternalService) { }

  public regClient(userSigninDto: UserSigninDto){
    return this.http.postRequest<UserDto>(`${this.authRoutePrefix}/create-account`, userSigninDto);
  }
}
