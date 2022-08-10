from django.shortcuts import render, redirect
from .models import *
from .forms import RecruitForm
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'home.html')

def alumni(request):
    return render(request, 'alumni.html')

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