from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Review

class ReviewForm(forms.ModelForm):
    """Форма добавления места"""

    captcha = ReCaptchaField()

    class Meta:
        model = Review
        fields = ('review_body', 'captcha')
        exclude = ('author', )
        widgets = {
            'photo': forms.FileInput(attrs={'id': 'photo_inp'}),
            'review_body': forms.Textarea()
        }