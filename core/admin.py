from django.contrib import admin

from .models import Morador, Familia

@admin.register(Morador)
class MoradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'endereco', 'data', 'modificado', 'ativo')

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id', 'familia', 'tempo', 'usuario', 'modificado', 'ativo')