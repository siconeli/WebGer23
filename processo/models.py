from django.db import models

from django.contrib.auth import get_user_model

class Base(models.Model): # Classe base, será herdada pelas outras classes
    data_criacao = models.DateField('data_criação', auto_now_add=True)
    data_alteracao = models.DateField('Alterado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class ProcessoAdm(Base):

    ufs = (
        ('MS', 'MS'), ('MT', 'MT'), ('SP', 'SP'), ('RJ', 'RJ'),
    )

    municipios = (
        ('Selvíria', 'Selvíria'), ('Inocência', 'Inocência'),
    )

    tipo_pessoas = (
        ('Física', 'Física'), ('Jurídica', 'Jurídica'),
    )

    criador_processo_adm = models.ForeignKey(get_user_model(), verbose_name='Usuário Criador', on_delete=models.CASCADE) # Usuário que criou o processo, utilizando chave primária com o get_user_model do django, para utilizar o usuário logado automaticamente
    numero = models.CharField(unique=True, verbose_name='N°', max_length=10) # Número do processo
    municipio = models.CharField(max_length=50, choices=municipios, verbose_name='Município') # Município
    uf = models.CharField(max_length=2, choices=ufs) # UF 
    data_inicial = models.DateField(blank=True, null=True) # Data Inicial do Período do processo
    data_final = models.DateField(blank=True, null=True) # Data final do Período do processo
    data_div_ativa = models.DateField(blank=True, null=True) # Data dívida ativa
    valor_atributo = models.CharField(max_length=14, blank=True, null=True)  # Valor do atributo
    valor_multa = models.CharField(max_length=14, blank=True, null=True) # Valor da multa
    valor_credito = models.CharField(max_length=14, blank=True, null=True) # Valor do crédito
    valor_atualizado = models.CharField(max_length=14, blank=True, null=True) # Valor do atualizado
    data_valor_atualizado = models.DateField(blank=True, null=True) # Data valor atualizado
    nome_contribuinte = models.CharField(max_length=50)  # Nome / Razão Social
    tipo_pessoa = models.CharField(max_length=50, choices=tipo_pessoas) # Física / Jurídica
    documento = models.CharField(max_length=20, verbose_name='CPF/CNPJ', unique=True) # CPF / CNPJ
    nome_fantasia = models.CharField(max_length=50, blank=True, null=True) # Nome Fantasia
    email = models.EmailField(max_length=50, blank=True, null=True) # E-mail
    endereco = models.CharField(max_length=150) # Rua
    complemento = models.CharField(max_length=50, blank=True, null=True) # Complemento
    municipio_contribuinte = models.CharField(max_length=50, blank=True, null=True) # Município Contribuinte
    uf_contribuinte = models.CharField(max_length=2, choices=ufs, verbose_name='UF', blank=True, null=True) # UF Contribuinte
    cep = models.CharField(max_length=10, blank=True, null=True) # CEP
    telefone = models.CharField(max_length=20, blank=True, null=True) # Telefone
    celular = models.CharField(max_length=20, blank=True, null=True) # Celular

    def __str__(self):
        return f'{self.numero}'
    
class AndamentoAdm(Base):

    andamentos = (
    ('Abertura', 'Abertura'), ('Parecer Fiscal', 'Parecer Fiscal'), ('Decisão 1ª Instância', 'Decisão 1ª Instância'), ('Suspenso Para Fiscalização Futura', 'Suspenso Para Fiscalização Futura'), ('Auto de Infração e Termo de Intimação - AITI.', 'Auto de Infração e Termo de Intimação - AITI.'), ('Termo de Intimação Fiscal - TIF.-tif.', 'Termo de Intimação Fiscal - TIF.'), ('Decisão de 2ª Instância', 'Decisão de 2ª Instância'), ('Cobrança de Documentação', 'Cobrança de Documentação'), ('Recurso Voluntário', 'Recurso Voluntário'), ('Fim do Contrato com a Assessoria', 'Fim do Contrato com a Assessoria'), ('Manifestação', 'Manifestação'), ('Recebimento do AR', 'Recebimento do AR'), ('Despacho', 'Despacho'), ('Aguardando Pagamento', 'Aguardando Pagamento'), ('Apresentação de Documentação para Análise', 'Apresentação de Documentação para Análise'), ('Aguardando AR', 'Aguardando AR'), ('Ofício', 'Ofício'), ('Revelia', 'Revelia'), ('Execução', 'Execução'), ('Confissão de Dívida (Parcelamento)', 'Confissão de Dívida (Parcelamento)'), ('Reenvio de Documento', 'Reenvio de Documento'), ('Parecer Juridico', 'Parecer Juridico'), ('Certidão', 'Certidão'), ('Encaminhado', 'Encaminhado'),
    )

    criador_andamento_adm = models.ForeignKey(get_user_model(), verbose_name='Usuário Criador', on_delete=models.CASCADE)
    processo = models.ForeignKey(ProcessoAdm, on_delete=models.CASCADE) # Relacionamento 'One to Many (um para muitos)'
    data_andamento = models.DateField(verbose_name='Data do Andamento')
    andamento = models.CharField(max_length=100, choices=andamentos, verbose_name='Andamento')
    dias = models.IntegerField(blank=True, null=True)
    data_prazo = models.DateField(blank=True, null=True)
    funcionario = models.CharField(max_length=50, blank=True, null=True)
    data_recebimento = models.DateField(blank=True, null=True)
    complemento = models.CharField(max_length=150, blank=True, null=True)
    arquivo_1 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True) 
    arquivo_2 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)
    arquivo_3 = models.FileField(upload_to='uploads/', verbose_name='Arquivo', blank=True)

    def __str__(self):
        return f'Processo: {self.processo} Andamento: {self.andamento} Arquivo: {self.arquivo_1} Arquivo: {self.arquivo_2} Arquivo: {self.arquivo_3}'

