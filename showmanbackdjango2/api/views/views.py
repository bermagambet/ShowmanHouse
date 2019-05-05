import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from api.models import *
# # from api.serializers import CategorySerializer, CategorySerializer2, ProductSerializer
#
#
# @csrf_exempt
# def EventTypes_list(request):
#     if request.method == 'GET':
#         eventtypess = EventTypes.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def FeeSchedule_list(request):
#     if request.method == 'GET':
#         feeschedules = FeeSchedule.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def PaymentMethod_list(request):
#     if request.method == 'GET':
#         payments = PaymentMethod.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def Country_list(request):
#     if request.method == 'GET':
#         countries = Country.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def FederativeRepublic_list(request):
#     if request.method == 'GET':
#         federativerepublics = FederativeRepublic.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def City_list(request):
#     if request.method == 'GET':
#         cities = City.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def Attendees_list(request):
#     if request.method == 'GET':
#         attendees = Attendees.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def Address_list(request):
#     if request.method == 'GET':
#         addresses = Address.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def Discount_list(request):
#     if request.method == 'GET':
#         discounts = Discount.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def Events_list(request):
#     if request.method == 'GET':
#         events = Events.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def ShowmanHouse_list(request):
#     if request.method == 'GET':
#         showmanhouses = ShowmanHouse.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def Order_list(request):
#     if request.method == 'GET':
#         orders = Order.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def Employees_list(request):
#     if request.method == 'GET':
#         employees = Employees.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def AdministrativeStuff_list(request):
#     if request.method == 'GET':
#         administrativestuffs = AdministrativeStuff.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def EntertainingGroup_list(request):
#     if request.method == 'GET':
#         entertaininggroups = EntertainingGroup.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})
#
# @csrf_exempt
# def Trainee_list(request):
#     if request.method == 'GET':
#         trainees = Trainee.objects.all()
#         # serializer = CategorySerializer2(categories, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         # serializer = CategorySerializer2(data=body)
#         if serializer.is_valid():
#             # create function from serializer
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#     return JsonResponse({'error': 'bad request'})