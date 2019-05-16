from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from api import views
urlpatterns = [
    url('', views.HomePageView.as_view() ),
]
