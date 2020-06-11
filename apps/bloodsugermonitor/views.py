from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required, name='dispatch')
class indexview(View):
    def get(self, request):
        return render(request, "bloodsugarmonitor/index.html", )

    def post(self, request):
        return render(request, "bloodsugarmonitor/index.html")