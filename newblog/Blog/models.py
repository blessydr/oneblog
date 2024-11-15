from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    
class Blog_Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags=models.ManyToManyField(Tag, related_name='blogs', blank=True)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    
class Comments(models.Model):
    blog=models.ForeignKey(Blog_Post,related_name='comments',on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog.title}"
    
    class Meta:
        ordering = ['created_at']