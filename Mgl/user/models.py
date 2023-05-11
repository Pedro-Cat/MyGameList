from django.db import models

# Create your models here.
# Classes: 
# Profile(User) {nick, nick-em-outras-plataformas, avatar, seguidores(ArrayProfile), seguidos, posts, tierlist-personalizada, Lista, conquistas, data-de-criação, data-de-nascimento, jogos(Array{jogo:double}), *report*, *nsfw*}   
# Configuração {Profile, ...} - As configurações serão salvas com base no usuário. Caso o usuário não esteja logado, nem todas as configurações estarão disponíveis e serão usadas as configurações padrão.
