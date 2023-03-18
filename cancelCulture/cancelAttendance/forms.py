
# import form class from django
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets 
  
# import GeeksModel from models.py
from .models import *
  
# create a ModelForm
class leavereqForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = leavereq
        fields = "__all__"
        