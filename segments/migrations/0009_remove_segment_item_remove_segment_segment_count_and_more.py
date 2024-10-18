# Generated by Django 5.1 on 2024-08-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0008_segment_item_segment_value_delete_segmentitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segment',
            name='item',
        ),
        migrations.RemoveField(
            model_name='segment',
            name='segment_count',
        ),
        migrations.RemoveField(
            model_name='segment',
            name='value',
        ),
        migrations.AddField(
            model_name='segment',
            name='actual_final_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='analysis_group_head',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='segment',
            name='completed_month',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='contact_person_in_analysis',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='contact_person_in_research',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='data_correction_done',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='expected_date_of_output',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='research_group_head',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='segment',
            name='status',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='segment',
            name='segment_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
