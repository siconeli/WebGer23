from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AndamentoAdm

import os # Módulo para trabalhar com pastas e arquivos

from docx2pdf import convert # Módulo para converter .docx em pdf

@receiver(post_save, sender=AndamentoAdm)

def conversorPdf(sender, instance, **kwargs):
        """
            Converter arquivos com formato '.docx' para formato '.pdf', remover o antigo arquivo '.docx' e atualizar o nome do arquivo na coluna do banco de dados para que busque o novo arquivo corretamente. (Ass. Siconeli)
        """
        nome_arquivo = instance.arquivo.name # Nome do arquivo em 'str'
        
        nome_arquivo_coversao = nome_arquivo[8:]

        caminho = 'media/Arquivo'
        lista_arquivos = os.listdir(caminho) # Todos os arquivos dentro do caminho
        for arquivo in lista_arquivos:
            if arquivo == nome_arquivo_coversao:  
                convert(f'media/Arquivo/{arquivo}') # Converte para PDF

        for arquivo in lista_arquivos:
                if '.docx' in arquivo:
                    os.remove(f'media/Arquivo/{arquivo}') # Remove o antigo arquivo com formato .docx  
        
        # if '.docx' in nome_arquivo:
        #     nome_formato_pdf = f'{nome_arquivo[:-5]}.pdf'
        #     print(nome_formato_pdf)
        #     instance.arquivo.name = nome_formato_pdf
        #     instance.save()



