from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Пароли не совпадают")
        return data['password2']
