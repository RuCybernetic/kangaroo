from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    coins = models.IntegerField(default=1000)

class Bet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    kangaroo = models.CharField(max_length=20)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)