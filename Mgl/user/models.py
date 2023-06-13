from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import pathlib
import uuid


# Create your models here.
# Classes: 
# Profile(User) {nick, nick-em-outras-plataformas, avatar, posts, tierlist-personalizada, Lista, cargo, conquistas, data-de-criação, data-de-nascimento, *report*, *nsfw*}   
# Avaliacao {profile, jogo, double(0-10)}
# SeguidoSeguidores {Seguidor(Profile), Seguido(Profile)}
# Configuração {Profile, ...} - As configurações serão salvas com base no usuário. Caso o usuário não esteja logado, nem todas as configurações estarão disponíveis e serão usadas as configurações padrão.

def profile_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f'avatar_images/{new_fname}{fpath.suffix}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick = models.TextField(max_length=20)
    avatar = models.FileField(null=True, blank=True, upload_to=profile_upload_handler)
    register_date = models.DateTimeField(User, auto_now=True)
    birth_date = models.DateField(null=True)
    follow = models.ManyToManyField("self", blank=True, symmetrical=False, related_name='followed_by')

    def __str__(self):
        return f"{self.user.username}  - {self.nick}"

    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile(user=instance, nick=instance.username, avatar='avatar_images/default_userimage.jpg')
            user_profile.save()
            user_profile.follow.set([instance.profile.id])
            user_profile.save()
            user_settings = Settings(profile=user_profile)
            user_settings.save()
            
    post_save.connect(create_profile, sender=User)


class Settings(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profile.user.username} settings"
    