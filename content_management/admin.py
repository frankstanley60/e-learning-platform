#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, UserRole, UserRolesMapping, Lesson, Quiz, Resource, Tag, ContentTag, UserInteraction, UserProgress, Content 

admin.site.register(Author)
admin.site.register(UserRole)
admin.site.register(UserRolesMapping)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Resource)
admin.site.register(Tag)
admin.site.register(ContentTag)
admin.site.register(UserInteraction)
admin.site.register(UserProgress)
admin.site.register(Content)



