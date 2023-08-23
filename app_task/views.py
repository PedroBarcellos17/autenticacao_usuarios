from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
#Home do projeto
def home(request):
    return render(request, 'menu.html')

def cadastro(request):

    if request.method == 'GET':
        return render(request, 'cadastrar.html', {
          'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Isso é um código q o próprio django tem de autenticação de usuário
                user = User.objects.create_user(username=request.POST['email'], password=  request.POST['passwword1'])
                user.save()
                login(request, user)
                return redirect('login')
            except:

                return render(request, 'cadastrar.html',{
                'form': UserCreationForm,
                "error": 'Usuário já existe!'

                })
        return render(request, 'cadastrar.html',{
            'form': UserCreationForm,
            "error": 'Senhas incorreta'
        })
def logar(request):

    if request.method == 'GET':
        return render(request, 'login.html',{
        'form': AuthenticationForm
        })

    else:
        user = authenticate(
            request, username=request.POST['email'], password=request.POST['password'])

        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                "error": 'Usuário ou senha incorreto'
            })
        else:
            login(request, user)
            return redirect('tasks')

@login_required
def tasks(request):
    return render(request, 'tasks.html')

@login_required
def sair(request):
    logout(request)
    return redirect('home')
