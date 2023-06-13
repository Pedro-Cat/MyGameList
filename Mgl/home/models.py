from django.db import models
from user.models import Profile
from django.db.models.signals import post_save
from django.db.models import Avg

import pathlib
import uuid
# Create your models here.

# Classes:
# Nota  {nome, jogo, API} # provavelmente haverá métodos: calcular média das notas referentes ao jogo, diferenciar quando for utilizada API ou não, construtor, if/else
# Jogo  {nome, imagem, notas(ArrayNota), descrição, criadores, plataformas, data-de-lançamento, tags}
# Lista {jogos(ArrayJogo), dataLimiteInicial, dataLimiteFinal, tags, nomeNota, ordemCrescenteDecrescente}
# BarraDePesquisa {String} - Prioridade de exibição: Jogo -> Profile -> Pergunta  

def game_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f'game_images/{new_fname}{fpath.suffix}'

class Plataform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
class Game(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=game_upload_handler)
    user_score = models.FloatField(null=True)
    metacritic_score = models.FloatField(null=True)
    sumary = models.TextField(max_length=3000)
    developers = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100) 
    plataform = models.ForeignKey(Plataform, related_name='plataform', on_delete=models.CASCADE, blank=True, null=True)
    plataforms = models.ManyToManyField(Plataform, related_name='plataforms', blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    release_date = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.plataform.name}'
        # return f'{self.name} - {self.platforms[0]}'

    # def update_score(sender, instance, created, **kwargs):
    #     if created:
    #         instance.game.user_score = Review.objects.filter(game=instance.game).aggregate(Avg('score'))
            
    # post_save.connect(update_score, sender=Review)

class Review(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000, blank=True, null=True)
    score = models.FloatField()
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.nick}'s review to {self.game.name} - {self.score}"


    
    # Quando o game for criado, usar uma play parecida com a usada no Profile para inserir os dados restantes durante a criação

# class List(models.Model):
#     games = models.ManyToManyField(Game, symmetrical=False)
