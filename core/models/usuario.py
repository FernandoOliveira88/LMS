from django.db import models

class Usuario(models.Model):
    id =  models.AutoField(primary_key=True)
    login = models.TextField(max_length=20, unique=True)
    senha = models.TextField(max_length=20)
    DtExpiracao = models.DateField(default=True)
    

class Aluno(Usuario):
    id_aluno =  models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255, unique=True )
    celular = models.TextField(max_length=255, unique=True)
    RA = models.TextField(max_length=10)

    def matriculas(self):
        from .disciplina import SolicitacaoMatricula
        sm = SolicitacaoMatricula.objects.filter(Aluno=self)
        return sm

class Professor(Usuario):
    id_professor = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True )
    celular = models.TextField(max_length=255, unique=True)
    apelido = models.TextField(max_length=30)

class Coordenador(Usuario):
    id_coordenador = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True )
    celular = models.TextField(max_length=255, unique=True)
    apelido = models.TextField(max_length=30)

    
