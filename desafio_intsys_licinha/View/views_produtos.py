from django.shortcuts import render, redirect
from django.contrib import messages
from .views_login import Cadastro
from Model.produtos.forms import FormProdutos
from Model.produtos.models import Produtos

def cadastro_produto(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            form = FormProdutos()
            return render(request, 'pedidos/cadastro_produto.html', {'form': form})
        else:
            # redireciona para tela de login se não estiver autenticado
            Cadastro.ir = True # depois da tela de login volta para cadastro_produto
            return redirect('entrar')
    else:
        form = FormProdutos(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.nome_de_usuario = request.user
            instance.agendamento = request.POST['agendamento']

            Produtos(nome_de_usuario = request.user)

            instance.save()

            messages.success(request, 'Maravilha!!! Tudo certinho :)\nSeu pedido de coleta foi cadastrado com sucesso')
            return redirect('confirmacao')
        else:
            messages.warning(request, '*Ocorreu algum problema, por favor tente novamente')
            return redirect('cadastro_produto')

def confirmacao(request):
    return render(request, 'pedidos/confirmacao.html')

def listagem(request):
    if request.user.is_authenticated:
        if Produtos.objects.filter(nome_de_usuario = request.user).exists():
            produtos = Produtos.objects.filter(nome_de_usuario = request.user)
        else:
            produtos = None
        return render(request, 'pedidos/listagem.html', {'produtos': produtos})
    else:
        messages.warning(request, '*É necessário entrar com uma conta para ver a lista de pedidos')
        return redirect('entrar')