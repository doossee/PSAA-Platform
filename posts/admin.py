from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["title", "description", "content", "creator", "publish_date", "is_published"]

admin.site.register(Post, PostAdmin)