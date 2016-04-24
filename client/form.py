from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from client.models import *

__author__ = 'yasina'

class ClientFileForm(forms.ModelForm):

    class Meta:
        model = ClientFileModel
        fields = '__all__'