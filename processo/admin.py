from django.contrib import admin

from .models import ProcessoAdm

@admin.register(ProcessoAdm)
class ProcessoAdmAdmin(admin.ModelAdmin):
    list_display = ('numero', '_usuario_criador')
    exclude = ['usuario_criador',]

    # É uma edição do atributo usuario_criador, para mostrar o nome completo do usuário e não somente o username, no painel admin.
    def _usuario_criador(self, instance): 
        return f'{instance.usuario_criador.get_full_name()}'
    
    #------------------------------------------------------------------------#
    # Busca no banco de dados, apenas os registros gerados pelo usuario_criador que estiver logado no sistema, assim somente o criador do processo consegue visualizar o mesmo.
    def get_queryset(self, request): 
        qs = super(ProcessoAdmAdmin, self).get_queryset(request) 
        return qs.filter(usuario_criador=request.user)
    
    def save_model(self, request, obj, form, change):
        obj.usuario_criador = request.user  
        super().save_model(request, obj, form, change)
    #------------------------------------------------------------------------#