# Generated by Django 2.2.7 on 2020-05-12 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingdetail',
            name='name',
        ),
        migrations.AlterField(
            model_name='bookingdetail',
            name='bookingobject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookingobject', to='eb.bookingobject', verbose_name='记账对象'),
        ),
        migrations.AlterField(
            model_name='bookingdetail',
            name='bookingtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookingtype', to='eb.bookingtype', verbose_name='费用类型'),
        ),
    ]
