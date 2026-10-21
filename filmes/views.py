from rest_framework import viewsets                       # viewsets do DRF para CRUD automático
from .models import Filmes, Generos                          # modelos/tabelas usados nas views
from .serializers import FilmesSerializer, GenerosSerializer # serializers para (de)serializar os modelos
from django_filters.rest_framework import DjangoFilterBackend  # permite filtragem via query params

# ViewSet para o modelo Gêneros — fornece endpoints list/retrieve/create/update/destroy
class GenerosViewSet(viewsets.ModelViewSet):
   queryset = Generos.objects.all()         # queryset base usado pelo ViewSet
   serializer_class = GenerosSerializer     # serializer que define representação e validação

# ViewSet para o modelo Filmes — fornece endpoints CRUD e suporte a filtros
class FilmesViewSet(viewsets.ModelViewSet):
   queryset = Filmes.objects.all()         # queryset base para operações do ViewSet
   serializer_class = FilmesSerializer     # serializer usado para Filmes
   filter_backends = [DjangoFilterBackend]  # habilita filtragem via django-filter
   # campos permitidos para filtragem via query string, ex: ?titulo=titanic or ?genero=terror
   filterset_fields = ['titulo', 'ano_lancamento', 'genero', 'duracao']
