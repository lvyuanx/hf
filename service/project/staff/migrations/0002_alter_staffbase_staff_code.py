# Generated by Django 4.1.7 on 2023-05-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffbase',
            name='staff_code',
            field=models.CharField(max_length=100, unique=True, verbose_name='员工编号'),
        ),
    ]
