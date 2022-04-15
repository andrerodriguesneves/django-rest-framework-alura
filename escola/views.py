from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """  Json com todos os alunos cadastrados   """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """ Json com todos os cursos cadastrados """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """ Json com todos as matriculas cadastrados """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

