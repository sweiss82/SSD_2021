import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginComponent} from "./login/login.component";
import {Medikamentenbestellung} from "./Medikamentenbestellung";
import {MedikamentenplanComponent} from "./medikamentenplan/medikamentenplan.component";
import {MedikamentenbestellungComponent} from "./medikamentenbestellung/medikamentenbestellung.component";
import {MedikamentenanfrageComponent} from "./medikamentenanfrage/medikamentenanfrage.component";


const routes: Routes = [
  { path: 'login', component: LoginComponent},
  { path: 'medikamentenbestellung', component: MedikamentenbestellungComponent},
  { path: 'medikamentenplan', component: MedikamentenplanComponent},
  { path: 'medikamentenanfragen', component: MedikamentenanfrageComponent},
  { path : '', redirectTo: '/login', pathMatch : 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
