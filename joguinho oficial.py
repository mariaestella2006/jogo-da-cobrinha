import pygame
from pygame.locals import * 
from sys import exit
from random import randint

pygame.init()

#declaração de variáveis
#criação da tela
largura_tela = 640
altura_tela = 480
titulo = "snake game"

#informações da cobrinha
x_cobrinha = largura_tela/2
y_cobrinha = altura_tela/2
largura_cobrinha = altura_cobrinha = 20
cor_cobrinha= (127,152,86)
lista_cobrinha = []

#informações da maça
x_maca = randint(40,600)
y_maca = randint(40,440)
largura_maca = altura_maca = 20

#informações da pontuação
fonte = pygame.font.SysFont ('Arial', 20, True, False) 
pontos= 0

#informações do movimento
velocidade = 10
movimento_x = velocidade
movimento_y = 0
key_left = key_up = key_down = False
key_right= True

def reiniciar_jogo():
    global pontod, x_cobrinha, y_cobrinha, lista_cabeca, lista_cobrinha, x_maca, y_maca, perdeu, velocidade, key_down,key_left, key_right, key_up
     

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption(titulo)
relogio = pygame.time.Clock()

while True:
    tela.fill((255,255,255))
    relogio.tick(30)
    mensagem= f' Pontos: {pontos}'
    caixa_texto= fonte.render(mensagem, True, (0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type ==KEYDOWN: 
            if event.key == K_LEFT and not(key_right):
                movimento_x = -velocidade
                movimento_y= 0
                key_down = key_up = key_right = False
                key_left= True
        
            elif event.key == K_RIGHT and not(key_left):
                movimento_x = velocidade
                movimento_y = 0
                key_left = key_up = key_down = False
                key_right= True
            
            elif event.key == K_UP and not(key_down):
                movimento_x = 0
                movimento_y = -velocidade
                key_left = key_right = key_down = False
                key_up= True
            
            elif event.key == K_DOWN and not(key_up):
                movimento_x = 0
                movimento_y = velocidade
                key_left = key_up = key_right = False
                key_down= True
                
    x_cobrinha += movimento_x
    y_cobrinha += movimento_y
    
    # if pygame.key.get_pressed()[K_LEFT]:
    #     x_cobrinha -= 10
    # elif pygame.key.get_pressed()[K_RIGHT]:
    #     x_cobrinha += 10
    # elif pygame.key.get_pressed()[K_UP]:
    #     y_cobrinha -= 10
    # elif pygame.key.get_pressed()[K_DOWN]:
    #     y_cobrinha += 10
    
    cobra = pygame.draw.rect(tela, (127,152,86), (x_cobrinha, y_cobrinha, largura_cobrinha, altura_cobrinha))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, largura_maca, altura_maca))
    
    if cobra.colliderect(maca):
        x_maca = randint (40,600)
        y_maca = randint(40,440)
        pontos +=1
    
    if len(lista_cobrinha) > pontos:
        del lista_cobrinha[0]
    
    lista_cabeca = []
    lista_cabeca.append(x_cobrinha)
    lista_cabeca.append(y_cobrinha)
    
    lista_cobrinha.append(lista_cabeca)
    
    for XeY in lista_cobrinha: 
        pygame.draw.rect(tela, (127,152,86), (XeY[0], XeY[1], largura_cobrinha, altura_cobrinha))
    
    if lista_cobrinha.count(lista_cabeca) > 1:
        morreu= True
        
        while morreu:
            tela.fill ((0,0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
                        perdeu= False
                    
    if x_cobrinha > largura_tela:
        x_cobrinha = 0
    if x_cobrinha < 0:
        x_cobrinha = largura_tela
    if y_cobrinha > altura_tela:
        y_cobrinha = 0
    if y_cobrinha < 0:
        y_cobrinha = altura_tela
    
    tela.blit(caixa_texto, (480,40))
    pygame.display.update()