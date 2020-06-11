from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from django.views.generic.base import View, TemplateView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse
import operator
from functools import reduce
from django.db.models import Sum

from .form import *
from .models import *
from users.models import *
import json


# Create your views here.
@method_decorator(login_required, name='dispatch')
class indexview(View):
    def get(self, request):
        return render(request, "eb/index.html", )

    def post(self, request):
        return render(request, "eb/index.html")


class bookingview(View):
    def get(self, request):
        allbookingofuser = bookingdetail.objects.filter(Q(submituser_id=request.user.id), Q(issubmit=False))
        form = bookingdetailModelForm(initial={"bookingobject": [1, ]})
        return render(request, 'eb/booking.html', {"form": form, "booking": allbookingofuser})

    def post(self, request):
        allbookingofuser = bookingdetail.objects.filter(Q(submituser_id=request.user.id), Q(issubmit=False))
        form = bookingdetailModelForm(data=request.POST)
        if form.is_valid():
            # 保存数据
            bookingde = form.save(commit=False)  # commit=False告诉Django先不提交到数据库.
            bookingde.submituser = request.user  # 添加额外数据
            bookingde.save()  # 发送到数据库
            form1 = bookingdetailModelForm(initial={"bookingobject": [1, ]})
            return render(request, 'eb/booking.html', {"form": form1, "booking": allbookingofuser, "message": "提交成功"})
        else:
            return render(request, 'eb/booking.html',
                          {"form": form, "booking": allbookingofuser, "message": "网络原因，没有提交成功"})


def delbook(request, id):
    bookingdetail.objects.filter(id=id).delete()
    allbookingofuser = bookingdetail.objects.filter(Q(submituser_id=request.user.id), Q(issubmit=False))
    form = bookingdetailModelForm(initial={"bookingobject": [1, ]})
    return render(request, 'eb/booking.html', {"form": form, "booking": allbookingofuser})


def inquery(request):
    if request.method == 'GET':
        user = UserProfile.objects.filter(user_type='2');
        expensestype = bookingtype.objects.all()
        return render(request, 'eb/inquery.html', {'submituser': user, 'expensestype': expensestype})
    else:
        hasvalue = []
        starttime = request.POST.get("starttime")
        endtime = request.POST.get("endtime")
        submituser = request.POST["submituser"]
        expensestype = request.POST.get("expensestype", "")
        issubmit = request.POST.get("issubmit", "")
        if starttime and endtime:
            q_obj = Q(add_time__range=(starttime, endtime))
            hasvalue.append(q_obj)

        if submituser != 'null':
            q_obj = Q(submituser_id=submituser)
            hasvalue.append(q_obj)

        if issubmit != 'null':
            q_obj = Q(issubmit=issubmit)
            hasvalue.append(q_obj)

        if expensestype != 'null':
            q_obj = Q(bookingtype_id=expensestype)
            hasvalue.append(q_obj)

        if hasvalue:
            result = bookingdetail.objects.filter(reduce(operator.and_, hasvalue))
            hz = result.aggregate(Sum("amount"))
            return render(request, 'eb/inquery_result.html', {'result': result, "hz": hz["amount__sum"]})
        else:
            result = bookingdetail.objects.all()
            hz = result.aggregate(Sum("amount"))
            return render(request, 'eb/inquery_result.html', {'result': result, "hz": hz["amount__sum"]})


def verify(request):
    if request.method == 'GET':
        bookingisnotverify = bookingdetail.objects.filter(Q(issubmit=False), Q(submituser_id=request.user.id))
        hz = bookingisnotverify.aggregate(Sum("amount"))
        return render(request, 'eb/verify.html', {'book': bookingisnotverify, "hz": hz['amount__sum']})
    else:
        id = request.POST["id"]
        try:
            bookingdetail.objects.filter(id=id).update(issubmit=True, verifyuser_id=request.user.id)


        except:
            return HttpResponse("fail")

        return HttpResponse("ok")
