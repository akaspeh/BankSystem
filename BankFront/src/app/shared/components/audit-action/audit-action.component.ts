import {Component, Input} from '@angular/core';
import {AuditDto} from "../../../models/admin/audit-dto";

@Component({
  selector: 'app-audit-action',
  standalone: true,
  imports: [],
  templateUrl: './audit-action.component.html',
  styleUrl: './audit-action.component.css'
})
export class AuditActionComponent {
  @Input() auditAction?: AuditDto;
}
