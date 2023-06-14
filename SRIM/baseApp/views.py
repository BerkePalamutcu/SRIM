from collections import defaultdict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Conference, Bulletin, Person, News, Archive, SliderContent, BlogPost, WorkGroup, Members, AnteriorRomedInf, EchipaTitles
from datetime import datetime
from django.shortcuts import render, get_object_or_404


def home(request):
    conferences = Conference.objects.all()
    slider_content = SliderContent.objects.all()
    blog_posts = BlogPost.objects.order_by('-created_at').all()[:4]
    # This block is used to get the latest bulletin for the home page.
    try:
        latest_bulletin = Bulletin.objects.latest('created')
    except Bulletin.DoesNotExist:
        latest_bulletin = None

    context = {'conferences': conferences,
               'latest_bulletin': latest_bulletin, 'slider_content': slider_content, 'blog_posts': blog_posts, 'dynamic_navbar':  'navbar-dynamic'}

    if request.method == 'POST':
        start_date_str = request.POST.get('start_date', None)
        end_date_str = request.POST.get('end_date', None)

        if start_date_str and end_date_str:
            # Convert the date strings to datetime objects
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            # Query for conferences within the date range
            conferences = Conference.objects.filter(
                dateStart__gte=start_date, dateEnd__lte=end_date)

            redirect_url = reverse(
                'conferences') + f'?start_date={start_date_str}&end_date={end_date_str}'
            return redirect(redirect_url)

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
    blog_posts = Archive.objects.order_by('created').all()
    paginator = Paginator(blog_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'archives': page_obj}
    return render(request, 'archives.html', context)


def archive(request, pk):
    archive = get_object_or_404(Archive, pk=pk)
    return render(request, 'archive.html', {'archive': archive})


def about(request):
    return render(request, 'about.html')


def board(request):
    echipa_titles = EchipaTitles.objects.all()
    grouped_titles = defaultdict(list)

    for member in echipa_titles:
        grouped_titles[member.title].append(member)

    return render(request, 'board.html', {'grouped_titles': dict(grouped_titles)})


def membership(request):
    return render(request, 'membership.html')


def conferences(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    conferences = Conference.objects.filter(
        dateStart__gte=start_date, dateEnd__lte=end_date)

    context = {'conferences': list(conferences)}

    print(context, 'context')
    return render(request, 'conferences.html', context)


def previous(request):
    previous_listing = AnteriorRomedInf.objects.all()

    context = {'previous_listing': previous_listing}
    return render(request, 'romedinf.html', context)


def blog_list(request):
    blog_posts = BlogPost.objects.order_by('-created_at').all()
    paginator = Paginator(blog_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'blog_posts': page_obj})


def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})


def grupuri_lucru(request):
    return render(request, 'lucru.html')


def hector(request):
    members = Members.objects.all()
    if 'hector' in request.path:
        workgroup = WorkGroup.objects.filter(name__contains='HECTOR').first()
        context = {'workgroup': workgroup, 'members': members}
    return render(request, 'hector.html', context)


def madman(request):
    members = Members.objects.all()
    if 'madman' in request.path:
        workgroup = WorkGroup.objects.filter(name__contains='MADMAN').first()
        context = {'workgroup': workgroup, 'members': members}
    return render(request, 'madman.html', context)


def nurser(request):
    members = Members.objects.all()
    if 'nurser' in request.path:
        workgroup = WorkGroup.objects.filter(name__contains='NURSER').first()
        context = {'workgroup': workgroup, 'members': members}
    return render(request, 'nurser.html', context)


def hearth(request):
    members = Members.objects.all()
    if 'hearth' in request.path:
        workgroup = WorkGroup.objects.filter(name__contains='hearth').first()
        context = {'workgroup': workgroup, 'members': members}
    return render(request, 'hearth.html', context)


def tender(request):
    members = Members.objects.all()
    if 'tender' in request.path:
        workgroup = WorkGroup.objects.filter(name__contains='tender').first()
        context = {'workgroup': workgroup, 'members': members}
    return render(request, 'tender.html', context)
