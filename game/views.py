from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, BetForm
from .models import CustomUser, Bet
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def home(request):
    return render(request, 'game/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('game')
    else:
        form = CustomUserCreationForm()
    return render(request, 'game/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('game')
    else:
        form = AuthenticationForm()
    return render(request, 'game/login.html', {'form': form})

def game(request):
    if request.method == 'POST':
        form = BetForm(request.POST)
        if form.is_valid():
            bet = form.save(commit=False)
            bet.user = request.user
            if request.user.coins >= bet.amount:
                request.user.coins -= bet.amount
                request.user.save()
                bet.save()
                return redirect('game')
    else:
        form = BetForm()
    return render(request, 'game/game.html', {'form': form})

@csrf_exempt
def update_coins(request):
    if request.method == 'POST':
        coins = int(request.POST.get('coins'))
        request.user.coins = coins
        request.user.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'})