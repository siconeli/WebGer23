import os

from docx2pdf import convert

caminho = 'media/Arquivo'

lista_arquivos = os.listdir(caminho) # Todos os arquivos dentro do caminho
print(lista_arquivos)

for arquivo in lista_arquivos:
    print(arquivo)
    nome_arquivo = os.path.basename(arquivo) # Nome do arquivo
    convert(f'media/Arquivo/{nome_arquivo}')

print(lista_arquivos)
    




# convert('media/Arquivo/TESTE.docx')





# for arquivo in lista_arquivos:
# convert('media/Arquivo/EU_SOU_O_CARA.docx')
    # print(arquivo)



