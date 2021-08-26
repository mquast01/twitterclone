from django.contrib import admin

from .models import UserFollowing, Profile
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("user_id", "created", "body", "picture")

class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ("user_id", "following_user_id", "created")

#register flight with flightadmin settings
admin.site.register(UserFollowing)
admin.site.register(Profile)

