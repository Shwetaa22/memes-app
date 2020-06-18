from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_accpted = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_profile'  # define your custom name

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
        return self
