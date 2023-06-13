from django.db import models
from django.contrib.auth.models import User
from user.models import Profile
import pathlib
import uuid

# Create your models here.
# Classes: 
# Post {perfil, texto, idPostPai(Id de outro Post), arquivo, data-de-post, like, oculto, deletado, *nsfw*, *report*}   

def post_upload_handler(instance, filename):
	fpath = pathlib.Path(filename)
	new_fname = str(uuid.uuid1())
	return f'post_media/{new_fname}{fpath.suffix}'

# Create a Post model
class Post(models.Model):
        user = models.ForeignKey(
            Profile, related_name='post',
            on_delete=models.CASCADE
        )
        body = models.CharField(max_length=300)
        post_father = models.BigIntegerField(primary_key=False, blank=True, null=True)
        archive = models.FileField(upload_to=post_upload_handler, blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        likes = models.ManyToManyField(User, related_name='post_like', blank=True)
        edited = models.BooleanField(blank=True)
        filed = models.BooleanField(blank=True)
        deleted = models.BooleanField(blank=True)

        # Get numbers of likes
        def get_likes(self):
            return self.likes.count()

        def __str__(self):
            return (
                f'{self.user} '
                f'({self.created_at:%Y-%m-%d %H:%M}): '
                f'{self.body}'
            )
