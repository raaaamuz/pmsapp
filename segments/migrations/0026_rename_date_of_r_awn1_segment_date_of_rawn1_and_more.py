# Generated by Django 5.1 on 2024-09-06 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0025_alter_segment_date_of_r_awn1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segment',
            old_name='date_of_r_awn1',
            new_name='date_of_rawn1',
        ),
        migrations.RenameField(
            model_name='segment',
            old_name='date_of_r_awn2',
            new_name='date_of_rawn2',
        ),
        migrations.RenameField(
            model_name='segment',
            old_name='date_of_r_awn3',
            new_name='date_of_rawn3',
        ),
    ]
