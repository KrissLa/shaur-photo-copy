from django import forms

class EmailAlbumForm(forms.Form):
    """Форма для отправки альбома другу"""
    name = forms.CharField(max_length=50, help_text='Введите Ваше имя')
    email_to = forms.EmailField(help_text='Введите E-mail получателя')
    comments = forms.CharField(widget=forms.TextInput(attrs={'type': 'textarea'}))