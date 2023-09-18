from django.urls import path

from .views import ProcessoAdmCreate
# from .views import AndamentoAdmCreate

from .views import ProcessoAdmUpdate
# from .views import AndamentoAdmUpdate

# from .views import ProcessoAdmDelete
# from .views import AndamentoAdmDelete

from .views import ProcessoAdmList
# from .views import AndamentoAdmList
# from .views import ArquivoAdmList

urlpatterns = [

    ###### CREATE ######
    path('cadastrar/processo-adm/', ProcessoAdmCreate.as_view(), name='proc-adm-create'), 

    ###### UPDATE ######
    path('editar/processo-adm/', ProcessoAdmUpdate.as_view(), name='proc-adm-update'),

    ###### LIST ######
    path('listar/processo-adm/', ProcessoAdmList.as_view(), name='proc-adm-list'),

]