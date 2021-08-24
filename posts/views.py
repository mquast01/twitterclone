from django.shortcuts import render

from .models import Post

# Create your views here.

def index(request):
    return render(request, "posts/index.html", {
        "posts": Post.objects.all()
    })

def post_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "posts/post.html", {
        "post": post,
    })

def tweet(request, post_id):
    pass
