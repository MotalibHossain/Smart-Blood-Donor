from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField
from django.contrib.auth.models import User

# Create your models here.
class BloodRequestPost(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='articale')
    phone=models.CharField(max_length=20)
    bloodgroup=models.CharField(max_length=20)
    neededBlood=models.CharField(max_length=20)
    locations=models.CharField(max_length=50)
    requestDate=models.DateField(max_length=50)
    currentDate=models.DateField(auto_now_add=True, blank=False)

    def __str__(self) -> str:
        return self.author.username
    
    class Meta:
        ordering=['-currentDate']
