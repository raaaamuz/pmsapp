# Generated by Django 5.0.6 on 2024-09-07 14:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('researcher_in_charge', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('job_number', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=20)),
                ('dp_or_scripting', models.CharField(max_length=20)),
                ('in_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('in_charge1', models.CharField(blank=True, max_length=100, null=True)),
                ('survey_responses', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
