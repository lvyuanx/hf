# Generated by Django 4.1.7 on 2023-05-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_rename_record_stepsort_change_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='stepbase',
            name='is_skip',
            field=models.BooleanField(default=False, verbose_name='是否跳过'),
        ),
    ]
