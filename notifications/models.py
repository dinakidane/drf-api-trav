from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import Profile

class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(User, related_name='notifications_from', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    target_profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.actor} {self.verb} {self.target}'
