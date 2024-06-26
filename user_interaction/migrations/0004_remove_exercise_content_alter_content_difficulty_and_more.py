# Generated by Django 5.0.4 on 2024-06-14 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0003_alter_exercise_ucid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='content',
        ),
        migrations.AlterField(
            model_name='content',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Unset', 'Unset')], max_length=20),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Unset', 'Unset')], max_length=20),
        ),
    ]
