import pygame
import random

#inicializando o pygame
pygame.init()

#configuraçoes da tela
largura,altura =500,600
tela=pygame.display.set_mode((largura,altura))#definir largura e altura da tela
pygame.display.set_caption('Aventuras do Coletor de moedas')#Legenda do jogo

#variaveis de cor
branco=(255,255,255)
preto=(0,0,0)
amarelo=(255,223,0)

#config jogador
jogador=pygame.Rect(largura//2-25,altura-60,50,50)#tamanho e formato do jogador
velocidade=8

#config moedas
moedas=[]
for i in range(5):
    moedas.append(pygame.Rect(random.randint(0,largura-20),random.randint(-200,-20),20,20))#moedas randomizadas caindo
velocidade_moeda=3

#