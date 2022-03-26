from django.db import models
from datetime import date
from usuarios.models import Usuario

class Categoria (models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
          return self.nome

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length = 100, blank = True)
    data_emprestimo = models.DateTimeField(blank = True, null = True)
    data_devolucao = models.DateTimeField(blank = True, null = True)
    tempo_duracao = models.DateField(blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome


class Emprestimos(models.Model):
    
    #nome_emprestado_anonimo = models.CharField(max_length = 100, blank = True)
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateField(blank = True, null = True)
    data_devolucao = models.DateField(blank = True, null = True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return f"{self.nome_emprestado} | {self.livro}"