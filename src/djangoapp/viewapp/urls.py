from django.urls import path, include
from . import views

app_name = 'viewapp'

urlpatterns = [
    path('<token>/', views.UploadVotePage.as_view(), name='upload_vote_page'),
]