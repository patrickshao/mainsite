from django.contrib import admin
from aspc.blog.models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "author", "posted")

admin.site.register(Post, PostAdmin)
