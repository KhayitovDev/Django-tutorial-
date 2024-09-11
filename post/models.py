from django.db import models
from django.contrib.auth.models import User


    
class Post(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255, blank=False, null=False)
    content=models.TextField(blank=False, null=False)
    is_published=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Post by {self.user.username}"
    

    