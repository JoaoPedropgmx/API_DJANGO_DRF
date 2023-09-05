from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    curso = serializers.ReadOnlyField(source='curso.nome')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['id','aluno', 'curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.nome')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['id','curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class listaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    id_aluno = serializers.ReadOnlyField(source='aluno.id')
    class Meta:
        model = Matricula
        fields = ['id_aluno','aluno']