from django import forms
from django.core.exceptions import ValidationError

from slider_app.models import Mail


class MicromodalForm(forms.ModelForm):
    """ Всплывающая форма. """
    class Meta:
        model = Mail
        fields = ('name', 'phone', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input modal__input', 'placeholder': 'Ваше имя...'}),
            'phone': forms.TextInput(attrs={'class': 'form-input modal__input', 'placeholder': 'Ваш телефон...'}),
            'message': forms.Textarea(attrs={'class': 'form-input modal__input',
                                             'placeholder': 'Сообщение...', 'cols': 30, 'rows': 6}),
        }

