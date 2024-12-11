from django.db import models
from userAuth.models import User

# Create your models here.
class Day(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(primary_key=True)
    title = models.CharField(max_length=50)



class Event(models.Model):
    date = models.ForeignKey(Day, on_delete=models.CASCADE)
    eventID = models.AutoField(primary_key=True)
    eventTitle = models.CharField(max_length=50)
    eventDescription = models.TextField()


class Photo(models.Model):
    eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
    photoID = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='static/memory')

