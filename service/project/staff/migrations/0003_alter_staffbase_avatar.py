# Generated by Django 4.1.7 on 2023-05-30 14:18

from django.db import migrations, models
import staff.models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_staffbase_staff_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffbase',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=staff.models.staff, verbose_name='头像'),
        ),
    ]
