from django.urls import path
from . import views

app_name = 'navigation'

urlpatterns = [
    path('',views.navigation,name='navigation'),
]