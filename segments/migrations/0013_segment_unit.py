# Generated by Django 5.1 on 2024-08-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0012_segment_achieved_sample_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='unit',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
