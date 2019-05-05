from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from api.models import *
# from api.serializers import CategorySerializer2, ProductSerializer
# from api.filters import ProductFilter


class EventTypesList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # category = get_object_or_404(Category, id=self.kwargs.get('pk'))
        try:
            events = EventTypes.objects.get(id=self.kwargs.get('pk'))
        except EventTypes.DoesNotExist:
            raise Http404
        queryset = events.orders.all()

        # TODO Query params
        # name = self.request.query_params.get('name', None)
        # price = self.request.query_params.get('price', None)
        # if name is not None and price is not None:
        #     queryset = queryset.filter(name=name).filter(price=price)

        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
class FeeScheduleList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

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
        # category = get_object_or_404(Category, id=self.kwargs.get('pk'))
        try:    
            cities = City.objects.get(id=self.kwargs.get('pk'))
        except City.DoesNotExist:
            raise Http404
        queryset = cities.adresses.all()

        # TODO Query params
        # name = self.request.query_params.get('name', None)
        # price = self.request.query_params.get('price', None)
        # if name is not None and price is not None:
        #     queryset = queryset.filter(name=name).filter(price=price)

        return queryset
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AttendeesList(generics.ListCreateAPIView):
    # serializer_class = CategorySerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # category = get_object_or_404(Category, id=self.kwargs.get('pk'))
        try:
            attendees = Attendees.objects.get(id=self.kwargs.get('pk'))
        except Attendees.DoesNotExist:
            raise Http404
        queryset = attendees.orders.all()

        # TODO Query params
        # name = self.request.query_params.get('name', None)
        # price = self.request.query_params.get('price', None)
        # if name is not None and price is not None:
        #     queryset = queryset.filter(name=name).filter(price=price)

        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


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
        # category = get_object_or_404(Category, id=self.kwargs.get('pk'))
        try:
            showmanhouses = ShowmanHouse.objects.get(id=self.kwargs.get('pk'))
        except ShowmanHouse.DoesNotExist:
            raise Http404
        queryset = showmanhouses.orders.all()

        # TODO Query params
        # name = self.request.query_params.get('name', None)
        # price = self.request.query_params.get('price', None)
        # if name is not None and price is not None:
        #     queryset = queryset.filter(name=name).filter(price=price)

        return queryset


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

