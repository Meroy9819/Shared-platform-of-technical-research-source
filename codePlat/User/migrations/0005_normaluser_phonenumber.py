# Generated by Django 2.2.1 on 2019-05-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20190524_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='phonenumber',
            field=models.CharField(default='00000000000', max_length=11),
        ),
    ]