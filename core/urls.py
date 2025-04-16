from django.contrib import admin
from django.urls import path
from .views import home , page , allgames

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('page/', page, name='page'),
    path('allgames/', allgames, name='allgames')
]
