from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormUsuarios(UserCreationForm):
    nome_de_usuario = forms.CharField(label = 'Nome de usuário:', max_length = 15, required = True)
    nome = forms.CharField(label = 'Nome social:', max_length = 101, required = True)
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['nome_de_usuario', 'nome', 'email', 'password1', 'password2']