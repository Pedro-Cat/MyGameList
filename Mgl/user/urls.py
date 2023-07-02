from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


urlpatterns = [
    # Colocar nome do usuário como url #
    path('register/', UserCreate, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileView, name='profile'),
    path('profile/update/', ProfileUpdate, name='profile-update'),
    # Modificar Delete #
    path('delete/<int:pk>', UserDelete.as_view(), name='user-delete'),
    path('profile/<int:pk>/follow', ProfileFollow, name='follow'),
]