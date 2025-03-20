from django.forms import ModelForm
from . import models


class DayForm(ModelForm):
    class Meta:
        model = models.Day
        fields = ['date', 'title']

    


class EventForm(ModelForm):
    class Meta:
        model = models.Event
        fields = ['eventTitle', 'eventDescription']

    


# class PhotoForm(ModelForm):
#     class Meta:
#         model = models.Photo
#         fields = ['photo']

    


