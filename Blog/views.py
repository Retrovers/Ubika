from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.validators import validate_email

##Other
def Index(request):
    articles = Article.objects.order_by('published_date')[:3]
    return render(request, 'index.html', {'articles': articles})

def Jouer(request):
    return render(request, 'play.html')

##Blog
def BlogList(request):
    articles = Article.objects.order_by('published_date')
    return render(request, 'list.html', {'articles': articles})

def BlogView(request,slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'view.html', {'article' : article})

##User
def UserLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'Vous etes deconnecté')
        return redirect('index')
    else:
        messages.warnig(request, 'Vous devez etre connecté pour acceder a cette page') 
        return redirect('user_login')  

def UserLogin(request):
     username = request.POST.get('username', '')
     password = request.POST.get('password', '')
     if username and password != None:
        user = authenticate(username=username, password=password)   
        if user is not None:
            login(request, user)
            messages.success(request, 'Vous êtes connzcté')
            return redirect('index')
        else:
            messages.warning(request, 'Identifiant / mot de passe eronée')
            return render(request, 'user/login.html')
     else:        
        return render(request, 'user/login.html')

def UserRegister(request):
     username = request.POST.get('username', '')
     password = request.POST.get('password', '')
     passwordV = request.POST.get('passwordV', '')
     email = request.POST.get('email', '')
     if username and password and email and passwordV != None:
        if password == passwordV:
            if len(password) >= 8:
                if User.objects.filter(username=username).count() == 0:
                    messages.success(request, "Vous etes inscrit, connectez vous pour la premiere fois pour visiter le site")
                    User.objects.create_user(username=username,email=email,password=password)
                    return redirect('user_login')    
                else:
                    messages.warning(request, "Le nom d'utilisateur est deja utilisé")
                    return render(request, 'user/register.html')            
            else:
                messages.warning(request, "Le mot de passe n'es pas correct, il doit etre long de 8 caracteres maximum")
                return render(request, 'user/register.html')
        else:
            messages.warning(request, 'Les deux mots de passes ne corresponde pas')
            return render(request, 'user/register.html')    
     else:        
        return render(request, 'user/register.html')

def UserSetting(request):
    if request.user.is_authenticated:
        return render(request, 'user/setting.html')
    else:
        messages.warnig(request, 'Vous devez etre connecté pour acceder a cette page') 
        return redirect('user_login')   