from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    # additional fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='media/profile_pictures/')
    bio = models.TextField()
    #groups
    balance = models.FloatField(default=5.00)
    dues = models.FloatField(default=1.00)
    #user_name = models.CharField(max_length=100, default)
    # this_user = models.ForeignKey(User, on_delete=models.CASCADE)
    #phone number

    def __str__(self):
        return self.user.username
    

    
    #image resizing
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


