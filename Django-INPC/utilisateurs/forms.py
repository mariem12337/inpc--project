from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur
from django import forms

class UtilisateurCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=Utilisateur.ROLE_CHOICES, required=True)

    class Meta:
        model = Utilisateur
        fields = ['username', 'role', 'password1', 'password2']
