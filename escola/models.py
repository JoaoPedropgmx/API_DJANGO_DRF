from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    niveis = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    nome = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    descricao = models.TextField()
    nivel = models.CharField(max_length=1, choices=niveis, blank=False, default='B')

    def __str__(self):
        return self.descricao
    
class Matricula(models.Model):
    periodos = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=periodos, blank=False, default='M')
