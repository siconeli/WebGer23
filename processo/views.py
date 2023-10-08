from .models import ProcessoAdm, AndamentoAdm, Auditoria

from django.views.generic.edit import CreateView, UpdateView, DeleteView # Módulo para create, update e delete

from django.views.generic.list import ListView # Módulo para list

from django.views.generic import TemplateView

from django.urls import reverse, reverse_lazy # Módulo para reverter para a url definida após ter sucesso na execução

import logging # Módulo para criar logs

import datetime # Módulo para datas

import os # Módulo para trabalhar com pastas e arquivos

from docx2pdf import convert # Módulo para converter .docx em pdf

from django.core.exceptions import ValidationError

import pythoncom

###### VIEW ######
class ProcessoAdmView(TemplateView):
    template_name = 'processos/views/processo_adm_view.html'

    # Função para iterar com os dados do processo
    def get_context_data(self, **kwargs):
        processo_pk = self.kwargs.get('pk') # Pega a PK do processo através da URL  

        context = super().get_context_data(**kwargs)
        context['dados_processo'] = ProcessoAdm.objects.filter(pk=processo_pk) # Filtra os dados do processo através da pk
        return context
    
class AndamentoAdmView(TemplateView):
    template_name ='processos/views/andamento_adm_view.html'

     #  Função para reverter para a url 'andamento-adm-list' passando a pk do processo para conseguir voltar para a tela de lista de andamentos do processo.
    def get_voltar(self, processo_pk):
        return reverse('andamento-adm-list-update', args=[processo_pk])

    # Função para funcionalidade do botão 'voltar'
    # Função para buscar a pk do processo e salvar na variável 'processo_pk', com a funcionalidade do get_context_data envia para o Template o contexto 'cancelar' que recebe a função 'get_cancelar' junto com a variavel 'processo_pk'.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        andamento_pk = self.kwargs.get('pk') # Pega a PK do andamento ao fazer o update através da URL
        andamento = AndamentoAdm.objects.get(pk=andamento_pk) # Busca o andamento através da PK do andamento
        processo_pk = andamento.processo_id # Busca a PK do processo através do andamento (processo_id é a ForeignKey entre o processo administrativo e o andamento)

        context['voltar'] = self.get_voltar(processo_pk)
        context['dados_andamento'] = AndamentoAdm.objects.filter(pk=andamento_pk) # Filtra os dados do andamento através da pk, para conseguir iterar com os dados do andamento

        return context

