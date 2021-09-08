from django import forms
from django.forms import Form, ModelForm
from . models import Lead

# NOTE using forms we need to define feilds and its type again, we can use builtin Modelform


class LeadModelForm(ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
