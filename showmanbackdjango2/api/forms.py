from form_utils import forms


class ImageUploadForm(forms.forms.Form):
    """Image upload form."""
    image = forms.forms.ImageField()