from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError


class NewsForms(forms.ModelForm):
    class Meta:
        model = EventsBlonck
        # fields = '__all__'
        fields = ['name', 'test', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'test': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('Название не начинается с цифры')
        return name
