from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)

# @admin.register(Profile)

# class ProfileAdmin(admin.ModelAdmin):
#     fields = ("user", "nick", "follows", "register_date")


# User: CDClos
# Senha: BBB