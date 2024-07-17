# management/commands/translate_exercise_names.py
from django.core.management.base import BaseCommand
from googletrans import Translator
from user_interaction.models import Exercise

class Command(BaseCommand):
    help = 'Translate exercise names and save to database'

    def handle(self, *args, **kwargs):
        translator = Translator()
        exercises = Exercise.objects.all()
        for exercise in exercises:
            if not exercise.translated_content_pretty_name:
                translated_name = translator.translate(exercise.content_pretty_name, dest='en').text
                exercise.translated_content_pretty_name = translated_name
                exercise.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully translated: {exercise.content_pretty_name}'))
