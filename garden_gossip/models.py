from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ForumPost(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    user = models.ForeignKey(User, related_name='forum_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
