from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('v1/', include('myapp.api.urls')),
]