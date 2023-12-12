import { Injectable } from '@angular/core';
import {BehaviorSubject, tap} from "rxjs";
import {UserDto} from "../../models/user/user-dto";
import {HttpInternalService} from "./http-internal.service";
import {UserLoginDto} from "../../models/user/user-login-dto";
import {UserWithStatusDto} from "../../models/user/user-with-status-dto";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly authRoutePrefix = '/api/auth';
  private currentUserSource = new BehaviorSubject<UserDto | null>(null);
  public currentUser$ = this.currentUserSource.asObservable();

  constructor(private http: HttpInternalService) { }

  public login(userLoginDto: UserLoginDto){
    return this.http.postRequest<UserWithStatusDto>(`${this.authRoutePrefix}/login`, userLoginDto)
      .pipe(tap( (userWithStatus) => {
        this.setStatus(userWithStatus.status)
        this.setCurrentUser(userWithStatus.userDto);
      }))
  }

  public setStatus(status: string) {
    localStorage.setItem('authStatus', status);
  }

  public getStatus(): string | null {
    return localStorage.getItem('authStatus');
  }

  public clearStatus() {
    localStorage.removeItem('authStatus');
  }

  public setCurrentUser(userDto: UserDto) {
    const status = this.getStatus();
    if (status !== "succeed"){
      return;
    }
    this.currentUserSource.next(userDto);
  }
}
