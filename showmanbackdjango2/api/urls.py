from django.conf.urls import url
from api import views



urlpatterns = [
    url('attendees/$', views.AttendeesList.as_view()),
    url(r'^attendees/(?P<pk>\d+)/', views.attendee_detail, name="attendees"),
    url('events/$', views.EventTypesList.as_view()),
    url(r'^events/(?P<pk>\d+)/', views.eventtype_detail, name="events"),
    url('users/', views.UserList.as_view()),
    url('login/', views.login),
    url('attendees/<int:pk>/postpicture/', views.upload_pic),
    url('logout/', views.logout),
    # url('categories/<int:pk>/products/', views.CategoryProductList.as_view())

]