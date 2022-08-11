"""likelionyonsei_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from likelionyonsei_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('alumni/', alumni, name="alumni"),
    path('recruit/', recruit, name="recruit"),
    path('contact/', contact, name="contact"),
    path('add_member/', add_member, name="add_member"),
    path('add_founded/', add_founded, name="add_founded"),
    path('add_company/', add_company, name="add_company"),
    path('add_project/', add_project, name="add_project"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
