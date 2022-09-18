from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, blank=False, null=False)
    isVendor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.user} {self.phone_number}'
