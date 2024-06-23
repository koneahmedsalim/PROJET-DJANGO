from django.shortcuts import render, redirect
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm


def categorys(request):
    categorys = Category.objects.all()
    
    return render(request, 'categorys.html', {'categorys': categorys})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        categorys = Category.objects.all()
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category': category})
    

    except:
        messages.success(request,("that category Doesn't not exist"))
        
        
        return redirect('home')

def home(request):
    categorys = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'home.html', {'categorys': categorys, 'products': products})



def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in!")
                return redirect('home')
            else:
                messages.error(request, "There was an error, please try again.")
                return redirect('login')
        else:
            messages.error(request, "Please fill out all fields.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logout...Thanks for stopping by...."))
    return redirect('home') 


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("You have registered Successfully!! Welcome!"))
            return redirect('home')
        else:
            messages.success(request, ("ERREUR Probleme d'enregistrement veuillez recommencer!!"))
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def product(request, pk):
    product =  Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})
