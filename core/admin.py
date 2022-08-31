from django.contrib import admin

from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoas', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permisssions')}),
        ('Datas Impostantes', {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(Morador)
class MoradoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'endereco', 'data', 'sexo', 'modificado', 'ativo')

@admin.register(FichaRegistros)
class FichaRegistroAdmin(admin.ModelAdmin):
    list_display = ('id', 'naturalidade', 'descricao', 'tempRua', 'porque','residen', 'local', 'documento', 'documentos','familia', 'ondeFami', 'composta', 'outrosFami','vacinado', 'vacinas', 'dose', 'outrosVacina', 'dependente', 'drogas', 'outraDroga', 'tratamento', 'ondeTrata', 'doenca', 'qualDoenca', 'tratamentoDoenca', 'ondeTratamento','profissao', 'qualProfi', 'trabalha','emque', 'trabalhou', 'doque', 'aprender', 'alfabetisado', 'grau', 'profissionalizante', 'modificado', 'ativo')