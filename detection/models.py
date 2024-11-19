from django.db import models
from django.contrib.auth.models import AbstractUser

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
