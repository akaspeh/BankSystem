import { Injectable } from '@angular/core';
import {HttpInternalService} from "./http-internal.service";
import {TransactionListDto} from "../../models/transaction/transaction-list-dto";
import {LoanListDto} from "../../models/loan/loan-list-dto";
import {TransactionCreationDto} from "../../models/transaction/transaction-creation-dto";
import {LoanCreationDto} from "../../models/loan/loan-creation-dto";
import {UserListDto} from "../../models/user/user-list-dto";
import {UserBalanceDto} from "../../models/user/user-balance-dto";

@Injectable({
  providedIn: 'root'
})
export class ClientService {
  private readonly clientRoutePrefix = '/api/client';
  constructor(private http: HttpInternalService) { }

  public getBalance(userId: number) {
    return this.http.getRequest<UserBalanceDto>(`${this.clientRoutePrefix}/balance/${userId}`);
  }

  public getAllTransactions(userId: number) {
    return this.http.getRequest<TransactionListDto>(`${this.clientRoutePrefix}/transaction/all/${userId}`);
  }

  public createTransaction(transactionCreationDto: TransactionCreationDto) {
    return this.http.postRequest(`${this.clientRoutePrefix}/transaction/create`, transactionCreationDto);
  }

  public getAllLoans(userId: number) {
    return this.http.getRequest<LoanListDto>(`${this.clientRoutePrefix}/loan/all/${userId}`);
  }
  public createLoan(loanCreationDto: LoanCreationDto) {
    return this.http.postRequest(`${this.clientRoutePrefix}/loan/create`, loanCreationDto);
  }
  public findClients(request: string) {
    return this.http.getRequest<UserListDto>(`${this.clientRoutePrefix}/find/${request}`)
  }
}
