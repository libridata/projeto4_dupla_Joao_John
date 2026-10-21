from django.contrib import admin
from .models import Generos, Filmes
from rest_framework.authtoken.models import Token

# Admin para o modelo Generos: mostra o campo 'nome' e permite busca por nome
@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
   list_display = ['nome']  # colunas exibidas na listagem
   search_fields = ['nome'] # campos pesquisáveis

# Admin para o modelo Filmes: exibe campos principais e adiciona filtros
@admin.register(Filmes)
class FilmeAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'descricao', 'ano_lancamento', 'genero', 'duracao']  # colunas na listagem
  search_fields = ['titulo', 'descricao'] # campos pesquisáveis
  list_filter = ['ano_lancamento', 'genero'] # filtros laterais


admin.site.register(Token)
