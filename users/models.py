from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  is_director = models.BooleanField(default=False)
  is_productor = models.BooleanField(default=True)
