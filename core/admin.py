from django.contrib import admin

from .models import Cargo, Servico, Funcionario


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoADmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')



@admin.register(Funcionario)
class FuncionarioADmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')