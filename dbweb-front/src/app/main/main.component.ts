import {Component, Input, OnDestroy, OnInit, Sanitizer, SecurityContext} from '@angular/core';
// import {ICategory, IProduct} from '../shared/models/models';
import { ServiceForMainService } from '../shared/services/service-for-main.service';
import { IEventsTypes, IAttendees, IOrder, IDepartment, IRealUser, ICity, IAddress, ICountry, IDiscount, IFeeSchedule, IPayment, IEmployees, IAvatar } from '../shared/modules/models';
import { DomSanitizer, SafeResourceUrl, SafeUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public myorderstrue = false;
  public myinfotrue = false;
  public neworder2: number[] = [];
  public output = '';
  public neworders: number[] = [];
  public stringArray: string[] = [];

  // public categories: ICategory[] = [];
  public loading = false;
  public selectedorderid: number;

  // public products: IProduct[] = [];
  public morderid: any = '';
  public morder_eventid: any = '';  
  public morder_customerid: any = '';
  public morder_departmentid: any = '';
  public orderidplus = true;
  public ordernameplus1 = true;
  public ordernameplus = true;

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
  public city: any = '';
  public address: IAddress;
  public country: any = '';
  public currencustomer: IAttendees;
  public currentcustomerod: any = '';

  public cities: ICity[] = [];
  public updating = false;
  public countries: ICountry[] = [];
  public fees: IFeeSchedule[]=[];
  public payments: IPayment[]=[];

  // public departments: IDepartment[] = [];
  public item1: IAttendees;
  public item2: IAttendees;

  public custcountry: any = '';
  public custcity: any = '';
  public custcitystate: any = '';
  public custdistrict: any = '';
  public custstreet: any = '';
  public custapart: any = '';

  public item3: ICity;
  public item4: ICountry;
  public neworderid: any = '';
  public suffix: any = '';
  public needdd: any = '';
  public isLogged = false;
  public item5:  IDiscount;
  public item100: IAvatar;
  public item6:  IDiscount;


  public selectedorder: IOrder;
  public nextorderid: any = '';
  public thenewsrc: any ='';
  public neededdepartment: IDepartment;
  public login = '';
  public password = '';

  public imm22: any = '';
  public discounts: IDiscount[]=[];
  public discount: IDiscount;
  public imm1: any = '';
  public imm2: any = '';
  public payed = false;
  public created = false;
  public confirmed = false;
  public imm3: any = '';
  public visitor: number;
  public employees: IEmployees[]=[];
  public currentemployee: IEmployees;
  public currentemployeeid: any='';
  public item10: IEmployees;
  public item11: IEmployees;

  public eventiddd: number;
  public eventttt: string;
  public eventddd: string;

  public customer = false;
  public avatars: IAvatar[]=[];
  public avatar: IAvatar;

  constructor(private provider: ServiceForMainService, private sanitizer: DomSanitizer){
  }
  
  

  ngOnInit() {

    this.provider.getAttendees().then(res => {
      this.attendees = res;
      this.getEmployees();
      this.getAvatars();
    })
    
    this.provider.getUsers().then(res => {
      this.users = res;
      console.log("users");
      if(this.isLogged){
        this.provider.getDepartments().then(res=>{
          this.departments = res;
        });
      this.provider.getUser().then(res=>{
        this.current_user = res;
        console.log("user");
        if(this.current_user.first_name == 'Bermagambet')
        this.customer = true;
        if(this.current_user.first_name != 'Bermagambet')
        this.customer = false;
        this.determineCustomer(this.current_user.first_name, this.current_user.last_name);
        this.determineEmployee(this.current_user.first_name, this.current_user.last_name);
      });
    }
    } ); 
    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }

    if (this.isLogged) {
      this.getEventTypes();
    }

  }

  getAvatars(){
    this.provider.getAvatars().then(res=>{
      this.avatars = res;
    });
  }

  createEvent(){
    this.provider.createEvent(this.eventiddd, this.eventttt, this.eventddd).then(res=>{
      this.eventtypes.push(res);
    })
  }

  maxOrder() {
    this.nextorderid = this.orders.length + 1;
  }

  findDepartment(department: IDepartment) {
    return department.id === this.order.department_id;
  }
  
  createOrder() {
    if (this.morderid !== '' || this.morder_customerid !== '' || this.morder_departmentid !== '' || this.morder_eventid !== '') {
      this.provider.createOrder(this.nextorderid, this.morder_eventid, this.currentcustomerod, this.morder_departmentid).then(res => {
        this.orders.push(res);
        this.item6.discount = this.item6.discount + 5;
        this.item6.orders_number = this.orders.length + 1;
        this.provider.updateDiscount(this.item6.id, this.item6.orders_number, this.item6.discount, this.item6.customer_id).then(res=>{
          this.item6 = res;
        })
      });
    }
  }

  getEmployees(){
    this.provider.getEmployees().then(res=>{
      this.employees = res;
    })
  }

  determineEmployee(fname: string, sname: string){
    this.item10 = this.employees.filter(function(item) {
      return item.first_name = fname
    })[0];
    this.item11 = this.employees.filter(function(item) {
      return item.second_name = sname
    })[0];
    if(this.item1 == this.item2 && fname != '' && sname != ''){
      this.currentemployee = this.item10;
      console.log(this.item10.first_name)

      this.currentemployeeid = this.currentemployee.id;
      console.log(this.customer)
    }
  }
  

  getEventTypes() {
    this.provider.getEventTypes(this.suffix).then(res => {
      this.eventtypes = res;
      this.loading = true;
      this.suffix = '';
    });
  }

  startMakingOrder(event: IEventsTypes) {
    this.ordereventid = event.id;
    this.morder_eventid = this.ordereventid;
    this.neededdepartment = this.departments.filter(function(item) {
      console.log('okever');
      return item.event_id = 1;
    })[0];
    console.log(this.departments);
    console.log(this.neededdepartment.id);
    this.needdd = this.neededdepartment.id;
    this.morder_departmentid = this.needdd;
    
  }

  getAttendees() {
    this.provider.getAttendees().then(res => {
      this.attendees = res;
      this.loading = true;
    });
  }

  getBI(){
    this.thenewsrc = this.sanitizer.bypassSecurityTrustStyle('linear-gradient(rgba(29, 29, 29, 0), rgba(16, 16, 23, 0.5)), url(${this.thenewsrc})');
  }

  getOrders() {
    this.myorderstrue = true;
    this.thenewsrc =this.item100.avatar.replace('http://localhost:8000/media/', 'C:/xd_team.project/showmanhouseback/oracledbimages/'); 
    this.thenewsrc= this.sanitizer.sanitize(SecurityContext.STYLE, 'url(' + this.thenewsrc + ')');
    this.myinfotrue = false;
    this.neworder2 = this.neworders;
    this.neworder2.forEach(element => {
      this.neworders.pop();
    });
    this.provider.getOrders().then(res => {
      this.orders = res;
      this.orders.forEach(element => {
        this.neworders.push(element.id);
        console.log(element.id);
      });
    });  
  }

  getOrders2() {
    this.provider.geFees().then(res=>{
       this.fees = res;
    })
    this.provider.getPayments().then(res=>{
      this.payments = res;
    })
  }

  makePayment(){
    this.payed = true;
  }

  confirmPayment(){
    this.confirmed = true;
    this.payed = false;
    this.created = true;

  }


  getInfo() {
    this.myinfotrue = true;
    this.myorderstrue = false;
    this.provider.getAddress(this.currencustomer.id).then(res=>{
      this.address = res;
      this.custapart = res.apartments;
      this.custdistrict = res.district;
      this.custstreet = res.street;
      this.provider.getCities().then(res2=>{
        this.cities = res2;
        console.log(res.id);
        this.item3 = this.cities.filter(function(item) {
          return item.id = res.city_id;
        })[0];
        console.log(this.item3.city_name);
        this.custcity = this.item3.city_name;
        this.custcitystate = this.item3.city_state;
          this.provider.getCity(this.item3).then(res22=>{
            this.provider.getCountries().then(res3=>{
              this.countries = res3;
              this.item4 = this.countries.filter(function(item) {
              return item.id = res22.country_id;
            })[0];
            this.custcountry = this.item4.country_name;
        });
      });
    });
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

  determineCustomer(fname: string, sname: string){
    this.item1 = this.attendees.filter(function(item) {
      return item.first_name = fname
    })[0];
    this.item2 = this.attendees.filter(function(item) {
      return item.second_name = sname
    })[0];
    if(this.item1 == this.item2 && fname != '' && sname != ''){
      this.currencustomer = this.item1;
      var ccc = this.currencustomer.id;
      this.currentcustomerod = this.currencustomer.id;
      this.item100 = this.avatars.filter(function(item) {
        return item.customer_id = ccc;
      })[0];

      console.log(this.item1.first_name)
      console.log(this.item1.second_name)

      console.log(this.customer)

    }
  }

  logout() {
    this.provider.logout().then(res => {
      this.isLogged = false;
      localStorage.clear();
    });
  }

  makeOrderID(){
    if(this.orderidplus)
     this.provider.getEventTypes('?ordering=-id').then(res=>{
       this.eventtypes = res;
       this.orderidplus = false;
     });
     else if (!this.orderidplus)
      this.provider.getEventTypes('').then(res=>{
       this.eventtypes = res;
       this.orderidplus = true;
     });
  }

  makeOrderName(){
     if(!this.orderidplus && this.ordernameplus1){
       this.provider.getEventTypes('?ordering=-id'+'&'+'?ordering=-event_title').then(res=>{
       this.eventtypes = res;
       this.ordernameplus1 = false;
     });
     }
     else
     if(this.ordernameplus1)
     this.provider.getEventTypes('?ordering=-event_title').then(res=>{
       this.eventtypes = res;
       this.ordernameplus1 = false;
     });
     else if (!this.ordernameplus1)
      this.provider.getEventTypes('?ordering=event_title').then(res=>{
       this.eventtypes = res;
       this.ordernameplus1 = true;
     });
  }

  makeOrderReverse(){
    this.eventtypes = this.eventtypes.reverse();
  }

  makeFilter(){
    this.provider.getEventTypes('?event_title=' + this.suffix).then(res=>{
       this.eventtypes = res;
       this.suffix = '';
     });
  }

  orderOrders(){
    // this.selectedorderid = this.selectedorder.id;
    // console.log(this.selectedorder.id);
    console.log(this.selectedorderid);
    this.provider.getOrderedOrders('?id=' + this.selectedorderid).then(res=>{
      this.orders = res;
    })
  }

  updateAddress(){
    if(this.updating){
    this.updating = false;
  }
    else if(!this.updating)
    this.updating = true;
  console.log(this.currencustomer.id);
  console.log(this.address.city_id);
  console.log(this.address.customer_id);
  console.log(this.address.district);
    console.log(this.address.street);
  this.address.district = this.custdistrict;
  this.address.street = this.custstreet;
  this.address.apartments = this.custapart;

  this.provider.updateAddress(this.currencustomer, this.address).then(res=>{
  });
}

updateAddress1(){
  this.item3.city_name = this.custcity;
  this.item3.city_state = this.custcitystate;
  this.provider.updateCity(this.item3).then(res=>{
  });

}
updateAddress2(){
  this.item4.country_name = this.custcountry;
  this.provider.updateCountry(this.item4).then(res=>{
  });
}

getDiscounts(){
  this.provider.getDiscounts().then(res=>{
    var mr = 0;
    this.discounts = res;
    mr = this.currencustomer.id;
    console.log(this.currencustomer.id);
    this.item6 = res.filter(function(item) {
      return item.customer_id = mr;
    })[0];
    console.log(this.item6.discount);
  })
}

}

