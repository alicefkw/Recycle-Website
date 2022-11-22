from django.contrib import admin
from .models import Produtos

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'quantidade', 'cidade', 'rua', 'agendamento', 'nome_de_usuario']