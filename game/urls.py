from django.urls import path
from .views import home, register, login_view, game, update_coins

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('game/', game, name='game'),
    path('update_coins/', update_coins, name='update_coins'),
]