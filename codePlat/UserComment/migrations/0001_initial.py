# Generated by Django 2.2.1 on 2019-05-27 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0003_auto_20190527_1111'),
        ('TechResource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('Comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('CommentTime', models.DateTimeField(auto_now_add=True)),
                ('CommentTitle', models.CharField(default='No yet', max_length=100)),
                ('CommentContent', models.CharField(max_length=5000, null=True)),
                ('CommentResourceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechResource.SciAchi')),
                ('CommentUSerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.NormalUser')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
