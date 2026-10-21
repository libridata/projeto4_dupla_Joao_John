from django.contrib import admin       # painel administrativo do Django   
from django.urls import path, include    # path para rotas, include para incluir outras URLs 
from rest_framework.routers import DefaultRouter  # router que gera rotas para ViewSets
from filmes.views import FilmesViewSet, GenerosViewSet # ViewSets registrados no router
from rest_framework.authtoken.views import obtain_auth_token # view para obter token de autenticação


router = DefaultRouter()
router.register(r'generos', GenerosViewSet)  # registra endpoints para generos: /api/generos/
router.register(r'filmes', FilmesViewSet)   # registra endpoints para filmes: /api/filmes/


urlpatterns = [
   path('admin/', admin.site.urls),           # rota do Django admin
   path('api/', include(router.urls)),        # inclui rotas geradas pelo router sob o prefixo /api/
   path('api/token/', obtain_auth_token),      # POST com username e password

]
