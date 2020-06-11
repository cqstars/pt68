# -*- coding: utf-8 -*-
# @Time    : 2020-05-09 17:36
# @Author  : 彭涛
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, re_path
from django.views.generic import TemplateView

from . import views

app_name = 'eb'
urlpatterns = [
    path('', views.indexview.as_view(), name='index'),
    path('booking', views.bookingview.as_view(), name='booking'),
    path('delbooking/<int:id>/',views.delbook, name='delbooking'),
    path('inquery',views.inquery, name='inquery'),
    path('verify',views.verify, name='verify'),
]
