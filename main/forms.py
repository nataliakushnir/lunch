from django import forms
from django.core.validators import validate_slug
from django.forms import ModelForm
from main.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('date',)


class LoginUserForm(forms.Form):
    username = forms.CharField(validators=[validate_slug], min_length=3, max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(min_length=3,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
