from django.urls import path
from .views import UserView

urlpatterns = [
    # Colocar nome do usuário como url #
    path('user/', UserView.as_view(), name='user')
]