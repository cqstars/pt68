from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(bookingtype)
class bookingobjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(bookingobject)
class bookingtypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(bookingdetail)
class bookingdetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'bookingobject','bookingtype')