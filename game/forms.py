from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Bet

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class BetForm(forms.ModelForm):
    KANGAROO_CHOICES = [
        ('Кенгуру 1', 'Кенгуру 1'),
        ('Кенгуру 2', 'Кенгуру 2'),
        ('Кенгуру 3', 'Кенгуру 3'),
        ('Кенгуру 4', 'Кенгуру 4'),
    ]
    kangaroo = forms.ChoiceField(choices=KANGAROO_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Bet
        fields = ['kangaroo', 'amount']