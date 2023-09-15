from django.contrib import admin

from .models import ProcessoAdm

@admin.register(ProcessoAdm)
class ProcessoAdmAdmin(admin.ModelAdmin):
    list_display = ('numero', '_criador_processo_adm')
    exclude = ['criador_processo_adm',]

    # É uma edição do atributo usuario_criador, para mostrar o nome completo do usuário e não somente o username, no painel admin.
    def _criador_processo_adm(self, instance): 
        return f'{instance.criador_processo_adm.get_full_name()}'
    
    #------------------------------------------------------------------------#
    # Busca no banco de dados, apenas os registros gerados pelo criador_processo_adm que estiver logado no sistema, assim somente o criador do processo consegue visualizar o mesmo.
    def get_queryset(self, request): 
        qs = super(ProcessoAdmAdmin, self).get_queryset(request) 
        return qs.filter(criador_processo_adm=request.user)
    
    def save_model(self, request, obj, form, change):
        obj.criador_processo_adm = request.user  
        super().save_model(request, obj, form, change)
    #------------------------------------------------------------------------#