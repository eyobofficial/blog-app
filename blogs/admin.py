from django.contrib import admin

from . import models

admin.site.site_header = 'Blog Admin'
admin.site.site_title = 'Blog Admin'


class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 1

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'updated_at', )
    list_filter = ('publish', 'status', 'author', )
    search_fields = ('title', 'slug', 'body', )
    ordering = ('status', 'updated_at', )
    inlines = [CommentInline, ]
    