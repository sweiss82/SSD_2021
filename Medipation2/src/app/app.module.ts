import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MedikamentenbestellungComponent } from './medikamentenbestellung/medikamentenbestellung.component';
import {FormsModule} from "@angular/forms";
import { LoginComponent } from './login/login.component';
import { MedikamentenplanComponent } from './medikamentenplan/medikamentenplan.component';
import { DatenubersichtComponent } from './datenubersicht/datenubersicht.component';
import { MedikamentenanfrageComponent } from './medikamentenanfrage/medikamentenanfrage.component';
import { MedikamentenanfragenOffenComponent } from './medikamentenanfragen-offen/medikamentenanfragen-offen.component';
import {HttpClientModule} from "@angular/common/http";

@NgModule({
  declarations: [
    AppComponent,
    MedikamentenbestellungComponent,
    LoginComponent,
    MedikamentenplanComponent,
    DatenubersichtComponent,
    MedikamentenanfrageComponent,
    MedikamentenanfragenOffenComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
