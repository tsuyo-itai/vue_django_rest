from django.contrib import admin

# Register your models here.
from myapp.models import TestModel, RoomModel
admin.site.register(TestModel)
admin.site.register(RoomModel)