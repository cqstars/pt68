# Generated by Django 2.2.7 on 2020-05-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eb', '0003_bookingdetail_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetail',
            name='issubmit',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='是否报销'),
        ),
        migrations.AlterField(
            model_name='bookingdetail',
            name='bookingdetail',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='费用具体内容'),
        ),
        migrations.AlterField(
            model_name='bookingdetail',
            name='bookingremarks',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='费用备注'),
        ),
    ]
