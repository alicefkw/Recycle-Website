from django.shortcuts import render

def instrucao(request):
    return render(request, 'instrucao.html')

def index(request):
    return render(request, 'index.html')