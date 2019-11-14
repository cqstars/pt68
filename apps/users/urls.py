# -*- coding: utf-8 -*-
# @Time    : 2019-11-13 18:04
# @Author  : 彭涛
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.indexview.as_view(), name='index'),
    path('login', views.loginview.as_view(), name='login'),
]