from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateField

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.CharField(max_length=150)
    phone=models.CharField(max_length=20)
    DateOfBirth=DateField(max_length=50)
    profession=CharField(max_length=50)
    bloodGroup=CharField(max_length=20)
    gender=CharField(max_length=20)
    city=CharField(max_length=30)
    thana=CharField(max_length=30)
    union=CharField(max_length=30)
    postCode=CharField(max_length=20)
    otp=models.CharField(max_length=30)


    def __str__(self) -> str:
        return self.user.username
