from django.db.models.signals import post_save
# signal sender
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# post_save send the signal when user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
