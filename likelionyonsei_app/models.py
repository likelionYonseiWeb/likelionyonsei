from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField(default=1)
    photo = models.ImageField(null=True, blank=True)
    moto = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    detail1 = models.TextField()
    detail2 = models.TextField()

    def __str__(self):
        return self.name

class Recruit(models.Model):
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.url

