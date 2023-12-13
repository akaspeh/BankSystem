import { Injectable } from '@angular/core';
import {HttpInternalService} from "./http-internal.service";
import {TransactionListDto} from "../../models/transaction/transaction-list-dto";
import {UserIdDto} from "../../models/user/user-id-dto";

@Injectable({
  providedIn: 'root'
})
export class ClientService {
  private readonly clientRoutePrefix = '/api/client';
  constructor(private http: HttpInternalService) { }

  public getAllTransactions(userIdDto: UserIdDto) {
    return this.http.getRequest<TransactionListDto>(`${this.clientRoutePrefix}/transaction/all`, userIdDto);
  }
}
