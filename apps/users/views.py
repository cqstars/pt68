from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
class indexview(View):
    def get(self,requset):
        return render(requset,"users/index.html")

class loginview(View):
    def get(self,requset):
        return render(requset,"users/login.html")

