from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from django.views.generic.base import View, TemplateView
from django.utils import timezone

from .models import *
from users.models import UserProfile
from .forms import *

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class indexview(View):
    def get(self, request):
        mygame=game.objects.filter(ischeck=False)
        if mygame:
            return render(request, "sc_card/index.html",{"current_game":mygame})
        else:
            players=UserProfile.objects.exclude(is_superuser=True)
            return render(request,"sc_card/nogame_set.html",{"seluser":players})


    def post(self, request):
        id = request.POST.get("id","")
        if id:
            game.objects.filter(id=id).update(ischeck=True)
            mygame = game.objects.filter(ischeck=False)
            if mygame:
                return render(request, "sc_card/index.html", {"current_game": mygame})
            else:
                players = UserProfile.objects.exclude(is_superuser=True)
                return render(request, "sc_card/nogame_set.html", {"seluser": players})
        else:
            mygame = game.objects.filter(ischeck=False)
            if mygame:
                return render(request, "sc_card/index.html", {"current_game": mygame})
            else:
                players = UserProfile.objects.exclude(is_superuser=True)
                return render(request, "sc_card/nogame_set.html", {"seluser": players})


@method_decorator(login_required, name='dispatch')
class setgameview(View):
    def get(self, request):
       players = UserProfile.objects.exclude(is_superuser=True)
       return render(request,"sc_card/setgame.html",{"seluser":players})
    def post(self, request):
        rate = request.POST.get("rate")
        if rate:
            newgame=game()
            newgame.name=request.user.nick_name+timezone.now().strftime("%d%H")
            newgame.rate=rate
            newgame.save()
            newgameid=newgame.id
            for i in request.POST.keys():  # 使用in判断'player'是否存在于request.POST.keys的键中
                if "player" in i:
                    try:
                        insgameplayer = gamepalyers()
                        insgameplayer.game = game.objects.get(id=newgameid)
                        insgameplayer.player = UserProfile.objects.get(id=request.POST.get(i))
                        insgameplayer.save()
                    except Exception as e:
                        raise e

                else:
                    msg="没有用户，牌局设置失败！"
                    players = UserProfile.objects.exclude(is_superuser=True)
                    return render(request, "sc_card/setgame.html", {"seluser": players, "msg": msg})

            else:
                msg="牌局建立成功！"

            players = UserProfile.objects.exclude(is_superuser=True)
            return render(request, "sc_card/setgame.html", {"seluser": players,"msg":msg})
        else:
            msg = "牌局建立失败！"
            players = UserProfile.objects.exclude(is_superuser=True)
            return render(request, "sc_card/setgame.html", {"seluser": players,"msg":msg})

@method_decorator(login_required, name='dispatch')
class game_detailview(View):
    def get(self, request,id):
            my_form=account()
            gamedetail=gamedetails.objects.filter(game_id=id)
            return render(request, "sc_card/game_detail.html",{"f":my_form,"gamedetail":gamedetail})



    def post(self, request):
        rate = request.POST.get("rate")
        if rate:
            mygame=game()
            mygame.name=request.user.nick_name
            mygame.rate=rate
            mygame.save()
            gameid=mygame.id
            get_player = request.POST.get("player").split(',')

            for i in get_player:
                insgameplayer = gamepalyers()
                insgameplayer.game=game.objects.get(id=gameid)
                insgameplayer.player=UserProfile.objects.get(id=i)
                insgameplayer.save()
            return HttpResponse("设置成功！")
        else:
            bookdata = booking(request.POST)
            if bookdata.is_valid():
                # 保存数据
                bookdata.save()
                mygame = game.objects.filter(ischeck=False)
                my_form = account()
                gamedetail = gamedetails.objects.all()
                return render(request, "sc_card/index.html",{"current_game": mygame, "f": my_form, "gamedetail": gamedetail})
            else:
                mygame = game.objects.filter(ischeck=False)
                my_form = account()
                gamedetail = gamedetails.objects.all()
                return render(request, "sc_card/index.html",{"current_game": mygame, "f": my_form, "gamedetail": gamedetail})