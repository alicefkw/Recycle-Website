from django.urls import path
from View import views_produtos as vp

urlpatterns = [
    path('fazer-pedido/', vp.cadastro_produto, name = 'cadastro_produto'),
    path('confirmacao/', vp.confirmacao, name = 'confirmacao'),
    path('listagem/', vp.listagem, name = 'listagem'),
]
