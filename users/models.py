from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserFollowing(models.Model):
    user_id = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

    # You can even add info about when user started following
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        #unique_together = ['user_id', 'following_user_id']
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'following_user_id'], name='unique_follow')
        ]

    def __str__(self):
        return f'{self.user_id} following {self.following_user_id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures', default='default.jpg')
    birthday = models.DateField()
    nickname = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.username}'