from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fish(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    fish_id = models.IntegerField()
    fish_size = models.IntegerField()
    fish_price = models.IntegerField()
    status = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True)
    modifiedDate = models.DateTimeField(auto_now=True)