
from django.contrib import admin
from django.urls import path
from core.views import IndexView, RegistroView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('admin/', admin.site.urls),
]
