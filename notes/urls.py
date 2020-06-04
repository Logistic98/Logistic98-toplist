# notes/urls.py

from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详细页面
    path('topics/<topic_id>', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),
]