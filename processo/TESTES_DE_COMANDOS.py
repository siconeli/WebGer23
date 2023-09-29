import os # Módulo para trabalhar com pastas e arquivos

from docx2pdf import convert # Módulo para converter .docx em pdf


# def conversorPdf(self):
#         """
#             Converter arquivos com formato '.docx' para formato '.pdf', remover o antigo arquivo '.docx' e atualizar o nome do arquivo na coluna do banco de dados para que busque o novo arquivo corretamente. (Ass. Siconeli)
#         """

#         andamentos = AndamentoAdm.objects.all()

#         for andamento in andamentos:
#             caminho = 'media/Arquivo'
#             lista_arquivos = os.listdir(caminho) # Todos os arquivos dentro do caminho
#             for arquivo in lista_arquivos:
#                 if arquivo[-5:] == '.docx':  # Se arquivo possuir formato .docx, ira converter para pdf
#                     convert(f'media/Arquivo/{arquivo}')
#                     # sleep(2)
#                     os.remove(f'media/Arquivo/{arquivo}') # Remove o antigo arquivo com formato .docx   

#             nome_arquivo = andamento.arquivo.name # Nome do arquivo em 'str'

#             if nome_arquivo[-5:] == '.docx':
#                 nome_convertido = f'{nome_arquivo[:-5]}.pdf'
#                 andamento.arquivo.name = nome_convertido
#                 andamento.save()



# Alterar o nome do arquivo para final '.pdf' se o arquivo for '.docx', faz parte da conversão para PDF.
# nome_arquivo = form.instance.arquivo.name 
# if '.docx' in nome_arquivo:
#     nome_convertido = f'{nome_arquivo[:-5]}.pdf'        
#     form.instance.arquivo.name = nome_convertido
