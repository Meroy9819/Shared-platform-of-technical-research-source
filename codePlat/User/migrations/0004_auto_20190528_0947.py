# Generated by Django 2.0.5 on 2019-05-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20190527_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normaluser',
            name='point',
        ),
        migrations.AlterField(
            model_name='expertuser',
            name='field',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
