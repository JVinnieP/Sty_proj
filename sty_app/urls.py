from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('blog.html', views.blog, name="blog"),
    path('services.html', views.services, name="services"),
    path('contact.html', views.contact, name="contact"),
]