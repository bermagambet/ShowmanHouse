import { NumberSymbol } from '@angular/common';

  export interface IAuthResponse {
    token: string;
  }

  export interface IDepartment {
    id: number;
    employees_number: number;
    event_id: number;
  }

  export interface IAttendees {
    id: number;
    first_name: string;
    second_name: string;
  }

  export interface IEventsTypes {
    id: number;
    event_title: string;
    event_description: string;
  }

  export interface IOrder {
    id: number;
    event_id: number;
    customer_id: number;
    department_id: number;
  }

  export interface IUser {
    login: string;
  }

  export interface IRealUser {
    id: number;
    username: string;
    email: string;
    first_name: string;
    last_name: string;    
  }

  export interface IAddress {
    location_id: number;
    city_id: number;
    customer_id: number;
    district: string;
    street: string;
    apartments: string;
  }

  export interface ICity {
    city_id: number;
    city_name: string;
    city_state: string;
    country_id: number;
  }

  export interface ICountry {
    country_id: number;
    country_name: string;
  }
  
  export interface IFederativeRepublic {
    coutry_id: number;
    federation_name: string;
  }

  export interface IDiscount {
    customer_id: number;
    orders_number: number;
    discount: number;
  }

  export interface IShowmanHouse {
    department_id: number;
    offered_event_id: number;
    employees_number: number;
  }

  export interface IEvents {
    event_id: number;
    type_id: number;
    payment_id: number;
    start_date: Date;
    end_date: Date;
    participants_number: number;
    price: number;
  }
  export interface IEmployees {
    employee_id: number;
    department_id: number;
    first_name: string;
    second_name: string;
    position: string;
    phone_number: string;
  }

  export interface IFeeSchedule {
    payment_id: number;
    payment_date: Date;
    payment_amount: number;
  }

  export interface IPaymentMethod {
    payment_name: string;
    payment_id: number;
  }

  export interface IEntertainingGroup {
    entertain_id: number;
    hous_per_week: number;
  }

  export interface IAdministrativeStaff {
    administrator_id: number;
    cab_number: number;
  }

  export interface ITrainee {
    employee_id: number;
    start_in: Date;
    ends_in: Date;
  }

