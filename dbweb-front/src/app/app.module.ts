import { BrowserModule } from '@angular/platform-browser';
import { NgModule,ClassProvider, } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import {ServiceForMainService} from './service-for-main.service';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {FormsModule} from '@angular/forms';
import {AuthInterceptor} from './main/AuthInterceptor';
import { MainService } from './main.service';
@NgModule({
  declarations: [
    AppComponent,
    MainComponent
  ],
  imports: [
    FormsModule,
    BrowserModule,
    HttpClientModule
  ],
  providers: [
    ServiceForMainService,
    MainService,
    <ClassProvider> {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

