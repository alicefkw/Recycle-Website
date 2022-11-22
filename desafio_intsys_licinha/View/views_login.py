from django.shortcuts import render, redirect
from django.contrib import messages
from Model.usuarios.forms import FormUsuarios
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class Cadastro():
	ir = False

def entrar(request):
	if request.method == "POST":
		nome_de_usuario = request.POST['username']
		senha = request.POST['password']

		user = authenticate(request, username = nome_de_usuario, password = senha)
		if user is not None:
			form = login(request, user)

			if Cadastro.ir == True:
				print(Cadastro.ir)
				messages.success(request, f'Bem-vindo(a), {user}!')
				return redirect('cadastro_produto')
			else:
				print(Cadastro.ir)
				messages.success(request, f'Bem-vindo, {user}!')
				return redirect('index')
		else:
			messages.error(request, 'Nome e/ou senha inválidos!')

	form = AuthenticationForm()
	return render(request, 'login/login.html', {'form': form})

def registro(request):
	if request.method == 'POST':
		form = FormUsuarios(request.POST)
		if form.is_valid():
			#print(request.POST)
			#form.save()
			u = User.objects.create_user(request.POST['nome_de_usuario'], request.POST['email'], request.POST['password1'])
			#u.nome = request.POST['nome']
			messages.success(request, f'Conta criada com sucesso. Entre agora!')    
			return redirect('entrar')
		#else:
		#	messages.warning(request, '*Ocorreu algum problema, por favor tente novamente')
		#	return redirect('registro')
	else:
		form = FormUsuarios()

	context = {'form': form}
	return render(request, 'login/registro.html', context)