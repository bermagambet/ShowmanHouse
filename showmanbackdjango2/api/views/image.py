from api.models import Avatars1 as Avatars
from api.forms import ImageUploadForm
from django.http import JsonResponse
from api.serializers import AvatarSerializer


# def upload_pic(request, pk2):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             m = Avatars.objects.get(id=pk2)
#             m.avatar = form.cleaned_data['image']
#             m.save
#             return JsonResponse({'error':'image upload success'})
#     if request.method == 'GET':
#         # form = ImageUploadForm(request.GET, request.FILES)
#         # if form.is_valid():
#             m = Avatars.objects.get(id=pk2)
#             serializer = AvatarSerializer(m)
#             return JsonResponse(serializer.data)
#     return JsonResponse({'error':'image upload failure'})

# def gallery(request):
#     img = Avatars.objects.filter(file_type='image')
#     return render(request, '')


# def get_pic(request):
