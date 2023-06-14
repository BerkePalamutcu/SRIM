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
    path('archive/<int:pk>/', views.archive, name='archive'),
    path('about/', views.about, name='about'),
    path('board/', views.board, name='board'),
    path('membership/', views.membership, name='membership'),
    path('conferences/', views.conferences, name='conferences'),
    path('romedinf/', views.previous, name='romedinf'),
    path('blog/', views.blog_list, name='blog-list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('grupuri-lucru/', views.grupuri_lucru, name='grupuri-lucru'),
    path('grupuri-lucru/hector', views.hector, name='hector'),
    path('grupuri-lucru/madman', views.madman, name='madman'),
    path('grupuri-lucru/nurser', views.nurser, name='nurser'),
    path('grupuri-lucru/hearth', views.hearth, name='hearth'),
    path('grupuri-lucru/tender', views.tender, name='tender'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
