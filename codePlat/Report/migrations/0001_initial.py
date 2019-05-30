# Generated by Django 2.0.5 on 2019-05-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('TechResource', '0001_initial'),
        ('UserComment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_context', models.CharField(default='Nothing has been written here', max_length=6000)),
                ('report_time', models.DateTimeField(auto_now_add=True)),
                ('report_error', models.CharField(choices=[('title', '标题错误'), ('author', '作者错误'), ('keyword', '关键词错误'), ('year', '发表年份错误'), ('abstract', '摘要错误'), ('author', '作者错误'), ('sciAchiUrl', '论文文件错误')], default='标题错误', max_length=32)),
                ('report_status', models.IntegerField(default=1)),
                ('report_resource_id', models.ForeignKey(on_delete=True, to='TechResource.SciAchi')),
                ('report_user', models.ForeignKey(on_delete=True, to='User.NormalUser')),
            ],
            options={
                'verbose_name': '举报成果信息',
                'verbose_name_plural': '举报成果信息',
            },
        ),
        migrations.CreateModel(
            name='report_comment',
            fields=[
                ('reportcomment_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_context', models.CharField(default='Nothing has been written here', max_length=6000)),
                ('report_time', models.DateTimeField(auto_now_add=True)),
                ('report_status', models.IntegerField(default=1)),
                ('report_comment_id', models.ForeignKey(on_delete=True, to='UserComment.Comment')),
                ('report_user', models.ForeignKey(on_delete=True, to='User.NormalUser')),
            ],
            options={
                'verbose_name': '举报评论',
                'verbose_name_plural': '举报评论',
            },
        ),
        migrations.CreateModel(
            name='report_expert',
            fields=[
                ('reportexpert_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_context', models.CharField(default='Nothing has been written here', max_length=6000)),
                ('report_time', models.DateTimeField(auto_now_add=True)),
                ('report_error', models.CharField(choices=[('name', '姓名错误'), ('institution', '所在机构错误'), ('paper_number', '论文发表数量错误'), ('H_index', 'H指数'), ('G_index', 'G指数'), ('field', '领域错误')], default='标题错误', max_length=32)),
                ('report_status', models.IntegerField(default=1)),
                ('report_expert_id', models.ForeignKey(on_delete=True, to='User.ExpertUser')),
                ('report_user', models.ForeignKey(on_delete=True, to='User.NormalUser')),
            ],
            options={
                'verbose_name': '举报专家信息',
                'verbose_name_plural': '举报专家信息',
            },
        ),
    ]
