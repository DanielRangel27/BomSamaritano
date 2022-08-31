
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

]
admin.site.site_header = 'Bom Samaritano'
admin.site.site_title = 'Bom Samaritano'
admin.site.index_title = 'Gerenciamento Bom Samaritano'