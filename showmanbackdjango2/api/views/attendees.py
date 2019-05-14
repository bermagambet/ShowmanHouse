import json

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from api.models import Attendees1 as Attendees, EventTypes1 as EventTypes,\
    Orders1 as Orders, ShowmanHouse1 as ShowmanHouse, Address1, City1, Country1, Discount1,\
    PaymentMethod1, FeeSchedule1, Employees1, Avatars1, Avatars1Events, OurEvents1

from api.serializers import AttendeesSerializer, EventTypesSerializer, OrdersSerializer,\
    ShowmanHouseSerializer, AddressSerializer, CitySerializer, CountrySerializer,\
    DiscountSerializer, PaymentMethodSerializer, FeeScheduleSerializer,\
    EmployeesSerializer, AvatarSerializer, EventAvatarSerializer, OurEventsSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view


@csrf_exempt
def attendee_detail(request, pk):
    try:
        category = Attendees.objects.get(id=pk)
    except Attendees.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = AttendeesSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = AttendeesSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def eventtype_detail(request, pk):
    try:
        category = EventTypes.objects.get(id=pk)
    except Attendees.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = EventTypesSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = EventTypesSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def orders_detail(request, pk):
    try:
        category = Orders.creator.get(id=pk)
    except Orders.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = OrdersSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = OrdersSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def showmanhouse_detail(request, pk):
    try:
        category = ShowmanHouse.objects.get(id=pk)
    except ShowmanHouse.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = ShowmanHouseSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = ShowmanHouseSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


def adress_detail(request, pk):
    try:
        category = Address1.objects.get(id=pk)
    except Address1.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = AddressSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = AddressSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': 'bad request'})
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})



@csrf_exempt
def city_detail(request, pk):
    try:
        category = City1.objects.get(id=pk)
    except City1.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = CitySerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body.decode)
        serializer = CitySerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"xd":"xd"})
        return JsonResponse({'error': 'bad request'})
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def country_detail(request, pk):
    try:
        category = Country1.objects.get(id=pk)
    except Country1.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = CountrySerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = CountrySerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def discount_detail(request, pk):
    try:
        category = Discount1.objects.get(id=pk)
    except Discount1.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = DiscountSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = DiscountSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def payment_detail(request, pk):
    try:
        category = PaymentMethod1.objects.get(id=pk)
    except PaymentMethod1.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = PaymentMethodSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = PaymentMethodSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})



@csrf_exempt
def fee_detail(request, pk):
    try:
        category = FeeSchedule1.objects.get(id=pk)
    except FeeSchedule1.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = FeeScheduleSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = FeeScheduleSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})



@csrf_exempt
def employee_detail(request, pk):
    try:
        category = Employees1.objects.get(id=pk)
    except Employees1.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = EmployeesSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = EmployeesSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def ourevent_detail(request, pk):
    try:
        category = OurEvents1.objects.get(id=pk)
    except OurEvents1.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = OurEventsSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = OurEventsSerializer(instance=category, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def avatar_detail(request, pk):
    try:
        category = Avatars1.objects.get(id=pk)
    except Avatars1.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = AvatarSerializer(category)
        return JsonResponse(serializer.data)
    return JsonResponse({"error":"error"})


@csrf_exempt
def eventavatar_detail(request, pk):
    try:
        category = Avatars1Events.objects.get(id=pk)
    except Avatars1Events.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = EventAvatarSerializer(category)
        return JsonResponse(serializer.data)
    return JsonResponse({"error":"error"})