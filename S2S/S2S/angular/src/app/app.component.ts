import { Component } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  mydata = '';
  results = '';

  constructor(private http: HttpClient){

  }

  ngOnInit(): void {
    this.http.get('https://127.0.0.1:8000/tenant/test?test_id=1').subscribe(data => {
      console.log(data);
    });
  }

}
