import {Component, OnInit} from '@angular/core';
import {BaseComponent} from "../../../core/base/base.component";
import {AuditDto} from "../../../models/admin/audit-dto";
import {AdminService} from "../../../core/services/admin.service";
import {takeUntil} from "rxjs";
import {NgForOf, NgIf} from "@angular/common";
import {AuditActionComponent} from "../../../shared/components/audit-action/audit-action.component";

@Component({
  selector: 'app-audit-list',
  standalone: true,
  imports: [
    NgIf,
    AuditActionComponent,
    NgForOf
  ],
  templateUrl: './audit-list.component.html',
  styleUrl: './audit-list.component.css'
})
export class AuditListComponent extends BaseComponent implements OnInit {
  public auditList?: AuditDto[];
  ngOnInit(): void {
    this.getAuditList();
  }

  constructor(private adminService: AdminService) {
    super();
  }

  private getAuditList() {
    this.adminService.getAudit('transaction').
    pipe(takeUntil(this.unsubscribe$))
      .subscribe({
        next: AuditList => {
          this.auditList = AuditList;
          console.log(this.auditList)
        }
      });
  }

}
