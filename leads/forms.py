from django import forms
from django.forms import Form, ModelForm
from . models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

# NOTE using forms we need to define feilds and its type again, we can use builtin Modelform
User = get_user_model()


class LeadModelForm(ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
