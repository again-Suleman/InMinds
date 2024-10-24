from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    date_posted = models.DateField(auto_now=True)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta():
        unique_together = ('title', 'author')
    
    # Dundererererer
    def __str__(self):
        return f'{self.author} post, Title: {self.title}'


