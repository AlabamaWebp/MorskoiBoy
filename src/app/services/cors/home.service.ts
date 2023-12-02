import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  constructor(public http: HttpClient) { }

  // url = "http://127.0.0.1:8081/";

  getHttp() {
    return this.http;
  }

}
