from django.contrib import admin

from . import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'status',
        'created',
        'updated',
    )
    search_fields = (
        'title',
        'author__username',   
        )
    list_filter = (
        'status',
        )

    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'created',
        'updated',
        )
    def __str__(self):
        return self.post

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)
