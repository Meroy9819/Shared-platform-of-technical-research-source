# Generated by Django 2.0.5 on 2019-05-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normaluser',
            name='corresponding_expert_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='corrsponding_admin_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='passwd',
            field=models.CharField(max_length=1024),
        ),
    ]