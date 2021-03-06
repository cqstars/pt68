# Generated by Django 2.2.7 on 2019-11-25 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sc_card', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gamepalyers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='sc_card.game', verbose_name='局名')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL, verbose_name='选手')),
            ],
            options={
                'verbose_name': '选手',
                'verbose_name_plural': '选手',
            },
        ),
    ]
