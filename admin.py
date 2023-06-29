from django.contrib import admin



from .models import Category, Post, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']

    admin.site.register(Comment, CommentAdmin)
