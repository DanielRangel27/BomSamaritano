
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registro/', Registrar, name='registro'),
    path('form1/', Formulario, name='form1'),
    path('informacoes/<int:id>', telabuscaView, name='informacoes'),
    path('busca/', telabusca, name='busca'),
    path('teste/<int:id>', telabuscaView, name='teste'),
    path('admin/', admin.site.urls),
    path('editar/ficha/<int:pk>', FichaUpdate.as_view(),name='editar-ficha'),
    path('editar/morador/<int:pk>', MoradorUpdate.as_view(),name='editar-morador'),
    path('excluir/ficha/<int:pk>', FichaDelete.as_view(),name='deletar-ficha'),
    path('excluir/morador/<int:pk>', MoradorDelete.as_view(),name='deletar-morador'),
]
admin.site.site_header = 'Bom Samaritano'
admin.site.site_title = 'Bom Samaritano'
admin.site.index_title = 'Gerenciamento Bom Samaritano'