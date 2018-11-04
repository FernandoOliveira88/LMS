from django.db import models
from .usuario import Aluno, Coordenador, Professor

class Disciplina(models.Model):
    idDisciplina = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, unique=True)
    data = models.DateField(default=True)
    Status = models.TextField(default=True)
    PlanodeEnsino = models.TextField(max_length=255)
    CargaHoraria = models.IntegerField()
    Competencias = models.TextField(max_length=255)
    Habilidades = models.TextField(max_length=255)
    Ementa = models.TextField(max_length=255)
    ConteudoProgramatico = models.TextField(max_length=255)
    BibliografiaBasica = models.TextField(max_length=255)
    BibliografiaComplementar = models.TextField(max_length=255)
    PercentualPratico = models.IntegerField()
    PorcentualTeorico = models.IntegerField()
    idCoordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)

class Curso(models.Model):
    nome = models.TextField(max_length=255, unique=True)
    Id_Curso = models.AutoField(primary_key=True)
    
class DisciplinaOfertada(models.Model):
    IdDisciplinaOfertada= models.AutoField(primary_key=True)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    idCoordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
    Dt_inicio_Matricula = models.DateField()
    Dt_fim_Matricula = models.DateField()
    Turma = models.TextField(max_length=255)
    idProfessor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    Metodologia = models.TextField(max_length=255)
    CriterioAvaliacao = models.TextField(max_length=255)
    PlanodeAulas = models.TextField(max_length=255)





class SolicitacaoMatricula(models.Model):
    IdSolicitacaoMatricula = models.AutoField(primary_key=True)
    idAluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    idCoordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
    idDisciplinaOfertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    status = models.TextField(max_length=255)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    disciplina_Ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    DataSolicitacao = models.DateField(default=True)

class Atividade(models.Model):
    idAtividade = models.AutoField(primary_key=True)
    Titulo = models.TextField(max_length=255, unique=True)
    Descricao = models.TextField(max_length=255)
    Tipo = models.TextField()
    Extras = models.URLField
    id_Professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

class AtividadeVinculada(models.Model):
    IdatividadeVinculada = models.AutoField(primary_key=True)
    IdAtividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    idProfessor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    idDisciplinaOfertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    Rotulo = models.TextField(max_length=255)
    status = models.TextField(max_length=255)
    DtInicioRespostas = models.DateField()
    DTFimRespostas = models.DateField()

class Entrega(models.Model):
    IdEntrega = models.AutoField(primary_key=True)
    IdAluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    idAtividadeVinculada = models.ForeignKey(AtividadeVinculada, on_delete=models.PROTECT)
    Titulo = models.TextField(max_length=255)
    Resposta = models.URLField(max_length=255) 
    DtEntrega = models.DateTimeField()
    Status = models.TextField(max_length=255)
    idProfessor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    Nota = models.IntegerField()
    DtAvaliacao = models.DateTimeField()
    OBS = models.TextField(max_length=255)



