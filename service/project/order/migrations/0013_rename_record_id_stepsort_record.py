# Generated by Django 4.1.7 on 2023-05-23 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_remove_stepsortchangerecord_step_sort_first_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stepsort',
            old_name='record_id',
            new_name='record',
        ),
    ]