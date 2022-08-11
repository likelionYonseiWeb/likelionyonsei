from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils import timezone

# Create your views here.

def home(request):
    founded_form = FoundedForm()
    company_form = CompanyForm()
    project_form = ProjectForm()

    ctx = {
        'founded_form':founded_form, 
        'company_form':company_form,
        'project_form':project_form,
    }
    return render(request, 'home.html', ctx)

def alumni(request):
    members = Member.objects.all()
    member_form = MemberForm()
    return render(request, 'alumni.html', {'members':members, 'member_form':member_form,})

def recruit(request):
    if (request.method == 'POST'):
        form = RecruitForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('recruit')
    else:
        form = RecruitForm()
        # for user
        today = timezone.now()
        recruit_url = Recruit.objects.latest('end_date')
        s_date = recruit_url.start_date
        e_date = recruit_url.end_date
        if (s_date > today or e_date < today):
            recruit_url = Recruit.objects.none()
        return render(request, 'recruit.html', {'form':form, 'recruit_url':recruit_url})

def contact(request):
    return render(request, 'contact.html')

def add_member(request):
    if (request.method == 'POST'):
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('alumni')

def add_founded(request):
    if (request.method == 'POST'):
        form = FoundedForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('home')

def add_company(request):
    if (request.method == 'POST'):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('home')

def add_project(request):
    if (request.method == 'POST'):
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('home')
