import json

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from api.models import Attendees1 as Attendees, EventTypes1 as EventTypes

from api.serializers import AttendeesSerializer, EventTypesSerializer



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