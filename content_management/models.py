from django.db import models
from django.contrib.auth.models import User

DIFFICULTY_CHOICES = [
    (1, 'Easy'),
    (2, 'Medium'),
    (3, 'Hard'),
]

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    social_links = models.URLField()
    profile_picture = models.ImageField(upload_to='author_profile_pics/')

    def __str__(self):
        return self.user.username

class UserRole(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name

class UserRolesMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(default='')
    math_content = models.TextField(blank=True, null=True)  # Mathematical content
    difficulty_level = models.IntegerField(choices=DIFFICULTY_CHOICES, default='1')  # Add choices for difficulty levels
    order_index = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(default='')  # Regular content (text, HTML, etc.)
    math_content = models.TextField(blank=True, null=True)  # Mathematical content
    difficulty_level = models.IntegerField(choices=DIFFICULTY_CHOICES, default='2')  # Add choices for difficulty levels
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(default='')  # Regular content (text, HTML, etc.)
    math_content = models.TextField(blank=True, null=True)  # Mathematical content
    difficulty_level = models.IntegerField(choices=DIFFICULTY_CHOICES, default='1')  # Add choices for difficulty levels
    submission_instructions = models.TextField()
    due_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Resource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(blank=True)
    file = models.FileField(upload_to='resources/', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name

class ContentTag(models.Model):
    content = models.ForeignKey('Content', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)
    interaction_date = models.DateTimeField(auto_now_add=True)

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_content_management'), 
    content = models.ForeignKey('Content', on_delete=models.CASCADE)
    progress_percentage = models.FloatField()
    last_interaction_date = models.DateTimeField(auto_now=True)

# Define the Content model which is referenced in ContentTag, UserInteraction, and UserProgress
class Content(models.Model):
    pass  # Define the fields for Content model as per your requirements

