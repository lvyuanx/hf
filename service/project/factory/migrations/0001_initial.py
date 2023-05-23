# Generated by Django 4.1.7 on 2023-04-29 09:11

from django.db import migrations, models
import factory.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_image', models.ImageField(null=True, upload_to=factory.utils.get_upload_path, verbose_name='模具图片')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('goods_shelf', models.CharField(max_length=32, null=True, verbose_name='货架')),
                ('row', models.CharField(max_length=32, null=True, verbose_name='行')),
                ('col', models.CharField(max_length=32, null=True, verbose_name='列')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '模具',
                'verbose_name_plural': '模具列表',
                'db_table': 's_factory_model_base',
            },
        ),
    ]