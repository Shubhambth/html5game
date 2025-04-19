from django.shortcuts import render
from .models import Game , Category ,Post


def home(request):
    games = Game.objects.all()
    popular_games = Game.objects.order_by('-views_count')[:6]
    posts = Post.objects.all()
    return render(request, 'home.html',{'games': games,'popular_games': popular_games,'posts': posts})



def detailpage1(request,id):
    allgames = Game.objects.all()
    game = Game.objects.get(id=id)
    popular_games = Game.objects.order_by('-views_count')[:6]
    posts = Post.objects.all()
    return render(request, 'detailpage1.html',{'game': game,'allgames':allgames,'popular_games': popular_games,'posts': posts})

def detailpage2(request,id):
    allgames = Game.objects.all()
    game = Game.objects.get(id=id)
    game.views_count += 1
    game.save()
    popular_games = Game.objects.order_by('-views_count')[:5]
    posts = Post.objects.all()
    return render(request, 'detailpage2.html',{'game': game,'allgames':allgames,'popular_games': popular_games,'posts': posts})

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html',{'blogs': posts})


def allgames(request):
    game = Game.objects.all()
    return render(request, "html5allgames.html",{'game':game})



def gamerivew(request):
    game = Game.objects.all()
    return render(request, 'gamerivew.html',{'game':game})

def about(request):
    return render(request, 'about.html')

def blogdetail(request, slug):
    post = Post.objects.get(slug=slug)
    allgames = Game.objects.all()
    popular_games = Game.objects.order_by('-views_count')[:3]
    post.increase_views()
    return render(request, 'blogdetail.html', {'post': post,'allgames':allgames,'popular_games': popular_games})



