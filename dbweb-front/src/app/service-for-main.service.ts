import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IAuthResponse, IAttendees, IEventsTypes, IUser} from './main/models';

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

  getAttendee(): Promise<IAttendees[]> {
    return this.get('http://localhost:8000/api/attendees/${id}/', {});
  }

  getEventTypes(): Promise<IEventsTypes[]> {
    return this.get('http://localhost:8000/api/events/', {});
  }

  getEventType(): Promise<IEventsTypes[]> {
    return this.get('http://localhost:8000/api/events/${id}/', {});
  }

  getUsers(): Promise<IUser[]> {
    return this.get('http://localhost:8000/api/users/', {});
  }
  // getProducts(category: ICategory): Promise<IProduct[]> {
  //   return this.get(`http://localhost:8000/api/categories/${category.id}/products/`, {});
  // }

  // createCategory(name: any): Promise<ICategory> {
  //   return this.post('http://localhost:8000/api/categories/', {
  //     name: name
  //   });
  // }

  // updateCategory(category: ICategory): Promise<ICategory> {
  //   return this.put(`http://localhost:8000/api/categories/${category.id}/`, {
  //     name: category.name
  //   });
  // }

  // deleteCategory(id: number): Promise<any> {
  //   return this.delet(`http://localhost:8000/api/categories/${id}/`, {});
  // }

  auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {});
  }

}