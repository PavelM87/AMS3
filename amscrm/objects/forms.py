from django import forms
from .models import Object


class ObjectModelForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = '__all__'