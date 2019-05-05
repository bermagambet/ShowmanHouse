import {Component, Input, OnDestroy, OnInit} from '@angular/core';
// import {ICategory, IProduct} from '../shared/models/models';
import { ServiceForMainService } from '../service-for-main.service';
import { IEventsTypes, IAttendees } from './models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public output = '';
  public stringArray: string[] = [];

  // public categories: ICategory[] = [];
  public loading = false;

  // public products: IProduct[] = [];
  public eventtypes: IEventsTypes[] = [];
  public attendees: IAttendees[]=[];
  public name: any = '';

  public isLogged = false;

  public login = '';
  public password = '';

  constructor(private provider: ServiceForMainService) {
  }

  ngOnInit() {

    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }

    if (this.isLogged) {
      //this.getEventTypes();
    }

  }

  getEventTypes() {
    this.provider.getEventTypes().then(res => {
      this.eventtypes = res;
      this.loading = true;
    });
  }

  getAttendees() {
    this.provider.getAttendees().then(res => {
      this.attendees = res;
      this.loading = true;
    });
  }

  // getProducts(category: ICategory) {
  //   this.provider.getProducts(category).then(res => {
  //     this.products = res;
  //   });
  // }

  // sendMessageByService() {
  //   this.provider.sendMessage.emit('This message From Parent Component');
  // }

  // updateCategory(c: ICategory) {
  //   this.provider.updateCategory(c).then(res => {
  //     console.log(c.name + ' updated');
  //   });
  // }

  // deleteCategory(c: ICategory) {
  //   this.provider.deleteCategory(c.id).then(res => {
  //     console.log(c.name + ' deleted');
  //     this.provider.getCategories().then(r => {
  //       this.categories = r;
  //     });
  //   });
  // }

  // createCategory() {
  //   if (this.name !== '') {
  //     this.provider.createCategory(this.name).then(res => {
  //       this.name = '';
  //       this.categories.push(res);
  //     });
  //   }
  // }

  Mauth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        // this.getCategories();
      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      this.isLogged = false;
      localStorage.clear();
    });
  }

}
