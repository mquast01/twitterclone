from django.contrib import admin

from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("user_id", "created", "body", "picture")

#register flight with flightadmin settings
admin.site.register(Post)