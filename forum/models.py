from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, related_name='forum_posts')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on', 'author']
    
    def __str__(self):
        return f"Post: {self.title} || by {self.author.username}"
    
class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
                             related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on', 'author']

    def __str__(self):
        return f"Reply by {self.author.username} on {self.post.title}"
    