# Generated by Django 2.2.1 on 2019-05-24 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_normaluser_has_confirmed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likeresources',
            options={'verbose_name': '收藏', 'verbose_name_plural': '收藏'},
        ),
    ]
