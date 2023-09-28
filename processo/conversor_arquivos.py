import os

from docx2pdf import convert # Módulo para converter .docx em pdf

caminho = 'media/Arquivo'

lista_arquivos = os.listdir(caminho) # Todos os arquivos dentro do caminho

for arquivo in lista_arquivos:
    nome_arquivo = os.path.basename(arquivo) # Nome do arquivo
    if nome_arquivo[-5:] == '.docx':
        convert(f'media/Arquivo/{nome_arquivo}')
    else:
        print('- Arquivo com outro formato, não foi possível converter')
    










# for arquivo in lista_arquivos:
# convert('media/Arquivo/EU_SOU_O_CARA.docx')
    # print(arquivo)



