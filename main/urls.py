from django.urls import path
from .views import home , detailpage1 , allgames , gamerivew, about , blog , detailpage2 , blogdetail , privacy , disclamer , ads_txt


urlpatterns = [
  
  path('', home, name='home'),
  path('game/<int:id>/', detailpage1, name='game_detail'),
  path('gamepage/<int:id>', detailpage2, name='detailpage2'),
  path('allgames/', allgames, name='allgames'),
  path('gamerivew/', gamerivew, name='gamerivew'),
  path('about/', about, name='about'),
  path('blog/', blog, name='blog'),
  path('blog/<slug:slug>/', blogdetail, name='blog_detail'),
  path('privacy/', privacy, name='privacy'),
  path('disclamer/', disclamer, name='disclamer'),
  path('ads.txt', ads_txt, name='ads_txt'),
  
]