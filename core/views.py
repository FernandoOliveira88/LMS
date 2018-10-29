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

def login(request):
    return render(request, 'login.html')

def area_do_professor(request):
    return render(request, 'area_do_professor.html')

def area_do_aluno(request):
    return render(request, 'area_do_aluno.html')