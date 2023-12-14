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
  private authStatusSource = new BehaviorSubject<string | null>(null);
  public authStatus$ = this.authStatusSource.asObservable();

  constructor(private http: HttpInternalService) { }

  public login(userLoginDto: UserLoginDto){
    return this.http.postRequest<UserWithStatusDto>(`${this.authRoutePrefix}/login`, userLoginDto)
      .pipe(tap( (userWithStatus) => {
        this.setStatus(userWithStatus.status)
        this.setCurrentUser(userWithStatus.userDto);
      }))
  }

  public logout(): void {
    this.currentUserSource.next(null);
    this.clearStatus();
  }

  private setStatus(status: string): void {
    this.authStatusSource.next(status);
  }

  private clearStatus(): void {
    this.authStatusSource.next(null);
  }

  private setCurrentUser(userDto: UserDto): void {
    this.authStatus$.subscribe((status: string | null) => {
      if (status === 'succeed') {
        this.currentUserSource.next(userDto);
      }
    });
  }
}
