# Generated by Django 5.0.4 on 2024-07-16 13:38

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0024_alter_studentresponse_choice_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseParameters',
            fields=[
                ('exercise', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user_interaction.exercise')),
                ('difficulty', models.FloatField()),
                ('discrimination', models.FloatField()),
                ('guessing', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='studentresponse',
            old_name='exercise_problem_re',
            new_name='exercise_problem_repeat_session',
        ),
        migrations.AddField(
            model_name='content',
            name='discrimination',
            field=models.FloatField(default=0.2),
        ),
        migrations.AddField(
            model_name='content',
            name='guessing',
            field=models.FloatField(default=0.1),
        ),
        migrations.AddField(
            model_name='exercise',
            name='discrimination',
            field=models.FloatField(default=0.1),
        ),
        migrations.AddField(
            model_name='exercise',
            name='guessing',
            field=models.FloatField(default=0.1),
        ),
        migrations.AddField(
            model_name='student',
            name='ability',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_interaction.content'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='ucid',
            field=models.CharField(default=1, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interaction.choice'),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_responses', to='user_interaction.exercise'),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_interaction.question'),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='total_attempt_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='total_sec_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='ucid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_interaction.content'),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='upid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='studentresponse',
            name='used_hint_cnt',
            field=models.IntegerField(default=0),
        ),
    ]