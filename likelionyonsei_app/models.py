from operator import truediv
from django.db import models
from django.utils import timezone

# Create your models here.

class Member(models.Model):
    STATUS_CHOICES = (
        (0, '일반 구성원'),
        (1, '운영진'),
        (2, '부대표'),
        (3, '대표'),
    )

    name = models.CharField(max_length=5)
    number = models.PositiveIntegerField(default=1)
    photo = models.ImageField(null=True, blank=True)
    moto = models.CharField(max_length=20)
    detail1 = models.TextField()
    detail2 = models.TextField()
    status = models.SmallIntegerField(choices = STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Recruit(models.Model):
    title = models.CharField(max_length=10, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

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
    name = models.CharField(max_length=8)
    number = models.PositiveIntegerField(default=1)
    detail = models.CharField(max_length=15)
    logo = models.ImageField(null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    member = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


