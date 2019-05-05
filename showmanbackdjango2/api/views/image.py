from api.models import Avatars1 as Avatars
from api.forms import ImageUploadForm
from django.http import JsonResponse


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Avatars.objects.get(pk=id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return JsonResponse({'error':'image upload success'})
    return JsonResponse({'error':'image upload failure'})