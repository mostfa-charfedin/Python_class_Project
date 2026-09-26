from django.db import models
from django.contrib.auth.models import User



class Person (models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

    cin =models.CharField(
        max_length=20,
        unique=True
    )

    email=models.EmailField(
        unique=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.cin}"
