from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm


class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        help_texts = {
            'username': None
        }
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este usuario ya existe!")
        return username

class ColabCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este usuario ya existe!")
        return username

class ArteCreationForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Arte
        fields = ['titulo','autor','descripcion','valor','imagen','categoria','mensaje']

    mensaje = forms.CharField(required=False, widget=forms.HiddenInput())

class ArtistaCreationForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model =  Autor
        fields = ['nombre','descripcion','imagen']

class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(label='',widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": ""
    }))


class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'new-password'
    }))

    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'new-password'
    }))



