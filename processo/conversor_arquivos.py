import os # Módulo para trabalhar com pastas e arquivos

from docx2pdf import convert # Módulo para converter .docx em pdf

from time import sleep

caminho = 'media/Arquivo'

lista_arquivos = os.listdir(caminho) # Todos os arquivos dentro do caminho

for arquivo in lista_arquivos:
    nome_arquivo = os.path.basename(arquivo) # Nome do arquivo
    if nome_arquivo[-5:] == '.docx':  # Se arquivo possuir formato .docx ira converter para pdf
        convert(f'media/Arquivo/{nome_arquivo}')
        sleep(10)
        os.remove(f'media/Arquivo/{nome_arquivo}') # Remove o antigo arquivo com formato .docx   
    








