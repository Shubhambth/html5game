from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def allgames(request):
    return render(request, "html5allgames.html")

def page(request):
    return render(request, 'page.html')

def gamerivew(request):
    return render(request, 'gamerivew.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def final(request):
    return render(request, 'final.html')