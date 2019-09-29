from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # import user model
    # when delete user, posts also will delete
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # magic method, return object title in query set instead of id
    def __str__(self):
        return self.title
