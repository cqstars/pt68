from django.db import models
from datetime import datetime
from users.models import UserProfile


# Create your models here.
class bloodsuger(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="检查血糖时间")
    bloodsugernum = models.DecimalField(default=0,max_digits=3,decimal_places=2, verbose_name="血糖值")
    submituser=models.ForeignKey(UserProfile,blank=True,null=True, on_delete=models.CASCADE, verbose_name="检测人",related_name="user")
    marks = models.CharField(max_length=150, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = "血糖监测"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "血糖监测"