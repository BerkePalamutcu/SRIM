from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('organizers/', views.organizers, name='organizers'),
    path('news/', views.news, name='news'),
    path('archives/', views.archives, name='archives'),
    path('about/', views.about, name='about'),
    path('board/', views.board, name='board'),
    path('membership/', views.membership, name='membership'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
