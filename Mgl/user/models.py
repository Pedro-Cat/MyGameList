from django.db import models



# Create your models here.
# Classes: 
# Profile(User) {nick, nick-em-outras-plataformas, avatar, posts, tierlist-personalizada, Lista, cargo, conquistas, data-de-criação, data-de-nascimento, *report*, *nsfw*}   
# Avaliacao {profile, jogo, double(0-10)}
# SeguidoSeguidores {Seguidor(Profile), Seguido(Profile)}
# Configuração {Profile, ...} - As configurações serão salvas com base no usuário. Caso o usuário não esteja logado, nem todas as configurações estarão disponíveis e serão usadas as configurações padrão.
