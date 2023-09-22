from django.urls import path

from .views import ProcessoAdmView

from .views import ProcessoAdmCreate
from .views import AndamentoAdmCreate

from .views import ProcessoAdmUpdate
from .views import AndamentoAdmUpdate

from .views import ProcessoAdmDelete
from .views import AndamentoAdmDelete

from .views import ProcessoAdmList
from .views import AndamentoAdmList
from .views import ArquivoAndamentoAdmList

urlpatterns = [

    ###### VIEW ######
    path('visualizar/processo-adm/<int:pk>/', ProcessoAdmView.as_view(), name='proc-adm-view'),

    ###### CREATE ######
    path('cadastrar/processo-adm/', ProcessoAdmCreate.as_view(), name='proc-adm-create'), 
    path('cadastrar/andamento-adm/<int:pk>/', AndamentoAdmCreate.as_view(), name='andamento-adm-create'),

    ###### UPDATE ######
    path('editar/processo-adm/<int:pk>/', ProcessoAdmUpdate.as_view(), name='proc-adm-update'),
    path('editar/andamento-adm/<int:pk>/', AndamentoAdmUpdate.as_view(), name='andamento-adm-update'),

    ###### DELETE ######
    path('deletar/processo-adm/<int:pk>/', ProcessoAdmDelete.as_view(), name='proc-adm-delete'),
    path('deletar/andamento-adm/<int:pk>/', AndamentoAdmDelete.as_view(), name='andamento-adm-delete'),

    ###### LIST ######
    path('listar/processo-adm/', ProcessoAdmList.as_view(), name='proc-adm-list'),
    path('listar/andamento-adm/<int:pk>', AndamentoAdmList.as_view(), name='andamento-adm-list'),
    path('listar/arquivo-andamento-adm/<int:pk>/', ArquivoAndamentoAdmList.as_view(), name='arquivo-andamento-adm-list'),
]