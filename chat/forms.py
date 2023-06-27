from django import forms
from chat.models import *


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["name"]

