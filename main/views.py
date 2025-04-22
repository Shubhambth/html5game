from django.shortcuts import render
from .models import Game , Category ,Post , AdsCode
from django.http import HttpResponse
import os


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
    ads_code = AdsCode.objects.first()
    return render(request, 'detailpage1.html',{'game': game,'allgames':allgames,'popular_games': popular_games,'posts': posts,'ads_code':ads_code})

def detailpage2(request,id):
    allgames = Game.objects.all()
    game = Game.objects.get(id=id)
    game.views_count += 1
    game.save()
    popular_games = Game.objects.order_by('-views_count')[:5]
    posts = Post.objects.all()
    ads_code = AdsCode.objects.first()
    return render(request, 'detailpage2.html',{'game': game,'allgames':allgames,'popular_games':popular_games,'posts': posts,'ads_code':ads_code})

def blog(request):
    posts = Post.objects.all()
    popularpost = Post.objects.order_by('-views')[:1]
    topapp = Post.objects.filter(categories__name='Top App').order_by('-views')[:1]
    topgame = Post.objects.filter(categories__name='Top Games').order_by('-views')[:2]
    popular_games = Game.objects.order_by('-views_count')[:4]
    ads_code = AdsCode.objects.first()
    return render(request, 'blog.html',{'blogs': posts,'popularpost': popularpost,'topapp':topapp,'topgame':topgame,'popular_games': popular_games,'ads_code':ads_code})


def allgames(request):
    game = Game.objects.all()
    popular_games = Game.objects.order_by('-views_count')[:4]
    ads_code = AdsCode.objects.first()
    return render(request, "html5allgames.html",{'game':game,'popular_games': popular_games,'ads_code':ads_code})



def gamerivew(request):
    game = Game.objects.all()
    popular_games = Game.objects.order_by('-views_count')[:4]
    ads_code = AdsCode.objects.first()
    return render(request, 'gamerivew.html',{'game':game,'popular_games': popular_games , 'ads_code':ads_code})

def about(request):
    popular_games = Game.objects.order_by('-views_count')[:4]
    return render(request, 'about.html',{'popular_games': popular_games})

def blogdetail(request, slug):
    post = Post.objects.get(slug=slug)
    allgames = Game.objects.all()
    ads_code = AdsCode.objects.first()
    popular_games = Game.objects.order_by('-views_count')[:3]
    post.increase_views()
    return render(request, 'blogdetail.html', {'post': post,'allgames':allgames,'popular_games': popular_games,'ads_code':ads_code})

def privacy(request):
    return render(request, 'privacy.html')


def disclamer(request):
    return render(request, 'disclamer.html')

def ads_txt(request):
    file_path = os.path.join(os.path.dirname(__file__), 'ads.txt')
    with open(file_path, 'r') as f:
        return HttpResponse(f.read(), content_type="text/plain")



