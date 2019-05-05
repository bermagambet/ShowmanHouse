from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from api.models import *
from api.models import Attendees1 as Attendees, EventTypes1 as EventTypes
from api.serializers import AttendeesSerializer, EventTypesSerializer
# from api.filters import ProductFilter


class EventTypesList(generics.ListCreateAPIView):
    serializer_class = EventTypesSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return EventTypes.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EventTypesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventTypesSerializer
    def get_queryset(self):
        queryset = EventTypes1.objects.get(id=self.kwargs.get('pk'))
        return queryset

class FeeScheduleList(generics.ListCreateAPIView):
    # serializer_class = EventTypesSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return FeeSchedule.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PaymentMethodList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return PaymentMethod.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CountryList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Country.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class FederativeRepublicList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return FederativeRepublic.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CityList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return City.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AttendeesList(generics.ListCreateAPIView):
    serializer_class = AttendeesSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Attendees.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AttendeesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttendeesSerializer
    def get_queryset(self):
        queryset = Attendees.objects.get(id=self.kwargs.get('pk'))
        return queryset

class AddressList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Address.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DiscountList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Discount.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ShowmanHouseList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ShowmanHouse.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class OrderList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class EmployeesList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Employees.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AdministrativeStuffList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return AdministrativeStuff.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class EntertainingGroupList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return EntertainingGroup.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class Trainee_List(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Trainee_.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

