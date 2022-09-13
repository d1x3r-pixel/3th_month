from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isVendor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'