from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from api.models import *
from api.models import Attendees1 as Attendees, EventTypes1 as EventTypes, Orders1, Discount1, Employees1, Avatars1Events
from api.serializers import AttendeesSerializer, EventTypesSerializer, OrdersSerializer, ShowmanHouseSerializer,\
    CountrySerializer, CitySerializer, AddressSerializer, DiscountSerializer, PaymentMethodSerializer,\
    FeeScheduleSerializer, EmployeesSerializer, OurEventsSerializer, AvatarSerializer, EventAvatarSerializer
# from api.filters import ProductFilter
from api.serializers import UserSerializer
from rest_framework import viewsets
from api.filters import OrderFilter, EventFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "C:/xd_team.project/showmanhouseback/ShowmanHouse/showmanbackdjango2/welcom.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_articles']=


class EventTypesList(generics.ListCreateAPIView):
    serializer_class = EventTypesSerializer
    permission_classes = (IsAuthenticated,)
    # pagination_class = LimitOffsetPagination

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)

    filter_class = EventFilter

    search_fields = ('event_title', 'event_description')

    ordering_fields = ('id', 'event_title')

    ordering = ('id',)

    def get_queryset(self):
        return EventTypes.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class EventTypesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventTypesSerializer
    def get_queryset(self):
        queryset = EventTypes1.objects.get(id=self.kwargs.get('pk'))
        return queryset


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    lookup_url_kwarg = "pk2"

    def get_queryset(self):
        try:
            category = Attendees1.objects.get(id=self.kwargs.get('pk'))
        except Attendees1.DoesNotExist:
            raise Http404
        queryset = category.customers.filter(id=self.kwargs.get('pk2'))
        return queryset

class AttendeesList(generics.ListCreateAPIView):
    serializer_class = AttendeesSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Attendees.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class EmployeesList(generics.ListCreateAPIView):
    serializer_class = EmployeesSerializer

        # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Employees1.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class OurEventsList(generics.ListCreateAPIView):
    serializer_class = OurEventsSerializer


    def get_queryset(self):
        return OurEvents1.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class OurEventsList2(generics.ListCreateAPIView):
    serializer_class = OurEventsSerializer

    permission_classes = (IsAuthenticated,)

    pagination_class = LimitOffsetPagination



    def get_queryset(self):
        return OurEvents1.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DiscountList(generics.ListCreateAPIView):
    serializer_class = DiscountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Discount1.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PaymentList(generics.ListCreateAPIView):
    serializer_class = PaymentMethodSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return PaymentMethod1.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class FeeList(generics.ListCreateAPIView):
    serializer_class = FeeScheduleSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return FeeSchedule1.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AvatarList(generics.ListCreateAPIView):
    serializer_class = AvatarSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Avatars1.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EventAvatarList(generics.ListCreateAPIView):
    serializer_class = EventAvatarSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Avatars1Events.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AttendeesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttendeesSerializer
    def get_queryset(self):
        queryset = Attendees.objects.get(id=self.kwargs.get('pk'))
        return queryset


class OrdersList(generics.ListCreateAPIView):
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated,)

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)

    filter_class = OrderFilter

    ordering_fields = ('id',)

    ordering = ('id',)

    def get_queryset(self):
        return Orders1.creator.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ShowmanHouseList(generics.ListCreateAPIView):
    serializer_class = ShowmanHouseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ShowmanHouse1.objects.all()
        # return ShowmanHouse1.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CityList(generics.ListCreateAPIView):
    serializer_class = CitySerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return City1.objects.all()
        # return ShowmanHouse1.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CountryList(generics.ListCreateAPIView):
    serializer_class = CountrySerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Country1.objects.all()
        # return ShowmanHouse1.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AttendeeOrdersList(generics.ListCreateAPIView):
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Attendees1.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super(UserViewSet, self).get_object()