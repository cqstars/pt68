from django.db import models
from datetime import datetime
from users.models import UserProfile

# Create your models here.
class game(models.Model):
    name = models.CharField(max_length=50, verbose_name="局名",default="首局")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="设置局时间")
    rate=models.IntegerField(default=2,verbose_name="一翻大小")
    ischeck=models.BooleanField(default=False,verbose_name="是否结账")

    class Meta:
        verbose_name = "局名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_gamedetails(self):
        return self.gametodetail.all()

    def get_gamepalyers(self):
        return self.gametoplayer.all()


class gamedetails(models.Model):
    game=models.ForeignKey(game,on_delete=models.CASCADE,verbose_name="局名",related_name="gametodetail")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="时间")
    gamewinner=models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="获胜选手",related_name="gametowinner")
    gameloser1=models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="失败选手1",related_name="gametoloser1")
    gameloser2=models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="失败选手2",related_name="gametoloser2")
    score=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="翻数")

    class Meta:
        verbose_name = "明细"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.game

class gamepalyers(models.Model):
    game = models.ForeignKey(game, on_delete=models.CASCADE, verbose_name="局名",related_name="gametoplayer")
    player = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="选手",related_name="playertouser")
    score = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    class Meta:
        verbose_name = "选手"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.game.name

