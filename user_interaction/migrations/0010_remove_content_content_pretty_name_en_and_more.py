# Generated by Django 5.0.4 on 2024-07-17 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0009_content_content_pretty_name_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='content_pretty_name_en',
        ),
        migrations.RemoveField(
            model_name='content',
            name='content_pretty_name_zh',
        ),
        migrations.RemoveField(
            model_name='content',
            name='subject_en',
        ),
        migrations.RemoveField(
            model_name='content',
            name='subject_zh',
        ),
    ]
