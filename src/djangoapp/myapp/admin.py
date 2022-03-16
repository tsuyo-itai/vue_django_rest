from django.contrib import admin

# Register your models here.
from myapp.models import TestModel
admin.site.register(TestModel)