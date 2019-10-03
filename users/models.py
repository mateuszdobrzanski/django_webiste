from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# one user has one profile and one profile is associated with one user
class Profile(models.Model):
    # create one-to-one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default='default.jpg' -> default image for all users
    # upload_to='dir' -> where will be stored users pic
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    # override and resize images over 300px
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)