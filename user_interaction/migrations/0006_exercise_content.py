# Generated by Django 5.0.4 on 2024-06-15 04:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0005_alter_content_discrimination'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_interaction.content'),
        ),
    ]
