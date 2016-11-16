from django.contrib import admin

from .models import Post, Like


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at')
    list_filter = ('user',)


admin.site.register(Post, PostAdmin)
admin.site.register(Like)
