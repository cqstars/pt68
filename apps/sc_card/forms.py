# -*- coding: utf-8 -*-
# @Time    : 2019-11-27 20:58
# @Author  : 彭涛
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from django import forms
from .models import *
from users.models import UserProfile

#models.py
class booking(forms.ModelForm):
    class Meta:
        model=gamedetails
        fields = ['game','gamewinner','gameloser1','gameloser2','score',]

class account(forms.Form):
    thisgame= forms.ChoiceField(choices=game.objects.values_list('id','name'))
    gamewinner = forms.ChoiceField(choices=UserProfile.objects.values_list('id','nick_name'))
    score= forms.DecimalField()




