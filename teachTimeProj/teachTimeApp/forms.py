from django import forms
from .models import TimeCard


class TimeCardForm(forms.ModelForm):
    class Meta():
        model = TimeCard
        fields = '__all__'
