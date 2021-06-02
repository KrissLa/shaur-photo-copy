from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Place

class PlacesForm(forms.ModelForm):
    """Форма добавления места"""

    captcha = ReCaptchaField()
    class Meta:
        model = Place
        fields = ('user_name', 'sity', 'title', 'photo', 'url_map', 'description', 'captcha')
        widgets = {
            'photo': forms.FileInput(attrs={'id': 'photo_inp'}),
            'description': forms.Textarea()
        }