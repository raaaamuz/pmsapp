# Generated by Django 5.1 on 2024-08-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0010_segment_check_list_followed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segment',
            name='analysis_group_head',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
