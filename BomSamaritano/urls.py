
from django.contrib import admin
from django.urls import path
from core.views import IndexView, Registrar,Formulario

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registro/', Registrar, name='registro'),
    path('form1/', Formulario, name='form1'),
    path('admin/', admin.site.urls),
]
