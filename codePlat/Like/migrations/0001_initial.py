# Generated by Django 2.2.1 on 2019-05-27 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TechResource', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeResources',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('like_resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechResource.SciAchi')),
                ('liker_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.NormalUser')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
    ]
