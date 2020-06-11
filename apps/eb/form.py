# -*- coding: utf-8 -*-
# @Time    : 2020-05-12 12:28
# @Author  : 彭涛
# @Site    : 
# @File    : form.py
# @Software: PyCharm

from . import models
from django.forms import ModelForm
from django.forms.widgets import Textarea

class bookingdetailModelForm(ModelForm):

    class Meta:
        model = models.bookingdetail  #对应的Model类
        fields = '__all__'  #对应的Model类中字段
        exclude = ['add_time','issubmit','verifyuser','submituser']     #排除的字段
        labels = {
            "bookingtype":"费用分类"
        }
        help_texts = {
            "bookingtype":"费用分类必须选择" #自定义帮助信息
        }
        error_messages = {
            "bookingtype":{"required":"费用分类必须选择"}  #自定义错误信息
        }
        widgets = {
            # "bookingdetail":Textarea(attrs={"class":"form-control"}) #自定义属性
        }