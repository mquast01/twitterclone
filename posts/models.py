from django.db import models
from django.db.models import TextField

from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user_id = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    body = TextField()
    picture = models.ImageField(upload_to='profile_pictures', default='default.jpg')

    # You can even add info about when user started following

    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    
    
