from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    # additional fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    bio = models.TextField()

    #test_identifier = models.CharField(max_length=40, unique=False)
    #groups
    #total balances owed
    #phone number

    def __str__(self):
        return self.username
    
    #image resizing
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    



