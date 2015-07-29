from django.contrib.admin import forms
from django.forms import ModelForm, Form
from django.forms.extras.widgets import SelectDateWidget
from main.models import Order

class OrderForm(ModelForm):
    class Meta():
        model = Order

        widgets = {
            'date': SelectDateWidget(years=range(2015, 2016))
        }

        fields = ('user', 'date',)
