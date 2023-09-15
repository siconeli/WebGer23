from .models import ProcessoAdm

from django.views.generic.edit import CreateView

from django.urls import reverse, reverse_lazy



###### CREATE ######
class ProcessoAdmCreate(CreateView):
    model = ProcessoAdm
    template_name = 'processo/processo-adm-create.html'
    field = ['numero', 'municipio', 'uf', 'data_inicial', 'data_final', 'data_div_ativa', 'valor_atributo', 'valor_multa', 'valor_credito', 'valor_atualizado', 'data_valor_atualizado', 'nome_contribuinte', 'tipo_pessoa', 'documento', 'nome_fantasia', 'email', 'endereco', 'complemento', 'municipio_contribuinte', 'uf_contribuinte', 'cep', 'telefone', 'celular']
    # success_url = reverse_lazy('')


