from django.urls import path
from . import views

app_name = 'github'

urlpatterns = [
    path('',views.github,name='github'),
]