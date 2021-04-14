from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser, Team


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('userName', 'userSurname', 'userTel', 'userEmail', 'userRole')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('userName', 'userSurname', 'userTel', 'userEmail', 'userRole')


class UserModelForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('userName', 'userSurname', 'userTel', 'userEmail', 'userRole', 'is_active')


class TeamModelForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('member',)

