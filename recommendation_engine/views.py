from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
from math import exp
from user_interaction.models import StudentResponse, ItemParameter  # Import your Django models

def estimate_user_ability(user):
    # Retrieve the user's responses
    user_responses = StudentResponse.objects.filter(student=user)
    
    # Initialize variables for ability estimation
    total_ability = 0
    total_responses = 0
    
    # Iterate over user's responses
    for response in user_responses:
        # Retrieve the item parameters for the current exercise
        try:
            item_parameters = ItemParameter.objects.get(upid=response.upid)
        except ItemParameter.DoesNotExist:
            # Skip if item parameters not found
            continue
        
        # Calculate the probability of a correct response using the 3PL model
        probability_correct = item_parameters.discrimination * (user.user_grade * item_parameters.difficulty - item_parameters.guessing) / (1 - item_parameters.guessing)
        probability_correct = 1 / (1 + exp(-probability_correct))
        
        # Update total ability
        total_ability += probability_correct
        total_responses += 1
    
    # Calculate average ability
    if total_responses > 0:
        average_ability = total_ability / total_responses
    else:
        average_ability = 0  # Default if no responses
    
    return average_ability

# Example usage:
# user = User.objects.get(pk=1)  # Assuming user is retrieved somehow
# user_ability = estimate_user_ability(user)
from myapp.models import Exercise, ItemParameter  # Import your Django models

def recommend_content(user, num_recommendations=5):
    # Retrieve all available exercises
    all_exercises = Exercise.objects.all()
    
    # Calculate difficulty of each exercise and rank them
    ranked_exercises = []
    for exercise in all_exercises:
        # Retrieve the item parameters for the exercise
        try:
            item_parameters = ItemParameter.objects.get(ucid=exercise.ucid)
        except ItemParameter.DoesNotExist:
            # Skip if item parameters not found
            continue
        
        # Calculate the difficulty of the exercise
        exercise_difficulty = user.user_grade * item_parameters.difficulty
        
        # Append exercise and difficulty to the ranked list
        ranked_exercises.append((exercise, exercise_difficulty))
    
    # Sort exercises by difficulty
    ranked_exercises.sort(key=lambda x: x[1])
    
    # Select top exercises to recommend
    top_recommendations = ranked_exercises[:num_recommendations]
    
    # Extract exercise objects from recommendations
    recommended_exercises = [exercise for exercise, _ in top_recommendations]
    
    return recommended_exercises

# Example usage:
# user = User.objects.get(pk=1)  # Assuming user is retrieved somehow
# recommended_exercises = recommend_content(user)
=======
>>>>>>> ea19d24fb0863fb2f3a38818a1609df716b7aaa9
