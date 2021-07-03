import { Injectable } from '@angular/core';
import {Medikamentenbestellung} from './Medikamentenbestellung';
import {Observable} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Router} from '@angular/router';





const httpOptions = {
  headers: new HttpHeaders({
      //'Content-Type': 'application/json',
      'Accept': 'application/json',
      'cache-control': 'no-cache',
    //'Access-Control-Allow-Origin': '*',
    }
  )
};
const restServiceUrl = 'http://localhost:8000/api';

@Injectable({
  providedIn: 'root'
})
export class MedikamentenbestellungService {


  constructor(private http: HttpClient, private router: Router) { }

  createMedikamentenbestellung(medikamentenbestellung: Medikamentenbestellung): Observable<Medikamentenbestellung>{
    const url = `${restServiceUrl}/medikamentenbestellung`;
    console.log('called rest-backend_2');
    return this.http.post<Medikamentenbestellung>(url, medikamentenbestellung, httpOptions);
    //return this.http.get<Medikamentenbestellung>(url, medikamentenbestellung, httpOptions);
  }
}
