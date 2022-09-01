from django.contrib import admin
from .models import Post

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ('title','auther','status')
    ordering = ('date_create',)
