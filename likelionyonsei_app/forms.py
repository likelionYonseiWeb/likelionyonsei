from django import forms
from .models import *

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = '__all__'
        widgets = {
            'start_date': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_date': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'url': forms.TextInput(attrs={'placeholder':'https://'},),
        }
        labels = {
            'title': '제목',
            'url': 'URL',
            'start_date': '모집 시작일',
            'end_date': '모집 마감일',
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        labels = {
            'name': '이름',
            'number': '기수',
            'photo': '사진',
            'moto': '한줄소개',
            'detail1': '자기소개',
            'detail2': '멋사 활동을 통해 얻은 것',
            'status': '직책',
        }
        exclude = ('created_at',)

class FoundedForm(forms.ModelForm):
    class Meta:
        model = Founded
        fields = '__all__'
        widgets = {
            'url': forms.TextInput(attrs={'placeholder':'https://'},),
        }
        labels = {
            'name': '회사명',
            'logo': '회사로고',
            'url': 'URL',
        }
        exclude = ('created_at',)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'url': forms.TextInput(attrs={'placeholder':'https://'},),
        }
        labels = {
            'name': '회사명',
            'logo': '회사로고',
            'url': 'URL',
        }
        exclude = ('created_at',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'url': forms.TextInput(attrs={'placeholder':'https://'},),
        }
        labels = {
            'name': '프로젝트명',
            'number': '기수',
            'detail': '프로젝트 소개',
            'logo': '프로젝트 로고',
            'url': 'URL',
        }
        exclude = ('created_at',)