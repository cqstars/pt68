"""pt68 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name="pc.html"), name="index"),
    path('jp', TemplateView.as_view(template_name="jp/jp.html"), name="jp"),
    path('nmn', TemplateView.as_view(template_name="jp/Nmusicnotation.html"), name="nmn"),
    path('game', TemplateView.as_view(template_name="canvas/game.html"), name="game"),
    path('', include('index.urls', 'index')),
    path('users/', include('users.urls', 'users')),
    path('sc_card/', include('sc_card.urls', 'sc_card')),
    path('eb/', include('eb.urls', 'eb')),
    path('blood/', include('bloodsugermonitor.urls', 'bloodsugermonitor')),

]
