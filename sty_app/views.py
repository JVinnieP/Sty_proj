from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def services(request):
    return render(request, 'services.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def email(request):
    return render(request, 'email.html', {})

def foot(request):
    return render(request, 'foot.html', {})

