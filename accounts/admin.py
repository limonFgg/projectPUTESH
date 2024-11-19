from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Profile, Comment, Like

admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
