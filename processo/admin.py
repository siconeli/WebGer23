from django.contrib import admin

from .models import TipoAndamentoAdm

# @admin.register(ProcessoAdm) # Para mostrar meu modelo ProcessoAdm no Django-Admin (o código está comentado para os dados do ProcessoAdm não aparecer no Django-Admin, pois o Django-Admin será usado apenas para o Super Usuário alterar senhas de usuário ou criar novos usuários)
# class ProcessoAdmAdmin(admin.ModelAdmin):
#     list_display = ('numero',)

@admin.register(TipoAndamentoAdm)
class TipoAndamentoAdmAdmin(admin.ModelAdmin):
    list_display = ('tipo_andamento',)