from django.db import models

from django.contrib.auth import get_user_model

class Base(models.Model): # Classe base, será herdada pelas outras classes
    criado = models.DateField('Criado', auto_now_add=True)
    alterado = models.DateField('Alterado', auto_now=True)
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

    usuario_criador = models.ForeignKey(get_user_model(), verbose_name='Usuário Criador', on_delete=models.CASCADE) # Usuário que criou o processo, utilizando chave primária com o get_user_model do django, para utilizar o usuário logado automaticamente
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