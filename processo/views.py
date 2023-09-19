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
    fields = ['data_andamento', 'andamento', 'dias', 'data_prazo', 'funcionario', 'data_recebimento', 'complemento', 'arquivo_1', 'arquivo_2', 'arquivo_3']
    success_url = reverse_lazy('proc-adm-list')

    # Busca a pk do processo na url e preenche o atributo 'processo_id', para vincular o processo ao andamento
    def form_valid(self, form):
        pk_processo = self.kwargs.get('pk')

        form.instance.processo_id = pk_processo
        form.instance.criador_andamento_adm = self.request.user # Função para preencher o atributo 'criador_andamento_adm' com o ID do usuário logado antes do formulário ser salvo.
        return super().form_valid(form) 
    
    # Após realizar o create do andamento com sucesso, reverte para a lista de andamentos do processo 
    # def get_success_url(self):
    #     processo_pk = self.kwargs.get('pk') # Pega a PK do processo através da URL       

    #     return reverse('proc-adm-list', args=[processo_pk])

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

class AndamentoAdmList(ListView):
    model = ProcessoAdm
    template_name = 'processos/lists/andamento_adm_list.html'
    
    def get_queryset(self):
        pk_processo = self.kwargs.get('pk') # Pega a pk(primary key) da URL, pk do processo
        
        processo = ProcessoAdm.objects.get(pk=pk_processo)  # Pega o processo que possui a pk recebida (pk é a primary key do processo)
        andamentos = processo.andamentoadm_set.all()  # Pega todos os atributos do andamento
    
        return andamentos