###### CREATE ######
class ProcessoAdmCreate(CreateView):
    model = ProcessoAdm
    template_name = 'processos/creates/processo_adm_create.html'
    fields = ['numero', 'municipio', 'uf', 'data_inicial', 'data_final', 'data_div_ativa', 'valor_atributo', 'valor_multa', 'valor_credito', 'valor_atualizado', 'data_valor_atualizado', 'nome_contribuinte', 'tipo_pessoa', 'documento', 'nome_fantasia', 'email', 'endereco', 'complemento', 'municipio_contribuinte', 'uf_contribuinte', 'cep', 'telefone', 'celular']
    success_url = reverse_lazy('proc-adm-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        result = super().form_valid(form)
        
        # Registre a operação de criação na auditoria
        Auditoria.objects.create(
            usuario = self.request.user,
            nome_model = ProcessoAdm,
            id_novo_registro = self.object.id,
            acao='Create',
            )
        
        return result

class AndamentoAdmCreate(CreateView):  
    model = AndamentoAdm
    template_name = 'processos/creates/andamento_adm_create.html'
    fields = ['data_andamento', 'tipo_andamento', 'situacao_pagamento', 'valor_pago', 'data_prazo', 'data_recebimento', 'complemento', 'arquivo']
    success_url = reverse_lazy('proc-adm-list')

    def form_valid(self, form):
        """
            A função form_valid() serve para alterar os valores do atributo ou realizar qualquer ação antes que o formulário seja salvo.
        """
        pk_processo = self.kwargs.get('pk')
        form.instance.processo_id = pk_processo

        # Preencher o atributo 'criador_andamento_adm' com o ID do usuário logado.
        form.instance.criador_andamento_adm = self.request.user 

        # Preencher o atributo 'funcionario' com o nome completo do usuário logado.
        form.instance.funcionario = self.request.user.get_full_name()

        pythoncom.CoInitialize() # Para não ocorrer o erro  "Exception Value:(-2147221008, 'CoInitialize não foi chamado.', None, None)" quando utilizado código para converter arquivos
        # Código para conversão do arquivo enviado, de .docx(word) para .pdf
        # Antes de salvar o formulário, verifica se um arquivo Word foi enviado
        if 'arquivo' in self.request.FILES:
            arquivo = self.request.FILES['arquivo']
            print(arquivo)
            
            if arquivo.name.endswith('.docx'): # Se o arquivo termina com '.docx'
                # Cria um arquivo temporário para a conversão
                word_temporario = os.path.join('media/Arquivo', arquivo.name)
                with open(word_temporario, 'wb') as arquivo_temporario:
                    for chunk in arquivo.chunks():
                        arquivo_temporario.write(chunk)

                # Converte o arquivo Word para PDF
                pdf_temporario = word_temporario.replace('.docx', '.pdf')
                convert(word_temporario, pdf_temporario)

                # Abra o arquivo PDF convertido e atualize o campo 'arquivo' no formulário
                with open(pdf_temporario, 'rb') as pdf:
                    form.instance.arquivo.save(pdf_temporario, pdf)

                # Certifique-se de que o arquivo Word temporário seja excluído
                os.remove(word_temporario)

                # Certifique-se de que o arquivo PDF temporário seja excluído
                os.remove(pdf_temporario)
                
        pythoncom.CoUninitialize() # Para não ocorrer o erro "Exception Value:(-2147221008, 'CoInitialize não foi chamado.', None, None)" quando utilizado códigos para converter arquivos

        return super().form_valid(form)
    
    # Após realizar o create do andamento com sucesso, reverte para a lista de andamentos do processo 
    def get_success_url(self):
        processo_pk = self.kwargs.get('pk') # Pega a PK do processo através da URL       

        return reverse('andamento-adm-list', args=[processo_pk])
    
    # Função para iterar com os dados do processo na view de create andamento
    def get_context_data(self, **kwargs):
        processo_pk = self.kwargs.get('pk') # Pega a PK do processo através da URL  

        context = super().get_context_data(**kwargs)
        context['dados_processo'] = ProcessoAdm.objects.filter(pk=processo_pk) # Filtra os dados do processo através da pk
        return context
    
###### UPDATE ######
class ProcessoAdmUpdate(UpdateView):
    model = ProcessoAdm
    template_name = 'processos/updates/processo_adm_update.html'
    fields = ['municipio', 'uf', 'data_inicial', 'data_final', 'data_div_ativa', 'valor_atributo', 'valor_multa', 'valor_credito', 'valor_atualizado', 'data_valor_atualizado', 'nome_contribuinte', 'tipo_pessoa', 'documento', 'nome_fantasia', 'email', 'endereco', 'complemento', 'municipio_contribuinte', 'uf_contribuinte', 'cep', 'telefone', 'celular']
    success_url = reverse_lazy('proc-adm-list')

    # Função para iterar com os dados do processo na view de update processo
    def get_context_data(self, **kwargs):
        processo_pk = self.kwargs.get('pk') # Pega a PK do processo através da URL  

        context = super().get_context_data(**kwargs)
        context['dados_processo'] = ProcessoAdm.objects.filter(pk=processo_pk) # Filtra os dados do processo através da pk
        return context
    
class AndamentoAdmUpdate(UpdateView):
    model = AndamentoAdm
    template_name = 'processos/updates/andamento_adm_update.html'
    fields = ['data_andamento', 'tipo_andamento', 'situacao_pagamento','valor_pago', 'data_prazo', 'data_recebimento', 'complemento', 'arquivo']

    # Após realizar o update com sucesso, reverte para a lista de andamentos do processo
    def get_success_url(self):
        andamento_pk = self.kwargs.get('pk') # Pega a PK do andamento ao fazer o update através da URL
        andamento = AndamentoAdm.objects.get(pk=andamento_pk) # Busca o andamento através da PK do andamento
        processo_pk = andamento.processo_id # Busca a PK do processo através do andamento (processo_id é a ForeignKey entre o processo administrativo e o andamento)

        return reverse('andamento-adm-list-update', args=[processo_pk]) # URL da lista de andamentos + pk do processo 
    
    #  Função para reverter para a url 'andamento-adm-list' passando a pk do processo para conseguir voltar para a tela de lista de andamentos do processo.
    def get_cancelar(self, processo_pk):
        return reverse('andamento-adm-list-update', args=[processo_pk])

    # Função para funcionalidade do botão 'Cancelar'
    # Função para buscar a pk do processo e salvar na variável 'processo_pk', com a funcionalidade do get_context_data envia para o Template o contexto 'cancelar' que recebe a função 'get_cancelar' junto com a variavel 'processo_pk'.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        andamento_pk = self.kwargs.get('pk') # Pega a PK do andamento ao fazer o update através da URL
        andamento = AndamentoAdm.objects.get(pk=andamento_pk) # Busca o andamento através da PK do andamento
        processo_pk = andamento.processo_id # Busca a PK do processo através do andamento (processo_id é a ForeignKey entre o processo administrativo e o andamento)

        context['cancelar'] = self.get_cancelar(processo_pk)
        context['dados_andamento'] = AndamentoAdm.objects.filter(pk=andamento_pk) # Filtra os dados do andamento através da pk, para conseguir iterar com os dados do andamento

        return context
    
    def form_valid(self, form):
        """
            A função form_valid() serve para alterar os valores do atributo ou realizar qualquer ação antes que o formulário seja salvo.
        """
        pythoncom.CoInitialize() # Para não ocorrer o erro  "Exception Value:(-2147221008, 'CoInitialize não foi chamado.', None, None)" quando utilizado código para converter arquivos
        # Código para conversão do arquivo enviado, de .docx(word) para .pdf
        # Antes de salvar o formulário, verifica se um arquivo Word foi enviado
        if 'arquivo' in self.request.FILES:
            arquivo = self.request.FILES['arquivo']
            print(arquivo)
            
            if arquivo.name.endswith('.docx'): # Se o arquivo termina com '.docx'
                # Cria um arquivo temporário para a conversão
                word_temporario = os.path.join('media/Arquivo', arquivo.name)
                with open(word_temporario, 'wb') as arquivo_temporario:
                    for chunk in arquivo.chunks():
                        arquivo_temporario.write(chunk)

                # Converte o arquivo Word para PDF
                pdf_temporario = word_temporario.replace('.docx', '.pdf')
                convert(word_temporario, pdf_temporario)

                # Abra o arquivo PDF convertido e atualize o campo 'arquivo' no formulário
                with open(pdf_temporario, 'rb') as pdf:
                    form.instance.arquivo.save(pdf_temporario, pdf)

                # Certifique-se de que o arquivo Word temporário seja excluído
                os.remove(word_temporario)

                # Certifique-se de que o arquivo PDF temporário seja excluído
                os.remove(pdf_temporario)
                
                pythoncom.CoUninitialize() # Para não ocorrer o erro "Exception Value:(-2147221008, 'CoInitialize não foi chamado.', None, None)"

        return super().form_valid(form)

###### DELETE ######
class ProcessoAdmDelete(DeleteView):
    model = ProcessoAdm
    template_name = 'processos/deletes/processo_adm_delete.html'
    success_url = reverse_lazy('proc-adm-list')

    # Função para iterar com os dados do processo na view de delete processo
    def get_context_data(self, **kwargs):
        processo_pk = self.kwargs.get('pk') # Pega a PK do processo através da URL  

        context = super().get_context_data(**kwargs)
        context['dados_processo'] = ProcessoAdm.objects.filter(pk=processo_pk) # Filtra os dados do processo através da pk
        return context  

class AndamentoAdmDelete(DeleteView):
    model = AndamentoAdm
    template_name = 'processos/deletes/andamento_adm_delete.html'

    # Após realizar o delete com sucesso, reverte para a lista de andamentos do processo
    def get_success_url(self):
        andamento_pk = self.kwargs.get('pk') # Pega a PK do andamento ao fazer o update através da URL
        andamento = AndamentoAdm.objects.get(pk=andamento_pk) # Busca o andamento através da PK do andamento
        processo_pk = andamento.processo_id # Busca a PK do processo através do andamento (processo_id é a ForeignKey entre o processo administrativo e o andamento)

        return reverse('andamento-adm-list-update', args=[processo_pk]) # URL da lista de andamentos + pk do processo
    
    # Função para iterar com os dados do andamento na view de delete andamento
    def get_context_data(self, **kwargs):
        andamento_pk = self.kwargs.get('pk') # Pega a PK do andamento através da URL  

        context = super().get_context_data(**kwargs)
        context['dados_andamento'] = AndamentoAdm.objects.filter(pk=andamento_pk) # Filtra os dados do andamento através da pk
        return context

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
    
    # Função para iterar com os dados do processo na lista de andamentos
    def get_context_data(self, **kwargs):
        processo_pk = self.kwargs.get('pk') # Pega a PK do processo através da URL  

        context = super().get_context_data(**kwargs)
        context['dados_processo'] = ProcessoAdm.objects.filter(pk=processo_pk) # Filtra os dados do processo através da pk
        return context

class AndamentoAdmListUpdate(ListView):
    model = ProcessoAdm
    template_name = 'processos/lists/andamento_adm_list_update.html'
    
    def get_queryset(self):
        pk_processo = self.kwargs.get('pk') # Pega a pk(primary key) da URL, pk do processo
        
        processo = ProcessoAdm.objects.get(pk=pk_processo)  # Pega o processo que possui a pk recebida (pk é a primary key do processo)
        andamentos = processo.andamentoadm_set.all()  # Pega todos os atributos do andamento
    
        return andamentos
    
    # Função para iterar com os dados do processo na lista de andamentos
    def get_context_data(self, **kwargs):
        processo_pk = self.kwargs.get('pk') # Pega a PK do processo através da URL  

        context = super().get_context_data(**kwargs)
        context['dados_processo'] = ProcessoAdm.objects.filter(pk=processo_pk) # Filtra os dados do processo através da pk
        return context

    

