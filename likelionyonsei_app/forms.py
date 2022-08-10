from django import forms
from .models import Recruit

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['url', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }