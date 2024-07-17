""" AUTOMAÇÃO DE ORGANIZADOR DE ARQUIVOS PARA O COMPUTADOR """

# Temos vários exemplos de arquivos no nosso computador, pdf's, txt, csv, xml, etc.
# Vou criar um organizador para o PC, onde podemos selecionar uma pasta e organizar os arquivos dessa pasta

##############################
### Bibliotecas Essenciais ###
##############################

import os   # Manipular arquivos do computador
from tkinter.filedialog import askdirectory # Permite Selecionar um Caminho para os seus arquivos

##############################
###### Funções Projeto #######
##############################

# Abrir um Pop Up para o usuário escolher qual pasta ele quer
caminho = askdirectory(title = "Selecione uma Pasta do seu Computador")
print(caminho)  # Retorna o caminho da pasta selecionada

# Criando uma lista de arquivos pra saber quais arquivos estão no caminho
lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

# Criando um dicionário de arquivos para criar aonde vamos armazenar esses arquivos
locais = {
    "imagens": [".png", "jpg"],
    "planilhas": [".csv", ".xml", ".xmls", ".xlsx", ".xlsm"],
    "pdf's": [".pdf", ".PDF"],
    "PowerPoint" : [".ppt", ".ppxt"],
    "word": [".docx"],
    "zips": [".zip"],
    "audios e videos": [".mp4"],
    "instaladores": [".exe"],
    "arquivos iso": [".iso"]
}

# Criando a lógica de criação de pasta com os arquivos organizados
for arquivo in lista_arquivos:  # Percorrendo a lista de arquivos
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")   # Passando o local onde está o arquivo, e o nome do arquivo
    for pasta in locais:    # Percorrendo o dicionário locais
        if extensao in locais[pasta]: 
            if not os.path.exists(f"{caminho}/{pasta}"): 
                os.mkdir(f"{caminho}/{pasta}")  # Cria a pasta caso ela não exista
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")   # Renomeando com os nomes dos arquivos

print("Arquivos organizados e movidos para as respectivas pastas.")