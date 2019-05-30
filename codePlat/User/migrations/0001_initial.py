# Generated by Django 2.0.5 on 2019-05-30 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(default='No yet', max_length=30)),
                ('admin_password', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
                'ordering': ['admin_id'],
            },
        ),
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpertUser',
            fields=[
                ('expert_id', models.AutoField(primary_key=True, serialize=False)),
                ('corresponding_user_id', models.IntegerField(default=0)),
                ('name', models.CharField(default='尚无姓名', max_length=64)),
                ('institution', models.CharField(max_length=128, null=True)),
                ('reference_number', models.IntegerField(null=True)),
                ('paper_number', models.IntegerField(null=True)),
                ('H_index', models.IntegerField(null=True)),
                ('G_index', models.IntegerField(null=True)),
                ('field', models.CharField(max_length=128, null=True)),
                ('like_number', models.IntegerField(default=0)),
                ('visit_number', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '专家',
                'verbose_name_plural': '专家',
                'ordering': ['expert_id'],
            },
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='用户名', max_length=64, unique=True)),
                ('passwd', models.CharField(max_length=1024)),
                ('user_type', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('introduction', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='女', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('phonenumber', models.CharField(default='00000000', max_length=11)),
                ('corresponding_expert_id', models.IntegerField(default=0)),
                ('corrsponding_admin_id', models.IntegerField(default=0)),
                ('has_confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='confirmstring',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.NormalUser'),
        ),
    ]
