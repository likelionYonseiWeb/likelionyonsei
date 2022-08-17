from operator import truediv
from django.db import models
from django.utils import timezone

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField(default=1)
    photo = models.ImageField(null=True, blank=True)
    moto = models.CharField(max_length=300)
    job = models.CharField(max_length=100)
    detail1 = models.TextField()
    detail2 = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Recruit(models.Model):
    url = models.CharField(max_length=500)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.url

class Founded(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    url = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    url = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=10)
    number = models.PositiveIntegerField(default=1)
    detail = models.CharField(max_length=15)
    logo = models.ImageField(null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


