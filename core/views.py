from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login # as duas funções responsáveis pela autenticação: 1-authenticate - verifica o login e senha; 2- login - realiza a autenticação no sistema.
from django.contrib.auth import logout #função responsável pelo logout
from django.contrib.auth.decorators import permission_required #Definindo que o acesso à View só será feito por usuários que tiverem a permissão permissao_adm_1 definida:
from django.contrib.auth.models import Permission #Primeiro passo: Importar o objeto Permission em Views:
from django.contrib.auth.forms import UserCreationForm #Registro: UserCreationForm: é um ModelForm que já vem implementado no Django, com 3 campos para o registro de usuário: username, password1 e password2.
#from .forms import  CategoriaForm, UsuarioForm #importando a class criado em forms.py 
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm
#from .forms import UsuarioForm

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def home (resquest):
    return render(resquest, "index.html")



def autenticacao(request):
    '''
    se o usuário digitou algo no formulário e clicou em enviar, o if 
    será verdadeiro, caso contrário, será uma requisição GET e entrara no else.
    -
    '''
    if request.POST:
       usuario = request.POST['usuario']
       senha = request.POST['senha']
       user = authenticate(request, username=usuario, password=senha)
       if user is not None:
        login(request, user)
        #messages.success(request, 'Bem-vindo(a)') #corrigir
        return redirect('perfil')
       else:
        return redirect('login') 
    else:
        return render(request, 'registration\login.html') 
    

def cadastro_manual(request):
    

    user = Usuario.objects.create_user(
        username='claudio01',
        email='claudio@email.com',
        cpf='333333333',
        nome='Claudio Rodrigues',
        password='emac0203',
        telefone=84987000000,
        #categoria = Categoria.objects.get(pk=1),
        is_superuser=False)
        
    permission1 = Permission.objects.get(codename='Administrador')
    user.user_permissions.add(permission1)


    user.save()
    return redirect('home')   


def desconectar(request):
    logout(request)
    return render(request, 'index.html')   



def registro(request):
    form = UsuarioForm(request.POST or None) #Inplemantando o registro utilizando a class criada emm 'forms.py'
    if form.is_valid(): #Ao realizar o registro, automaticamente o usuário será redirecionado para a página de login:
        form.save()
        return redirect('login')
    contexto = {
        'form': form
        }
    return render(request, 'registro.html', contexto)