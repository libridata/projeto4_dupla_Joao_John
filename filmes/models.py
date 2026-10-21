from django.db import models

class Generos(models.Model):
   nome = models.CharField(max_length=255)  # nome do gênero

   def __str__(self):
       return self.nome  # representação em string do gênero

class Filmes(models.Model):
   titulo = models.CharField(max_length=255)           # título do filme
   descricao = models.CharField(max_length=500)           # título do filme
   ano_lancamento = models.PositiveIntegerField()                  # ano de lançamento do filme (positivo)
   genero = models.ForeignKey(Generos, on_delete=models.CASCADE)  # chave estrangeira para tabela generos
   duracao = models.PositiveIntegerField()              # duracao do filme em minutos (positivo)
   

   def __str__(self):
       return self.titulo  # representação em string do filme
