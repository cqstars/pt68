# -*- coding: utf-8 -*-
# @Time    : 2020-06-10 21:34
# @Author  : 彭涛
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

app_name = 'bloodsugermonitor'
urlpatterns = [
    path('', views.indexview.as_view(), name='index'),
]