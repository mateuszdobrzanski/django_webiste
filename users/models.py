from django.db import models
from django.contrib.auth.models import User


# one user has one profile and one profile is associated with one user
class Profile(models.Model):
    # create one-to-one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default='default.jpg' -> default image for all users
    # upload_to='dir' -> where will be stored users pic
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
