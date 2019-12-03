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
        return render(request, "sc_card/index.html",{"current_game":mygame})

    def post(self, request):
        id = request.POST.get("id","")
        game.objects.filter(id=id).update(ischeck=True)
        mygame = game.objects.filter(ischeck=False)
        return render(request, "sc_card/index.html", {"current_game": mygame})



@method_decorator(login_required, name='dispatch')
class setgameview(View):
    def get(self, request):
       players = UserProfile.objects.exclude(is_superuser=True)
       return render(request,"sc_card/setgame.html",{"seluser":players})
    def post(self, request):
        rate = request.POST.get("rate")
        if rate:
            newgame=game()
            newgame.name=request.user.nick_name+timezone.now().strftime("%S")
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
            return HttpResponseRedirect(reverse('sc_card:index'))
        else:
            msg = "没有牌局,或者牌局建立失败！建立牌局"
            players = UserProfile.objects.exclude(is_superuser=True)
            return render(request, "sc_card/setgame.html", {"seluser": players,"msg":msg})

@method_decorator(login_required, name='dispatch')
class game_detailview(View):
    def get(self, request,id):
            this_game=game.objects.get(id=id)
            gamedetail=gamedetails.objects.filter(game_id=id)
            return render(request, "sc_card/game_detail.html",{"game_detail":gamedetail,"this_game":this_game})

    def post(self, request,id):
        score = request.POST.get("score","")
        players=gamepalyers.objects.filter(game_id=id)
        if players.count() > 3 :
            winner=request.POST.get("winner","")
            loser1=request.POST.getlist("loser",[])[0]
            loser2=request.POST.getlist("loser",[])[1]
            new_gamedetail=gamedetails()
            new_gamedetail.game=game.objects.get(id=id)
            new_gamedetail.gamewinner=UserProfile.objects.get(id=winner)
            new_gamedetail.gameloser1=UserProfile.objects.get(id=loser1)
            new_gamedetail.gameloser2=UserProfile.objects.get(id=loser2)
            new_gamedetail.score=score
            new_gamedetail.save()
            this_game = game.objects.get(id=id)
            gamedetail = gamedetails.objects.filter(game_id=id)
            return render(request, "sc_card/game_detail.html", {"game_detail": gamedetail, "this_game": this_game})
        else:
            winner = request.POST.get("winner", "")
            p=players.exclude(player_id=winner)
            loser1 = p[0].player_id
            loser2 = p[1].player_id
            new_gamedetail = gamedetails()
            new_gamedetail.game = game.objects.get(id=id)
            new_gamedetail.gamewinner = UserProfile.objects.get(id=winner)
            new_gamedetail.gameloser1 = UserProfile.objects.get(id=loser1)
            new_gamedetail.gameloser2 = UserProfile.objects.get(id=loser2)
            new_gamedetail.score = score
            new_gamedetail.save()
            this_game = game.objects.get(id=id)
            gamedetail = gamedetails.objects.filter(game_id=id)
            return render(request, "sc_card/game_detail.html", {"game_detail": gamedetail, "this_game": this_game})

def del_gamedetail(request,id):
    gamedetails.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('sc_card:index'))

