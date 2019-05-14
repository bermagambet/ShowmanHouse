import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IDepartment, IAuthResponse, IAttendees, IEventsTypes, IUser, IOrder, 
IRealUser, ICity, ICountry, IAddress, IDiscount, IPayment, IFeeSchedule, IPaginated, IEmployees, IAvatar, IOurEvents, IPaginatedOurEvents} 
from '../modules/models';

@Injectable({
  providedIn: 'root'
})
export class ServiceForMainService extends MainService {

  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  getAttendees(): Promise<IAttendees[]> {
    return this.get('http://localhost:8000/api/attendees/', {});
  }

  getAvatars(): Promise<IAvatar[]> {
    return this.get('http://localhost:8000/api/avatar/', {});
  } 

  getAvatar(avatar: IAvatar): Promise<IAvatar> {
    return this.get('http://localhost:8000/api/avatar/' + avatar.id + '/', {});
  } 

  getDepartments(): Promise<IDepartment[]> {
    return this.get('http://localhost:8000/api/departments/', {});
  }

  getAttendee(attendee: IAttendees): Promise<IAttendees[]> {
    return this.get('http://localhost:8000/api/attendees/' + attendee.id + '/', {});
  }

  getCities(): Promise<ICity[]>{
    return this.get('http://localhost:8000/api/cities/', {});
  }

  getEmployee(emp: IEmployees): Promise<IEmployees>{
    return this.get('http://localhost:8000/api/employees/' + emp.id + '/', {});
  }
  // getCity(city: ICity): Promise<ICity>{
  //   return this.get('http://localhost:8000/api/cities/' + city.id + '/', {});
  // }

  getCountries(): Promise<ICountry[]>{
    return this.get('http://localhost:8000/api/countries/', {});  
  }

  getEmployees(): Promise<IEmployees[]>{
    return this.get('http://localhost:8000/api/employees/', {});  
  }

  getAddress(customer: number): Promise<IAddress>{
    return this.get('http://localhost:8000/api/attendees/'+ customer +'/address/' + '1' + '/', {});
  }


  getCity(city: ICity): Promise<ICity>{
    return this.get('http://localhost:8000/api/cities/' + city.id + '/', {});
  }




  getEventTypes(suf: string): Promise<IEventsTypes[]> {
    return this.get('http://localhost:8000/api/events/' + suf, {});
  }



  getOrders(): Promise<IOrder[]> {
    return this.get('http://localhost:8000/api/orders/', {});
  }

  getPayments(): Promise<IPayment[]> {
    return this.get('http://localhost:8000/api/payments/', {});
  }

  geFees(): Promise<IFeeSchedule[]> {
    return this.get('http://localhost:8000/api/fees/', {});
  }
  getPaginatedEvents(l: number, o: number, p: number): Promise<IPaginated> {
    return this.get('http://localhost:8000/api/events/?limit='+l+'&offset='+o+'&page=' + p, {});
  }
  getPayment(p: IPayment): Promise<IPayment> {
    return this.get('http://localhost:8000/api/payments/' + p.id + '/', {});
  }

  geFee(f: IFeeSchedule): Promise<IFeeSchedule> {
    return this.get('http://localhost:8000/api/fees/' + f.id + '/', {});
  }

  getDiscounts(): Promise<IDiscount[]> {
    return this.get('http://localhost:8000/api/discounts/', {});
  }

  getDiscount(disc: IDiscount): Promise<IDiscount> {
    return this.get('http://localhost:8000/api/orders/' + disc.id + '/', {});
  }


  getOrderedOrders(strings: string): Promise<IOrder[]> {
    return this.get('http://localhost:8000/api/orders/' + strings, {});
  }
  
  getOrder(order: IOrder): Promise<IOrder> {
    return this.get('http://localhost:8000/api/orders/' + order.id + '/', {});
  }

  createEvent(id: number, event_title: string, event_description: string): Promise<IEventsTypes> {
    return this.post('http://localhost:8000/api/events/', {
      id: id,
      event_title: event_title,
      event_description: event_description,
    });
  }

  getOurEvents(str: string): Promise<IOurEvents[]> {
    return this.get('http://localhost:8000/api/createde/' + str , {});
  }
  getOurEvents2(str: string): Promise<IOurEvents[]> {
    return this.get('http://localhost:8000/api/createde/paginated/' + str , {});
  }
  
  getPaginatedOurEvents(): Promise<IPaginatedOurEvents> {
    return this.get('http://localhost:8000/api/createde/', {});
  }

  getOurEvent(event: IOurEvents): Promise<IOurEvents> {
    return this.get('http://localhost:8000/api/createde/' + event.id + '/', {});
  }

  createOurEvent(id: number, start_date: string, end_date: string, participants: number, price: number, type_id: number, payment_id:number): Promise<IOurEvents> {
    return this.post('http://localhost:8000/api/createde/', {
      id: id,
      start_date: start_date,
      end_date: end_date,
      participants: participants,
      price: price,
      type_id: type_id,
      payment_id: payment_id
    });
  }

  createFee(id: number, payment_date: string, payment_amount: number): Promise<IFeeSchedule> {
    return this.post('http://localhost:8000/api/fees/', {
      id: id,
      payment_date: payment_date,
      payment_amount: payment_amount,
    });
  }

  updateEvent(id: number, event_title: string, event_description: string): Promise<IEventsTypes> {
    return this.put('http://localhost:8000/api/events/' + id + '/', {
    event_title: event_title,
    event_description: event_description,
    });
  }


  createOrder(id: number, event_id: number, customer_id: number, department_id: number): Promise<IOrder> {
    return this.post('http://localhost:8000/api/orders/', {
      id: id,
      event_id: event_id,
      customer_id: customer_id,
      department_id: department_id
    });
  }


  updateDiscount(id: number, orders_number: number, discount: number, customer_id: number): Promise<IDiscount> {
    return this.put('http://localhost:8000/api/discounts/' + id + '/', {
    orders_number: orders_number,
    discount: discount,
    customer_id: customer_id
    });
  }

  updateAddress(list: IAttendees, add: IAddress): Promise<IAddress>{
    return this.put('http://localhost:8000/api/attendees/'+ list.id +'/address/' + '1' + '/', {
      district: add.district,
      street: add.street,
      apartments: add.apartments,
      city_id: add.city_id,
      customer_id: add.customer_id
    })
  }

  updateCity(city: ICity){
    return this.put('http://localhost:8000/api/cities/'+ city.id +'/', {
      city_name: city.city_name,
      city_state: city.city_state,
      country_id: city.country_id
        })
  }



  updateCountry(country: ICountry){
    return this.put('http://localhost:8000/api/countries/'+ country.id +'/', {
      country_name: country.country_name,
        })
  }


  getEventType(): Promise<IEventsTypes[]> {
    return this.get('http://localhost:8000/api/events/${id}/', {});
  }

  getUsers(): Promise<IRealUser[]> {
    return this.get('http://localhost:8000/api/users/', {});
  }

  getUser(): Promise<IRealUser> {
    return this.get('http://localhost:8000/api/users/current/', {});
  }

  auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {});
  }

  getImage(url: string): Promise<Blob> {
    return this.get(`${url}`, {responseType: 'blob'})
  }
}