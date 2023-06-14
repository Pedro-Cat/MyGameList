from typing import Any, Dict
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
import json

# Create your views here.
def HomeView(request):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(Profile, user_id=request.user)
        metacritc_best_games = Game.objects.order_by('-metacritic_score')
        user_best_games = Game.objects.order_by('-user_score')
        new_games = Game.objects.order_by('-release_date', '-metacritic_score')
        best_rpg_games = Game.objects.filter(tags=16).order_by('-metacritic_score', '-user_score')
        best_open_world_games = Game.objects.filter(tags=10).order_by('-metacritic_score', '-user_score')
        best_shooter_games = Game.objects.filter(tags=4).order_by('-metacritic_score', '-user_score')
        best_fantasy_games = Game.objects.filter(tags=1).order_by('-metacritic_score', '-user_score')
        best_simulators_games = Game.objects.filter(tags=54).order_by('-metacritic_score', '-user_score')
        
        return render(request, 'home.html', {'user_profile': user_profile,
                                            'lists': {
                                            'Best Games By Metacritic': metacritc_best_games[:5], 
                                            'Most Popular Games': user_best_games[:5], 
                                            'Most Recent Games Released': new_games[:5], 
                                            "Best RPG's": best_rpg_games[:5], 
                                            "Best Open World Games": best_open_world_games[:5], 
                                            "Best Shooter's": best_shooter_games[:5], 
                                            "Best Fantasies": best_fantasy_games[:5], 
                                            "Best Simulators": best_simulators_games[:5]}
                                            })
    else:
        metacritc_best_games = Game.objects.order_by('-metacritic_score')
        user_best_games = Game.objects.order_by('-user_score')
        new_games = Game.objects.order_by('-release_date', '-metacritic_score')
        best_rpg_games = Game.objects.filter(tags=16).order_by('-metacritic_score', '-user_score')
        best_open_world_games = Game.objects.filter(tags=10).order_by('-metacritic_score', '-user_score')
        best_shooter_games = Game.objects.filter(tags=4).order_by('-metacritic_score', '-user_score')
        best_fantasy_games = Game.objects.filter(tags=1).order_by('-metacritic_score', '-user_score')
        best_simulators_games = Game.objects.filter(tags=54).order_by('-metacritic_score', '-user_score')
        
        return render(request, 'home.html', {'lists': {
                                            'Best Games By Metacritic': metacritc_best_games[:5], 
                                            'Most Popular Games': user_best_games[:5], 
                                            'Most Recent Games Released': new_games[:5], 
                                            "Best RPG's": best_rpg_games[:5], 
                                            "Best Open World Games": best_open_world_games[:5], 
                                            "Best Shooter's": best_shooter_games[:5], 
                                            "Best Fantasies": best_fantasy_games[:5], 
                                            "Best Simulators": best_simulators_games[:5]}
                                            })
    

def GameView(request, pk):
    game = get_object_or_404(Game, id=pk)
    if request.user.is_authenticated:
        form = ReviewForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                review = form.save(commit=False)
                review.profile = request.user.profile
                review.game = get_object_or_404(Game, id=pk)
                review.save()
                review.game.user_score = Review.objects.filter(game=review.game).aggregate(Avg('score'))['score__avg']
                print(round(review.game.user_score, 1))
                review.game.user_score = round(review.game.user_score, 1)
                review.game.save()
                messages.success(request, ('Your Review Has Been Posted!'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        reviews = Review.objects.filter(game=game).order_by('-release_date')
        return render(request, 'game_page.html', {'game': game, 'form': form, 'reviews': reviews})
    
    else:
        reviews = Review.objects.filter(game=game).order_by('-release_date')
        return render(request, 'game_page.html', {'game': game, 'reviews': reviews})
    
def SearchView(request):
    if request.method == 'POST':
        searchInput = request.POST.get('searched')
        game_results = Game.objects.filter(name__contains=searchInput)
        profile_results = Profile.objects.filter(nick__contains=searchInput)
        return render(request, 'search.html', {'search':searchInput,
                                                'game_results':game_results,
                                                'profile_results':profile_results})
    else:
        return render(request, 'search.html')
    
def load_json(request):
    meta = open('home/meta.json', encoding="utf8")
    data = json.load(meta)
    meta.close()
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for game in data:
        date = game['release_data'].strip()
        pos = months.index(date[:3])
        if date[4] == ' ':
            r_date = date[-4:] + '-' + str(pos + 1) + '-' + date[5:-6]
        else:
            r_date = date[-4:] + '-' + str(pos + 1) + '-' + date[4:-6]
        #print(r_date)
        try:
            Plataform.objects.get(name=game['plataform'])

        except:
            Plataform.objects.create(name=game['plataform'])

        try:
            Game.objects.get(name=game['name'], plataform=Plataform.objects.get(name=game['plataform']))
        except:
            g = Game.objects.create(
                name=game['name'],
                publisher=game['publisher'],
                plataform=Plataform.objects.get(name=game['plataform']),
                release_date=r_date,
                developers=game['developers'],
                sumary=game['sumary'],
                metacritic_score=game['metascore'],
                image=game['image'],
            )

            print(g.name)
            for plataform in game['plataforms']:
                try:
                    g.plataforms.add(Plataform.objects.get(name=plataform))
                except:
                    Plataform.objects.create(name=plataform)
                    g.plataforms.add(Plataform.objects.get(name=plataform))
                    
            for tag in game['genres']:
                try:
                    g.tags.add(Tag.objects.get(name=tag))
                except:
                    Tag.objects.create(name=tag)
                    g.tags.add(Tag.objects.get(name=tag))

    return render(request, 'meta.html')

# def ReviewCreate(request, pk):
#     if request.user.is_authenticated:
#         form = ReviewForm(request.POST or None)
#         if request.method == 'POST':
#             if form.is_valid():
#                 review = form.save(commit=False)
#                 review.profile = request.user.profile
#                 review.game = get_object_or_404(Game, id=pk)
#                 review.save()
#                 messages.success(request, ('Your Review Has Been Posted!'))
#                 return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
#     else:


# class GameView(DetailView):
#     model = Game
#     template_name = 'game_page.html'

# Provavelmente vai virar uma função
# class TierListView(DetailView):
#     #model = List
#     template_name = 'tierlist_page.html'


# Views:
# HomeView - listas

# ListView - Alternar visibilidade entre lista maximizada e minimizada
# ListCreate
# ListUpdate 
# ListDelete

# JogoView - Alternar visibilidade entre jogo maximizado e minimizado, barra de pesquisa e profile
# JogoCreate
# JogoUpdate 
# JogoDelete

# BarraDePesquisaView
# BarraDePesquisaUpdate