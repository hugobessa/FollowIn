# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from usuario.models import Usuario
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


def verificar(email):
    return len(Usuario.objects.filter(email__exact = email ))>=1

@csrf_exempt
def cadastro(request):
    if request.method =='POST':
        nome = request.POST['nome'] 
        sobrenome = request.POST['sobrenome'] 
        email = request.POST['email']
        senha = request.POST['senha']
        confsenha = request.POST['confsenha']
        accept = request.POST['readandaccept']
        
        if not verificar(email) and senha==confsenha:  
            if ('@' in email):
                user = Usuario(nome = nome, sobrenome = sobrenome, email = email, senha=senha)
                user.save()
                print "Funcionou"
            else:
                print "Coloque um email valido"
        else:
            print "Usuario ja cadastrado"
        
        return render_to_response('login.html',locals(),context_instance=RequestContext(request))    
        
    else:
        print "Entrou como get"
        return render_to_response('login.html',locals(),context_instance=RequestContext(request))    
    