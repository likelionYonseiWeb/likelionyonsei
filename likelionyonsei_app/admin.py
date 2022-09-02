from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Member)
admin.site.register(Recruit)
admin.site.register(Company)
admin.site.register(Project)