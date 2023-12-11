import { Injectable } from '@angular/core';
import {BehaviorSubject, tap} from "rxjs";
import {UserDto} from "../../models/user/user-dto";
import {HttpInternalService} from "./http-internal.service";
import {UserLoginDto} from "../../models/user/user-login-dto";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly authRoutePrefix = '/api/auth';
  private currentUserSource = new BehaviorSubject<UserDto | null>(null);
  public currentUser$ = this.currentUserSource.asObservable();

  constructor(private http: HttpInternalService) { }

  public login(userLoginDto: UserLoginDto){
    return this.http.postRequest<UserDto>(`${this.authRoutePrefix}/login`, userLoginDto)
      .pipe(tap( (userAuth) => {
        this.setCurrentUser(userAuth);
      }))
  }

  public setCurrentUser(userDto: UserDto) {
    this.currentUserSource.next(userDto);
  }
}
