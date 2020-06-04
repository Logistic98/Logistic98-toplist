from django.urls import path
from . import views

app_name = 'weibodjango'

urlpatterns = [
    path('', views.weibo, name='weibo'),
    path('<int:num>/', views.weibodetail, name='weibodetail'),
]