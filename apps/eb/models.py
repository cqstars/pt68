from django.db import models
from datetime import datetime
from users.models import UserProfile


# Create your models here.
class bookingobject(models.Model):
    name = models.CharField(max_length=50, verbose_name="记账对象",default="老汉")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="设置时间")

    class Meta:
        verbose_name = "记账对象"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class bookingtype(models.Model):
    name=models.CharField(max_length=50, verbose_name="费用类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="费用类型设置时间")
    class Meta:
        verbose_name = "费用类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class bookingdetail(models.Model):
    bookingobject = models.ForeignKey(bookingobject, on_delete=models.CASCADE, verbose_name="记账对象", related_name="bookingobject")
    bookingtype = models.ForeignKey(bookingtype, on_delete=models.CASCADE, verbose_name="费用类型", related_name="bookingtype")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="记账时间")
    bookingdetail = models.CharField(max_length=150,blank=True,null=True,verbose_name="费用具体内容")
    bookingremarks= models.CharField(max_length=150,blank=True,null=True,verbose_name="费用备注")
    amount= models.DecimalField(default=0,max_digits=9,decimal_places=2, verbose_name="金额")
    issubmit=models.BooleanField(default=False,blank=True,null=True,verbose_name="是否报销")
    verifyuser=models.ForeignKey(UserProfile,blank=True,null=True, on_delete=models.CASCADE, verbose_name="审核",related_name="verifyuser")
    submituser=models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="报销",related_name="submituser")
    class Meta:
        verbose_name = "具体费用"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "费用"
