from django.contrib import admin

from post.models import Post, PostImage

@admin.register
class PostImageInline(admin.TabularInline):
    pass

@admin.register
class PostImageAdmin(admin.ModelAdmin):
    pass