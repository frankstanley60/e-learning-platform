# Generated by Django 5.0.4 on 2024-05-17 15:12

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0017_remove_studentresponse_completed_exercise_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='completed',
        ),
        migrations.CreateModel(
            name='StudentExerciseCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('completion_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interaction.exercise')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interaction.student')),
            ],
        ),
    ]
