# Generated by Django 4.1.7 on 2023-05-06 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_orderdetail_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='number',
            new_name='order_number',
        ),
    ]