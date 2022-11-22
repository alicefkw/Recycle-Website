"""desafio_intsys_licinha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from View import views_geral as vg, views_login as vl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vg.instrucao, name = 'instrucoes'),
    path('index/', vg.index, name = 'index'),
    path('cadastro/', vl.registro, name = 'registro'),
    path('login/', vl.entrar, name = 'entrar'),
    path('#', auth_views.LogoutView.as_view(template_name='index.html'), name = 'sair'),
    path('produtos/', include('Model.produtos.urls')),
]
