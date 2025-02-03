from django.shortcuts import render, redirect
from .forms import UtilisateurCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès !")
            return redirect('login')
    else:
        form = UtilisateurCreationForm()
    return render(request, 'utilisateurs/register.html', {'form': form})



from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('home')
        else:
            messages.error(request, "Identifiants incorrects.")
    
    return render(request, 'utilisateurs/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Déconnexion réussie !")
    return redirect('login')
