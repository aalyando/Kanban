# Generated by Django 5.0.1 on 2024-01-24 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('In QA', 'In QA'), ('Ready', 'Ready'), ('Done', 'Done')], default='New'),
        ),
    ]
