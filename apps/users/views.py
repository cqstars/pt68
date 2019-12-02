from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from django.views.generic.base import View, TemplateView
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# 秒嘀短信API实现
# Refer to: http://www.miaodiyun.com/doc/guide.html
from urllib import parse
import http.client, urllib, hashlib, datetime, time, json  # 加载模块
import random

from .forms import *


# 随机四位数字
def generate_code():
    # 定义一个种子，从这里面随机拿出一个值，可以是字母
    seeds = "1234567890"
    # 定义一个空列表，每次循环，将拿到的值，加入列表
    random_num = []
    # choice函数：每次从seeds拿一个值，加入列表
    for i in range(4):
        random_num.append(random.choice(seeds))
    # 将列表里的值，变成四位字符串
    return "".join(random_num)


# 发送行业短信
def sendIndustrySms(tos, templateid, param):
    # 定义账号和密码，开户之后可以从用户中心得到这两个值
    accountSid = 'b4a69102a48e447d8a2f4da7067635b5'
    acctKey = '39f04ab448b19c4936240a41bc4b040a'

    # 定义地址，端口等
    serverHost = "openapi.miaodiyun.com"
    serverPort = 443
    industryUrl = "/distributor/sendSMS"

    # 格式化时间戳，并计算签名
    timeStamp = str(int(round(time.time() * 1000)))
    rawsig = accountSid + acctKey + timeStamp
    m = hashlib.md5()
    m.update(rawsig.encode('utf-8'))
    sig = m.hexdigest()

    # 定义需要进行发送的数据表单
    params = urllib.parse.urlencode({'accountSid': accountSid,
                                     'templateid': templateid,
                                     'to': tos,
                                     'timestamp': timeStamp,
                                     'sig': sig,
                                     'param': param})

    # 定义header
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}

    # 与构建https连接
    conn = http.client.HTTPSConnection(serverHost, serverPort)

    # Post数据
    conn.request(method="POST", url=industryUrl, body=params, headers=headers)

    # 返回处理后的数据
    response = conn.getresponse()
    # 读取返回数据
    jsondata = response.read().decode('utf-8')

    # 打印完整的返回数据
    print(jsondata)

    # 解析json，获取特定的几个字段
    jsonObj = json.loads(jsondata)
    respCode = jsonObj['respCode']
    print("错误码:", respCode)
    respDesc = jsonObj['respDesc']
    print("错误描述:", respDesc)

    # 关闭连接
    conn.close()


# Create your views here.
class indexview(View):
    def get(self, requset):
        return render(requset, "users/index.html")


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class regview(View):
    def get(self, requset):
        regform = RegisterForm()
        return render(requset, "users/reg.html", {"f": regform})

    def post(self, request):
        reguser = RegisterForm(request.POST)
        if reguser.is_valid():
            new_user = reguser.save(commit=False)
            # 提交的密码加密后写入数据库
            new_user.password = make_password(request.POST.get("password"))
            new_user.save()
            reguser.save_m2m()
            return render(request, "users/regok.html", {"user": new_user.username})
        else:
            return render(request, "users/reg.html", {"f": reguser})


class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(request, username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("users:index"))
                else:
                    return render(request, "users/login.html", {"msg": "用户未激活！"})
            else:
                return render(request, "users/login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request, "users/login.html", {"login_form": login_form})


class fpwView(View):
    def get(self, request):
        v_code = verifycodeForm()
        return render(request, "users/fpw.html", {"f": v_code})

    def post(self, request):

        if request.POST.get("action") == 'getverficode':
            mobile = request.POST.get("mobile")
            tos = mobile
            templateid = 240530
            param1 = generate_code()
            # 提交短信
            sendIndustrySms(tos, templateid, param1)
            return render(request, "users/verifycode.html")
        if request.POST.get("action") == 'verifycode':
            pw_ = reset_pwForm()
            return render(request, "users/resetpw.html")
        if request.POST.get("action") == 'reset_pw':
            pw1 = request.POST.get('pw1')
            return HttpResponse(pw1 + "resetok")
