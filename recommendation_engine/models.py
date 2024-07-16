from django.db import models
from user_interaction.models import Student

class Recommendation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    recommended_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    proficiency_estimation = models.FloatField()
