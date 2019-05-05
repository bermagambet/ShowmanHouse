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

  export interface IAttendees{
    id: number;
    name: string;
    surname: string;
  }

  export interface IEventsTypes{
    id: number;
    event_title: string;
    event_description: string;
  }

  export interface IOrder{
    id: number;
  }

  export interface IUser{
    login: string;
  }
