// export interface ICategory {
//     id: number;
//     name: string;
//   }
  
//   export interface IProduct {
//     id: number;
//     name: string;
//     price: number;
//     count: number;
//   }
  
  export interface IAuthResponse {
    token: string;
  }

  export interface IDepartment {
    id: number;
    employees_number: number;
    event_id: number;
  }

  export interface IAttendees{
    id: number;
    first_name: string;
    second_name: string;
  }

  export interface IEventsTypes{
    id: number;
    event_title: string;
    event_description: string;
  }

  export interface IEmployees{
    id: number;
    first_name: string;
    second_name: string;
    position: string;
    phone_number: string;
    department_id: number;
  }

  export interface IOrder{
    id: number;
    event_id: number;
    customer_id: number;
    department_id: number;
  }

  export interface IUser{
    login: string;
  }

  export interface IPaginated{
    count: number;
    next: string;
    previous: string;
    results: IEventsTypes[];
  }

  export interface IRealUser{
    id: number;
    username: string;
    email: string;
    first_name: string;
    last_name: string;    
  }

  export interface ICity{
    id: number;
    city_name: string;
    city_state: string;
    country_id: number;
  }

  export interface IDiscount{
    id: number;
    orders_number: number;
    discount: number;
    customer_id: number;
  }

  export interface IPayment{
    id: number;
    method_name: string;
    payment_id: number;
  }

  export interface IFeeSchedule{
    id: number;
    payment_date: string;
    payment_amount: number; 
  }

  export interface IAddress{
    id: number;
    district: string;
    street: string;
    apartments: number;
    city_id: number;
    customer_id: number;

  }

  
  export interface ICountry{
    id: number;
    country_name: string;
  }

  export interface IAvatar{
    id: number;
    avatar: string;
    customer_id: number;
  }

  export interface IOurEvents{
    id: number;
    start_date: string;
    end_date: string;
    participants: number;
    price: number;
    type_id: number;
    payment_id: number;
  }
  export interface IPaginatedOurEvents{
    count: number;
    next: string;
    previous: string;
    results: IOurEvents;
  }
