# -*- coding: utf-8 -*-
# @Time    : 2019-11-14 18:08
# @Author  : 彭涛
# @Site    : 
# @File    : forms.py
# @Software: PyCharm
from django import forms
from .models import UserProfile

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label="重复输入密码")
    class Meta:
        model = UserProfile
        fields = ['username','password','password2','email','mobile',]
        widgets = {
            'username': forms.TextInput(attrs={'class':'txt'}),
            'password': forms.TextInput(attrs={'class':'txt'}),
        }
        error_messages = None  # 自定义错误信息
        # error_messages用法：
        error_messages = {
            # 'username': {'required': "用户名不能为空", },
            # 'password': {'required': "密码不能为空", },
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

        self.fields['mobile'].required = True


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('两次输入密码不匹配')
        return cd['password2']

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

class verifycodeForm(forms.Form):
    mobil = forms.CharField(required=True)
    code = forms.CharField(required=False,min_length=5)


class reset_pwForm(forms.Form):
    password = forms.CharField(required=True)
    passsword1 = forms.CharField(required=True, min_length=5)