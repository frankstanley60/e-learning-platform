# Generated by Django 5.0.4 on 2024-05-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0016_studentresponse_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentresponse',
            name='completed',
        ),
        migrations.AddField(
            model_name='exercise',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
