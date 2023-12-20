import { Injectable } from '@angular/core';
import {HttpInternalService} from "./http-internal.service";
import {AuditDto} from "../../models/admin/audit-dto";

@Injectable({
  providedIn: 'root'
})
export class AdminService {
  private readonly adminRoutePrefix = '/api/admin';

  constructor(private http: HttpInternalService) { }

  public getAudit(filter: string) {
    return this.http.getRequest<AuditDto[]>(`${this.adminRoutePrefix}/audit/${filter}`);
  }
}
