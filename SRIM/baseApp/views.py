from django.shortcuts import render
from .models import Conference, Bulletin, Person


def home(request):
    conferences = Conference.objects.all()

    try:
        latest_bulletin = Bulletin.objects.latest('created')
    except Bulletin.DoesNotExist:
        latest_bulletin = None

    context = {'conferences': conferences, 'latest_bulletin': latest_bulletin}
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html')


def organizers(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'organizers.html', context)
