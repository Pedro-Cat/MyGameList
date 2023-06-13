from django.urls import path

from .views import *

urlpatterns = [
    path('home/', HomeView, name='home'),
    path('meta/', load_json, name='meta'),
    path('search_page/', SearchView, name='search'),
    path('game-<int:pk>', GameView, name='game'),
    #path('game_page/<int:pk>', GameView.as_view(), name='game-view'),
    #path('tierlist/<int:pk>', TierListView.as_view(), name='tierlist-view')
]