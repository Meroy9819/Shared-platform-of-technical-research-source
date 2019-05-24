# Generated by Django 2.2.1 on 2019-05-24 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20190523_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likeresources',
            old_name='liker_id',
            new_name='liker_user',
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='type',
            field=models.CharField(choices=[('专家用户', '专家用户'), ('普通用户', '普通用户'), ('管理员', '管理员')], default='普通用户', max_length=32),
        ),
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.NormalUser')),
            ],
            options={
                'verbose_name': '确认码',
                'verbose_name_plural': '确认码',
                'ordering': ['-c_time'],
            },
        ),
    ]