# -*- coding: utf-8 -*-
# @Time    : 2019-11-22 11:52
# @Author  : 彭涛
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path,re_path
from django.views.generic import TemplateView

from . import views
app_name = 'sc_card'
urlpatterns = [
    path('', views.indexview.as_view(), name='index'),
    path('game_detail/<int:id>/', views.game_detailview.as_view(), name='game_detail'),
    path('setgame', views.setgameview.as_view(), name='setgame'),

    # path('login', views.LoginView.as_view(), name='login'),
    # path('reg', views.regview.as_view(), name='reg'),
    # path('fpw', views.fpwView.as_view(), name='fpw'),
]