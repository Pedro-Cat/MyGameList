from django.contrib import admin
from .models import Game, Review, Plataform, Tag, Tierlist
# Register your models here.

admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Plataform)
admin.site.register(Tag)
admin.site.register(Tierlist)