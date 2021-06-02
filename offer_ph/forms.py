from django import forms
from .models import OfferPhotography
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class OfferForm(forms.ModelForm):
    """Форма добавления места"""

    captcha = ReCaptchaField()

    class Meta:
        model = OfferPhotography
        fields = (
        'name', 'phone_number', 'time_to_call_1', 'time_to_call_2', 'date_of_photography', 'photography', 'сity',
        'comment', 'captcha')
        widgets = {
            'time_to_call_1': forms.Select(attrs={'class': 'select-css'}),
            'time_to_call_2': forms.Select(attrs={'class': 'select-css'}),
            'photography': forms.Select(attrs={'class': 'select-css'}),
            'comment': forms.Textarea(),
        }
