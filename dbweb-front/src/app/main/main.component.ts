import {Component, Input, OnDestroy, OnInit} from '@angular/core';
// import {ICategory, IProduct} from '../shared/models/models';
import { ServiceForMainService } from '../service-for-main.service';
import { IEventsTypes, IAttendees, IOrder, IDepartment, IRealUser, IAddress, IDiscount } from './models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public output = '';
  public stringArray: string[] = [];

  // public categories: ICategory[] = [];
  public aboutme = false;
  public myorders = false;
  public loading = false;
  // public products: IProduct[] = [];
  public morderid: any = '';
  public morder_eventid: any = '';  
  public morder_customerid: any = '';
  public morder_departmentid: any = '';
  public eventtypes: IEventsTypes[] = [];
  public attendees: IAttendees[]=[];
  public attendee: IAttendees;
  public ordereventid: any = '';
  public orders: IOrder[]=[];
  public order: IOrder;
  public name: any = '';
  public departments: IDepartment[] = [];
  public department: IDepartment;
  public users: IRealUser[] = [];
  public current_user: IRealUser;
  public workers: any = '';
  public ordersre: IOrder[]=[];
  public url = '';
  public addresses: IAddress[]=[];
  public address:IAddress;
  public discounts: IDiscount[]=[];
  public discount: IDiscount;
  public isLogged = false;

  public login = '';
  public password = '';

  constructor(private provider: ServiceForMainService) {
  }

  

  ngOnInit() {
    this.provider.getUsers().then(res => {
      this.users = res;
      console.log("users");
      this.provider.getUser().then(res=>{
        this.current_user = res;
        console.log("user");
      })
    } ); 
    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }
    if (this.isLogged) {
      this.getEventTypes();
    }

  }

  getUserAddress(attendee: IAttendees){
    this.provider.getAddress(attendee).then(res => {
      this.address = res;
      this.aboutme=true;
      this.myorders=false;
    });
  }

  getUserDiscount(attendee: IAttendees){
    this.provider.getDiscount(attendee).then(res => {
      this.discount = res;
    });
  }
  findDepartment(department: IDepartment) {
    return department.id === this.order.department_id;
  }
  
  createOrder() {
    if (this.morderid !== '' || this.morder_customerid !== '' || this.morder_departmentid !== '' || this.morder_eventid !== '') {
      this.provider.createOrder(this.morderid, this.morder_eventid, this.morder_customerid, this.morder_departmentid).then(res => {
        this.morderid = '';
        this.morder_customerid = '';
        this.morder_departmentid = '';
        this.morder_eventid = '';
        this.orders.push(res);
      });
    }
  }

  getEventTypes() {
    this.provider.getEventTypes().then(res => {
      this.eventtypes = res;
      this.loading = true;
    });
  }

  startMakingOrder(event: IEventsTypes) {
    this.ordereventid = event.id;
    this.morder_eventid = this.ordereventid;
  }

  getAttendees() {
    this.provider.getAttendees().then(res => {
      this.attendees = res;
      this.loading = true;
    });
  }

  getOrders() {
    this.provider.getOrders().then(res => {
      this.orders = res;
      this.aboutme=false;
      this.myorders=true;
    });
  }

  getOrder(order: IOrder){
    this.provider.getOrder(order).then(res => {
      this.order = res;
      this.provider.getDepartments().then(res => {
        this.departments = res;
        // this.department = this.departments.find(this.findDepartment);
        // this.workers = this.department.employees_number;
        this.department =  this.departments.filter(x => x.id == this.order.department_id)[0];
        this.workers = this.department.employees_number;
        this.ordersre = [order];
      });
      this.provider.getAttendees().then(res => {
        this.attendees = res;
        console.log("attendees")
      });
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
        this.getEventTypes();
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
