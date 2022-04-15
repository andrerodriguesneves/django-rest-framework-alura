from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel_curso')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso', )
# Register your models here.

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    # o que será exibido
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', )

# Matricula(Class do modes) / Matriculas(Class do admin)
admin.site.register(Matricula, Matriculas)
