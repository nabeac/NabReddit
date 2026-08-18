from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', '__str__', 'updated')
    search_fields = ('title',)
    list_filter = ('created', 'updated')

