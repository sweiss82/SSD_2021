import {Component, Input, OnInit} from '@angular/core';
import {Medikamentenbestellung} from "../Medikamentenbestellung";

@Component({
  selector: 'app-medikamentenbestellung',
  templateUrl: './medikamentenbestellung.component.html',
  styleUrls: ['./medikamentenbestellung.component.css']
})
export class MedikamentenbestellungComponent implements OnInit {

 @Input() medikamentenbestellung: Medikamentenbestellung;

  constructor() { }

  ngOnInit(): void {
  }

}
