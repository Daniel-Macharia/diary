from django.db import models

# Create your models here.

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userProfilePicture = models.ImageField(upload_to='userAuth/static/profilePhoto/')
    userName = models.CharField(max_length=20)
    userEmail = models.EmailField()
    userPassword = models.CharField(max_length=30)

