import {Component, OnInit} from '@angular/core';
import {BaseComponent} from "../../../core/base/base.component";
import {AuditDto} from "../../../models/admin/audit-dto";
import {AdminService} from "../../../core/services/admin.service";
import {takeUntil} from "rxjs";
import {NgForOf, NgIf} from "@angular/common";
import {AuditActionComponent} from "../../../shared/components/audit-action/audit-action.component";
import {MatTableModule} from "@angular/material/table";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatInputModule} from "@angular/material/input";
import {MatSelectModule} from "@angular/material/select";
import {FormBuilder, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";

@Component({
  selector: 'app-audit-list',
  standalone: true,
  imports: [
    NgIf,
    AuditActionComponent,
    NgForOf,
    MatTableModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    ReactiveFormsModule
  ],
  templateUrl: './audit-list.component.html',
  styleUrl: './audit-list.component.css'
})
export class AuditListComponent extends BaseComponent implements OnInit {
  public filterForm: FormGroup = new FormGroup({});
  public auditList?: AuditDto[];
  public columns = [
    {
      columnDef: 'action',
      header: 'Action',
      cell: (element: AuditDto) => `${element.action}`,
    },
    {
      columnDef: 'date',
      header: 'Date',
      cell: (element: AuditDto) => `${element.date}`,
    },
    {
      columnDef: 'userId',
      header: 'User ID',
      cell: (element: AuditDto) => `${element.user_id}`,
    },
    {
      columnDef: 'userName',
      header: 'User Name',
      cell: (element: AuditDto) => `${element.user_name}`,
    },
  ];
  public displayedColumns = this.columns.map(c => c.columnDef);
  public options = [
    {value: 'all', display: 'No filters'},
    {value: 'signin', display: 'Sign In'},
    {value: 'transaction', display: 'Transactions'},
    {value: 'loan', display: 'Loans'},
  ];
  ngOnInit(): void {
    this.initializeForm();
    this.getAuditList('all');
  }

  constructor(private fb: FormBuilder, private adminService: AdminService) {
    super();
  }

  private initializeForm() {
    this.filterForm = this.fb.group({
      filter: ['all', Validators.required]
    })
  }

  public onFilterChange() {
    const selectedFilter = this.filterForm.get('filter')?.value;
    this.getAuditList(selectedFilter);
  }

  private getAuditList(filter: string) {
    this.adminService.getAudit(filter).
    pipe(takeUntil(this.unsubscribe$))
      .subscribe({
        next: AuditList => {
          this.auditList = AuditList.reverse();
        }
      });
  }
}
