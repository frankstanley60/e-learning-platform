from django import forms
from .models import Lesson


class LessonCreateForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'content', 'difficulty_level', 'order_index']  # Include the order_index field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'math-content'  # Add a class for MathJax rendering

class LessonEditForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'content', 'order_index']
