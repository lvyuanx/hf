# Generated by Django 4.1.7 on 2023-05-23 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_alter_stepsort_child_step_alter_stepsort_parent_step'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stepsort',
            old_name='child_step',
            new_name='child_step_id',
        ),
        migrations.RenameField(
            model_name='stepsort',
            old_name='parent_step',
            new_name='parent_step_id',
        ),
    ]
