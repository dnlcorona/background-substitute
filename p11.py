# Feito com ♥ por Daniel Corona
import imagens
import numpy as np


imagemUtilizada1 = 'vicenteVega.jpg'
imagemUtilizada2 = 'UFV.jpg'
im = imagens.Imagem(f'C:/Users/danie/Documents/VSCODE/PROJETOS/ATIVIDADES/CK/{imagemUtilizada1}')
im2 = imagens.Imagem(f'C:/Users/danie/Documents/VSCODE/PROJETOS/ATIVIDADES/CK/{imagemUtilizada2}')

im.mostrar()
im2.mostrar()

for i in range(0, im.altura):
    for j in range(0, im.largura):
        if im[i][j] == (0,255,1):   
            im[i][j] = im2[i][j]

im.mostrar()