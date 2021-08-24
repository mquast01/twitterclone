from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>", views.post_view, name="post"),
    path("<int:post_id>/tweet", views.tweet, name="tweet")
]