# Generated by Django 2.2.7 on 2019-11-25 03:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='首局', max_length=50, verbose_name='局名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='设置局时间')),
                ('rate', models.IntegerField(default=2, verbose_name='一翻大小')),
                ('ischeck', models.BooleanField(default=False, verbose_name='是否结账')),
            ],
            options={
                'verbose_name': '局名',
                'verbose_name_plural': '局名',
            },
        ),
        migrations.CreateModel(
            name='gamedetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='时间')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sc_card.game', verbose_name='局名')),
                ('gameloser1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameloser1', to=settings.AUTH_USER_MODEL, verbose_name='失败选手1')),
                ('gameloser2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameloser12', to=settings.AUTH_USER_MODEL, verbose_name='失败选手2')),
                ('gamewinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamewinner', to=settings.AUTH_USER_MODEL, verbose_name='获胜选手')),
            ],
            options={
                'verbose_name': '明细',
                'verbose_name_plural': '明细',
            },
        ),
    ]