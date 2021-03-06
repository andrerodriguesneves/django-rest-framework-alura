from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """  Json com todos os alunos cadastrados   """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """ Json com todos os cursos cadastrados """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """ Json com todos as matriculas cadastrados """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# Essa class, so lista os cursos, nao tem todos os verbos http
class ListaMatriculasAlunos(generics.ListAPIView):
    """
        Listando as matriculas de um aluno(a)
    """
    # Criando uma função para pegar as matriculas do aluno
    def get_queryset(self):
        queryset= Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    """ Listando os alunos matriculados em um curso """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


