from django.contrib import admin

from .models import *

@admin.register(Morador)
class MoradoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'endereco', 'data', 'sexo', 'modificado', 'ativo')

"""@admin.register(Origem)
class OrigemAdmin(admin.ModelAdmin):
    list_display = ('id', 'naturalidade', 'descricao', 'tempRua', 'porque', 'modificado', 'ativo')

@admin.register(Residencia)
class ResidenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'residen', 'local', 'modificado', 'ativo')

@admin.register(Identificacao)
class IdentificacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'documento', 'documentos', 'modificado', 'ativo')

@admin.register(Familiares)
class FamiliaresAdmin(admin.ModelAdmin):
    list_display = ('id', 'familia', 'onde', 'composta', 'outros', 'modificado', 'ativo')

@admin.register(Saude)
class SaudeAdmin(admin.ModelAdmin):
    list_display = ('id', 'vacinado', 'vacinas', 'dose', 'outros', 'dependente', 'drogas', 'outra', 'tratamento', 'ondeTrata', 'doenca', 'qual', 'tratamentoDoenca', 'onde', 'modificado', 'ativo')

@admin.register(Religiao)
class ReligiaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'crenca', 'religiosidade', 'modificado', 'ativo')

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'profissao', 'qual', 'trabalha','emque', 'trabalhou', 'doque', 'aprender', 'modificado', 'ativo')

@admin.register(Escolaridade)
class EscolaridadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'alfabetisado', 'grau', 'profissionalizante', 'modificado', 'ativo')
"""
@admin.register(FichaRegistros)
class FichaRegistroAdmin(admin.ModelAdmin):
    list_display = ('id', 'naturalidade', 'descricao', 'tempRua', 'porque','residen', 'local', 'documento', 'documentos','familia', 'ondeFami', 'composta', 'outrosFami','vacinado', 'vacinas', 'dose', 'outrosVacina', 'dependente', 'drogas', 'outraDroga', 'tratamento', 'ondeTrata', 'doenca', 'qualDoenca', 'tratamentoDoenca', 'ondeTratamento','profissao', 'qualProfi', 'trabalha','emque', 'trabalhou', 'doque', 'aprender', 'alfabetisado', 'grau', 'profissionalizante', 'modificado', 'ativo')