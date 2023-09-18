from .models import ProcessoAdm, AndamentoAdm

from django.views.generic.edit import CreateView, UpdateView, DeleteView # Módulo para criar, atualizar e deletar

from django.views.generic.list import ListView # Módulo para listar

from django.urls import reverse, reverse_lazy

###### CREATE ######
class ProcessoAdmCreate(CreateView):
    model = ProcessoAdm
    template_name = 'processos/creates/processo_adm_create.html'
    fields = ['numero', 'municipio', 'uf', 'data_inicial', 'data_final', 'data_div_ativa', 'valor_atributo', 'valor_multa', 'valor_credito', 'valor_atualizado', 'data_valor_atualizado', 'nome_contribuinte', 'tipo_pessoa', 'documento', 'nome_fantasia', 'email', 'endereco', 'complemento', 'municipio_contribuinte', 'uf_contribuinte', 'cep', 'telefone', 'celular']
    success_url = reverse_lazy('proc-adm-list')
    
    # Função para preencher o atributo 'criador_processo_adm' com o ID do usuário logado antes do formulário ser salvo.
    def form_valid(self, form):
        form.instance.criador_processo_adm = self.request.user
        return super().form_valid(form)  

class AndamentoAdmCreate(CreateView):  
    model = AndamentoAdm
    template_name = 'processos/creates/andamento_adm_create.html'

    def form_valid(self, form):
        form.instance.processo = self.request.user
        return super().form_valid(form) 

###### UPDATE ######
class ProcessoAdmUpdate(UpdateView):
    model = ProcessoAdm
    template_name = 'processos/updates/processo_adm_update.html'
    fields = ['municipio', 'uf', 'data_inicial', 'data_final', 'data_div_ativa', 'valor_atributo', 'valor_multa', 'valor_credito', 'valor_atualizado', 'data_valor_atualizado', 'nome_contribuinte', 'tipo_pessoa', 'documento', 'nome_fantasia', 'email', 'endereco', 'complemento', 'municipio_contribuinte', 'uf_contribuinte', 'cep', 'telefone', 'celular']
    success_url = reverse_lazy('proc-adm-list')

###### DELETE ######
class ProcessoAdmDelete(DeleteView):
    model = ProcessoAdm
    template_name = 'processos/deletes/processo_adm_delete.html'
    success_url = reverse_lazy('proc-adm-list')

###### LIST ######
class ProcessoAdmList(ListView):
    model = ProcessoAdm
    template_name = 'processos/lists/processo_adm_list.html'
    