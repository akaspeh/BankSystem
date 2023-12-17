import {Component, Input} from '@angular/core';
import {UserDto} from "../../../models/user/user-dto";
import {MatButtonModule} from "@angular/material/button";
import {MatListModule} from "@angular/material/list";
import {NgClass, NgIf} from "@angular/common";

@Component({
  selector: 'app-client-details',
  standalone: true,
  imports: [
    MatButtonModule,
    MatListModule,
    NgIf,
    NgClass
  ],
  templateUrl: './client-details.component.html',
  styleUrl: './client-details.component.css'
})
export class ClientDetailsComponent {
  @Input() user?: UserDto;
  @Input() selected?: boolean;
}
