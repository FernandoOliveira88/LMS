from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def detalhecurso(request):
    return render(request, 'detalhecurso.html')

def disciplinas(request):
    return render(request, 'disciplinas.html')

def listascursos(request):
    return render(request, 'listascursos.html')

def noticias(request):
    return render(request, 'noticias.html')
