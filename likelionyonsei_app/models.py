from django.db import models

class likelion(models.Model):
    apple = models.CharField(max_length=100)
    banana = models.PositiveIntegerField(default=1)
    cow = models.ImageField(null=True, blank=True)
