import pandas as pd
import uuid
import re
from django.core.management.base import BaseCommand
from user_interaction.models import Exercise, ExerciseParameters, Content  # Update 'your_app' to the actual app name

class Command(BaseCommand):
    help = 'Load exercise data from my_items.csv'

    def handle(self, *args, **kwargs):
        # Load the CSV file
        my_items = pd.read_csv('C:\\Users\\frank\\Documents\\FYP_Item_parameters\\my_items.csv')

        # Print the column names to verify
        print("Column names:", my_items.columns)

        # Define a function to clean UUID strings
        def clean_uuid(uuid_str):
            # Remove any non-alphanumeric characters
            cleaned_uuid = re.sub(r'[^a-zA-Z0-9-]', '', uuid_str)
            return cleaned_uuid

        # Define a function to map difficulty strings to numeric values
        def map_difficulty(difficulty_value):
            if isinstance(difficulty_value, str):
                difficulty_map = {
                    'easy': 1.0,
                    'normal': 2.0,
                    'hard': 3.0,
                    'unset': 0.0
                }
                return difficulty_map.get(difficulty_value.lower(), 0.0)
            elif isinstance(difficulty_value, (int, float)):
                return float(difficulty_value)
            else:
                return 0.0

        # Iterate over the rows of my_items DataFrame
        for index, row in my_items.iterrows():
            try:
                # Clean the UUID string
                cleaned_upid = clean_uuid(row['upid'])
                # Attempt to convert the cleaned value to UUID format
                upid = uuid.UUID(cleaned_upid)
            except ValueError:
                # If it's not a valid UUID, generate a new one
                upid = uuid.uuid4()
                # Update the DataFrame with the new UUID
                my_items.at[index, 'upid'] = str(upid)

            # Map the difficulty field to numeric value
            my_items.at[index, 'difficulty'] = map_difficulty(row['difficulty'])

        # Save the modified DataFrame back to the CSV file
        my_items.to_csv('C:\\Users\\frank\\Documents\\FYP_Item_parameters\\my_items.csv', index=False)

        # Iterate over the modified DataFrame to create or update Exercise and ExerciseParameters objects
        for index, row in my_items.iterrows():
            try:
                # Check if the content_id exists in the Content model
                try:
                    content = Content.objects.get(pk=row['content_id'])
                except Content.DoesNotExist:
                    print(f"Content with ID {row['content_id']} does not exist. Skipping row {index}.")
                    continue

                exercise, created = Exercise.objects.get_or_create(
                    ucid=row['ucid'],
                    defaults={
                        'content_pretty_name': row['content_pretty_name'],
                        'content_kind': row['content_kind'],
                        'difficulty': row['difficulty'],
                        'discrimination': row['discrimination'],
                        'guessing': row['guessing'],
                        'subject': row['subject'],
                       # 'content': content,
                        'learning_stage': row['learning_stage'],
                        'level1_id': row['level1_id'],
                        'level2_id': row['level2_id'],
                        'level3_id': row['level3_id'],
                        'level4_id': row['level4_id']
                    }
                )

                if not created:
                    # Update existing record if it was not created
                    exercise.content_pretty_name = row['content_pretty_name']
                    exercise.content_kind = row['content_kind']
                    exercise.difficulty = row['a']
                    exercise.discrimination = row['b']
                    exercise.guessing = row['c']
                    exercise.subject = row['subject']
                   # exercise.content = content
                    exercise.learning_stage = row['learning_stage']
                    exercise.level1_id = row['level1_id']
                    exercise.level2_id = row['level2_id']
                    exercise.level3_id = row['level3_id']
                    exercise.level4_id = row['level4_id']
                    exercise.save()

                # Create or update ExerciseParameters
                ExerciseParameters.objects.update_or_create(
                    exercise=exercise,
                    defaults={
                        'difficulty': row['difficulty'],
                        'discrimination': row['discrimination'],
                        'guessing': row['guessing']
                    }
                )

            except KeyError as e:
                print(f"Missing column {e} in row {index}. Skipping row.")
            except Exception as e:
                print(f"Error processing row {row['ucid']}: {e}")
