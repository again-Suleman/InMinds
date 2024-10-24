from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    
    
    def __str__(self):
        return f'Profile of {self.user.username}'
    
    def save(self):
        super().save()
        print(f'{self.image.path}')
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  #! Cuz it accept a tuple :)
            img.save(self.image.path)
