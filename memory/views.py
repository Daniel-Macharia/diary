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
        enteredPhoto = request.FILES.get('photo')

        userData = models.User.objects.filter(userID=10).values()#(userProfilePicture=enteredPhoto, userName="macharia", userEmail="macharia@gmail.com", userPassword="@Macharia1")
        user = models.User(userID=userData[0]['userID'], userProfilePicture=userData[0]['userProfilePicture'], userName=userData[0]['userName'], userEmail=userData[0]['userEmail'], userPassword=userData[0]['userPassword'])
        print(userData)
        dayData = models.Day(userID=user, date=enteredDate, title=enteredTitle)
        eventData = models.Event(date=dayData, eventTitle=enteredEventTitle, eventDescription=enteredEventDescription)
        photoData = models.Photo(eventID=eventData,photo=enteredPhoto)

        #day = models.Day(userID=userData.userID, date=enteredDate, title=enteredTitle)
        #event = models.Event(date=day.date, eventTitle=enteredEventTitle,  eventDescription=enteredEventDescription)
        #photo = models.Photo(eventID=event.eventID, photo=enteredPhoto)

        #user.save()
        dayData.save()
        eventData.save()
        photoData.save()
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
    events = models.Event.objects.all().values()

    data = []
    for event in events:
        photos = models.Photo.objects.filter(eventID=event['eventID']).values().order_by('eventID')[0]
        data.append({'event' : event, 'photos' : photos})
    
    for datum in data:
        print(f"Image url: {datum}")

    print(f"\n\n{data}\n\n")
    return render(request, "memory/review.html", {"memories" : data})