from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from . import views
from django.contrib import messages
from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    return render(request,'accounts/dashboard.html')

def customers(request):
    return render(request,'accounts/customers.html')
def products(request):
    return render(request,'accounts/products.html')
def about(request):
    return render(request,'accounts/about.html')
# Dans votre fichier views.py

from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.shortcuts import render, redirect
from .models import Client
def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Vérification de l'existence de l'utilisateur dans la base de données
        if Client.objects.filter(name=username).exists() or Client.objects.filter(email=email).exists():
            messages.error(request, 'Un utilisateur avec ce nom d\'utilisateur ou cette adresse e-mail existe déjà.')
            return redirect('inscription')
        
        # Création de l'utilisateur s'il n'existe pas déjà
        Client.objects.create(name=username, email=email, password=password)
        messages.success(request, 'Inscription réussie. Connectez-vous maintenant.')
        return redirect('connexion')  # Redirection vers la page de connexion après l'inscription
    
    return render(request, 'accounts/inscription.html')

# Fonction de connexion
def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirection vers le tableau de bord en cas de succès
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/connexion.html', {'form': form})




def deconnexion(request):
    logout(request)
    return redirect('connexion')