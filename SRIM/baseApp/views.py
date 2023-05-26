from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Conference, Bulletin, Person, News, Archive


def home(request):
    conferences = Conference.objects.all()
    # This block is used to get the latest bulletin for the home page.
    try:
        latest_bulletin = Bulletin.objects.latest('created')
    except Bulletin.DoesNotExist:
        latest_bulletin = None

    context = {'conferences': conferences, 'latest_bulletin': latest_bulletin}
    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # send email
        send_mail(
            f'Message from {name}',
            message,
            email,
            ['romedinf.secretariat@gmail.com'],
        )

        return HttpResponse('Thank you for your message.')

    return render(request, 'contact.html')


def organizers(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'organizers.html', context)


def news(request):
    context = {'news': News.objects.all()}
    return render(request, 'news.html', context)


def archives(request):
    context = {'archives': Archive.objects.all()}
    return render(request, 'archives.html', context)


def about(request):
    return render(request, 'about.html')


def board(request):
    return render(request, 'board.html')


def membership(request):
    return render(request, 'membership.html')
