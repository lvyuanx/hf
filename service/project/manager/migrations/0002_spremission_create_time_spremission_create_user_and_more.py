# Generated by Django 4.1.7 on 2024-02-27 05:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spremission',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spremission',
            name='create_user',
            field=models.BigIntegerField(null=True, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='spremission',
            name='delete_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='删除时间'),
        ),
        migrations.AddField(
            model_name='spremission',
            name='delete_user',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='删除人'),
        ),
        migrations.AddField(
            model_name='spremission',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='spremission',
            name='is_enable',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
        migrations.AddField(
            model_name='spremission',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='spremission',
            name='update_user',
            field=models.BigIntegerField(null=True, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='srole',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='srole',
            name='create_user',
            field=models.BigIntegerField(null=True, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='srole',
            name='delete_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='删除时间'),
        ),
        migrations.AddField(
            model_name='srole',
            name='delete_user',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='删除人'),
        ),
        migrations.AddField(
            model_name='srole',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='srole',
            name='is_enable',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
        migrations.AddField(
            model_name='srole',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='srole',
            name='update_user',
            field=models.BigIntegerField(null=True, verbose_name='更新人'),
        ),
    ]