import {ApplicationConfig, NgModule} from '@angular/core';
import {provideRouter, RouterOutlet} from '@angular/router';

import {AppRoutingModule, routes} from './app.routes';
import {BrowserAnimationsModule, provideAnimations} from '@angular/platform-browser/animations';
import {CommonModule} from "@angular/common";
import {HttpClientModule} from "@angular/common/http";
import {BrowserModule} from "@angular/platform-browser";
import {SharedModule} from "./shared/shared.module";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {CoreModule} from "./core/core.module";
import {AppComponent} from "./app.component";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    SharedModule,
    AppRoutingModule,
    RouterOutlet,
    ReactiveFormsModule,
    HttpClientModule,
    FormsModule,
    CoreModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
