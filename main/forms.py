import json
import urllib
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from django.forms import DateInput


class OrderForm(forms.Form):
    # TODO replace this hardcode!
    url = 'http://localhost:8000/ajax/available-days'
    r = urllib.request.urlopen(url)
    dates = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    date = forms.DateField(
                           label="Оберіть дату замовлення",
                           widget=DateInput(format='%Y-%m-%d'),
                           input_formats=['%Y-%m-%d'], )


class LoginUserForm(forms.Form):
    username = forms.CharField(validators=[validate_slug], min_length=3, max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(min_length=3,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(validators=[validate_slug], min_length=3, max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'},
                                                      ))
    password1 = forms.CharField(min_length=6,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(min_length=6,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self):
        user = super(RegistrationForm, self).save()
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email
