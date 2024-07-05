# Generated by Django 5.0.4 on 2024-07-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_location_job_requirements_job_salary_job_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='status',
        ),
        migrations.RemoveField(
            model_name='job',
            name='views_count',
        ),
        migrations.AlterField(
            model_name='job',
            name='requirements',
            field=models.TextField(default='Not specified'),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(default='Not specified', max_length=100),
        ),
    ]
