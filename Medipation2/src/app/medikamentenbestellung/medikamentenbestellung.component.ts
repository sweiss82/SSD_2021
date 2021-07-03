import {Component, Input, OnInit} from '@angular/core';
import {Medikamentenbestellung} from "../Medikamentenbestellung";
import {MedikamentenbestellungService} from '../medikamentenbestellung.service';

@Component({
  selector: 'app-medikamentenbestellung',
  templateUrl: './medikamentenbestellung.component.html',
  styleUrls: ['./medikamentenbestellung.component.css']
})
export class MedikamentenbestellungComponent implements OnInit {

 medikamentenbestellung: Medikamentenbestellung;

 //medikamentenbestellung: Medikamentenbestellung;
  constructor(private medikamentenbestellungService: MedikamentenbestellungService) { }

  ngOnInit(): void {
    this.medikamentenbestellung = new Medikamentenbestellung();
  }

  save(): void {
    console.log("called save()");
    this.medikamentenbestellungService.createMedikamentenbestellung(this.medikamentenbestellung).subscribe((
      medikamentenbestellung) => this.medikamentenbestellung = medikamentenbestellung);
  }

}
