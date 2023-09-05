from django.contrib import admin
from .models import *


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10


admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display =  ('id', 'nome', 'professor','nivel')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display =  ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', 'aluno')
    search_fields = ('nome', 'id')
    list_per_page = 10

admin.site.register(Matricula, Matriculas)