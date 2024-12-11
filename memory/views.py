from django.shortcuts import render
from django.http import HttpResponse

from . import forms
from . import models

# Create your views here.
def createUser(request):
    return HttpResponse('user created')


def addMemoryView(request):
    if request.method == 'POST':
        """dayForm = request.POST.dayForm
        eventForm = request.POST.eventForm
        photoForm = request.POST.photoForm"""
        enteredDate = request.POST.get('date')
        enteredTitle = request.POST.get('title')
        enteredEventTitle = request.POST.get('eventTitle')
        enteredEventDescription = request.POST.get('eventDescription')
        enteredPhoto = request.POST.get('photo')

        userData = models.User(userProfilePicture="", userName="macharia", userEmail="macharia@gmail.com", userPassword="@Macharia1")
        dayData = models.Day(userID=userData.userID, date=enteredDate, title=enteredTitle)
        eventData = models.Event(date=dayData, eventTitle=enteredEventTitle, eventDescription=enteredEventDescription)
        photoData = models.Photo(eventID=eventData.eventID,photo=enteredPhoto)

        return HttpResponse(f"""adding memory ...\n{enteredDate}
        \n{enteredTitle}\n{enteredEventTitle}\n{enteredEventDescription}\n{enteredPhoto}""")
    
    else:
        dayForm = forms.DayForm()
        eventForm = forms.EventForm()
        photoForm = forms.PhotoForm()

        return render(request, 'memory/addMemory.html', {'day' : dayForm,
        'event' : eventForm,
        'photo' : photoForm})
    

def reviewMemoryView(request):
    data = models.Event.objects.all()
    return render(request, "memory/review.html", {"memories" : data})