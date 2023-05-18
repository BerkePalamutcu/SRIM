from django.shortcuts import render
from .models import Conference
# Create your views here.


def home(request):
    conferences = Conference.objects.all()
    context = {'conferences': conferences}
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html')
