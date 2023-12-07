import pygame
from sys import exit

oi = 2
def verificacao_de_vitoria(verificacao_01, jogador_1, jogador_2):
                for i in range(0, 3):
                    if (verificacao_01[i][0] == 'zero') and (verificacao_01[i][1] == 'zero') and (verificacao_01[i][2] == 'zero'):
                        
                        return ['j1', True]
                    elif (verificacao_01[i][0] == 'xis') and (verificacao_01[i][1] == 'xis') and (verificacao_01[i][2] == 'xis'):
                        return ['j2', True]
                        
                for d in range(0, 3):
                    if (verificacao_01[0][d] == 'zero') and (verificacao_01[1][d] == 'zero') and (verificacao_01[2][d] == 'zero'):
                        return ['j1', True]

                    elif (verificacao_01[0][d] == 'xis') and (verificacao_01[1][d] == 'xis') and (verificacao_01[2][d] == 'xis'):            
                        return ['j2', True]

                if (verificacao_01[0][0] == 'zero') and (verificacao_01[1][1] == 'zero') and (verificacao_01[2][2] == 'zero'):
                    return ['j1', True]  
                        
                elif (verificacao_01[0][0] == 'xis') and (verificacao_01[1][1] == 'xis') and (verificacao_01[2][2] == 'xis'):  
                    return ['j2', True]

                if (verificacao_01[0][2] == 'zero') and (verificacao_01[1][1] == 'zero') and (verificacao_01[2][0] == 'zero'):
                    return ['j1', True]    
    
                elif (verificacao_01[0][2] == 'xis') and (verificacao_01[1][1] == 'xis') and (verificacao_01[2][0] == 'xis'): 
                    return ['j2', True]   
    
                casas_vazias = 0

                for n in range(0, 3):
                        for m in range(0, 3):
                            if verificacao_01[n][m] != ' ':
                                casas_vazias += 1

                            if casas_vazias == 9:
                                return ['empate', True]
                            
                return ['2', False]       
 
def turnos(cont, verificacao_01, x, y, tela):    
    alerta = True
    while alerta:     
        if cont % 2 == 0:

            if (x < 220) and (y < 220):
                if verificacao_01[0][0] == ' ':

                    pygame.draw.line(tela, (255, 0, 0), (20, 20), (200, 200), 20)
                    pygame.draw.line(tela, (255, 0, 0), (200, 20), (20, 200), 20)
                    verificacao_01[0][0] = 'xis'
                    alerta = False

                elif not verificacao_01[0][0] == ' ':
                     alerta = False
                
            elif (220 <= x < 440) and (y < 220):
                if verificacao_01[0][1] == ' ':
                    pygame.draw.line(tela, (255, 0, 0), (240, 20), (420, 200), 20)
                    pygame.draw.line(tela, (255, 0, 0), (420, 20), (240, 200), 20)
                    verificacao_01[0][1] = 'xis'
                    alerta = False

                elif not verificacao_01[0][1] == ' ':
                     alerta = False
                
            elif (440 <= x < 660) and (y < 220):
                if verificacao_01[0][2] == ' ':    
                    pygame.draw.line(tela, (255, 0, 0), (460, 20), (640, 200), 20)
                    pygame.draw.line(tela, (255, 0, 0), (640, 20), (460, 200), 20)
                    verificacao_01[0][2] = 'xis'
                    alerta = False
                elif not verificacao_01[0][2] == ' ':
                     alerta = False
                
            elif (x < 220) and (220 <= y < 440):
                if verificacao_01[1][0] == ' ':
                    pygame.draw.line(tela, (255, 0, 0), (20, 240), (200, 420), 20)
                    pygame.draw.line(tela, (255, 0, 0), (200, 240), (20, 420), 20)
                    verificacao_01[1][0] = 'xis'
                    alerta = False
                elif not verificacao_01[1][0] == ' ':
                     alerta = False
                
            elif (220 <= x < 440) and (220 <= y < 440):
                if verificacao_01[1][1] == ' ':
                    pygame.draw.line(tela, (255, 0, 0), (240, 240), (420, 420), 20)
                    pygame.draw.line(tela, (255, 0, 0), (420, 240), (240, 420), 20)
                    verificacao_01[1][1] = 'xis'
                    alerta = False
                elif not verificacao_01[1][1] == ' ':
                     alerta = False

            elif (440 <= x < 660) and ( 220 <= y < 440):
                if verificacao_01[1][2] == ' ':
                    pygame.draw.line(tela, (255, 0, 0), (460, 240), (640, 420), 20)
                    pygame.draw.line(tela, (255, 0, 0), (640, 240), (460, 420), 20)
                    verificacao_01[1][2] = 'xis'
                    alerta = False
                elif not verificacao_01[1][2] == ' ':
                     alerta = False 

            elif (x < 220) and ( 440 <= y < 660):
                if verificacao_01[2][0] == ' ':
                    pygame.draw.line(tela, (255, 0, 0), (20, 460), (200, 640), 20)
                    pygame.draw.line(tela, (255, 0, 0), (200, 460), (20, 640), 20)
                    verificacao_01[2][0] = 'xis'
                    alerta = False

                elif not verificacao_01[2][0] == ' ':
                     alerta = False    

            elif (220 <= x < 440) and (440 <= y < 660):
                if verificacao_01[2][1] == ' ':
                    pygame.draw.line(tela, (255, 0, 0), (240, 460), (420, 640), 20)
                    pygame.draw.line(tela, (255, 0, 0), (420, 460), (240, 640), 20)
                    verificacao_01[2][1] = 'xis'
                    alerta = False

                elif not verificacao_01[2][1] == ' ':
                     alerta = False
                        

            elif (440 <= x < 660) and (440 <= y < 660):
                if verificacao_01[2][2] == ' ':
                    pygame.draw.line(tela, (255, 0, 0), (460, 460), (640, 640), 20)
                    pygame.draw.line(tela, (255, 0, 0), (640, 460), (460, 640), 20)
                    verificacao_01[2][2] = 'xis'
                    alerta = False
                elif not verificacao_01[2][2] == ' ':
                     alerta = False    

        elif cont % 2  == 1: 

            if (x < 220) and (y < 220):
                if verificacao_01[0][0] == ' ':
                    pygame.draw.circle(tela, (0, 0, 255), (110, 110), 80)
                    verificacao_01[0][0] = 'zero'
                    alerta = False

                elif not verificacao_01[0][0] == ' ':
                     alerta = False    

            elif (220 <= x < 440) and (y < 220):
                if verificacao_01[0][1] == ' ':
                    pygame.draw.circle(tela, (0, 0, 255), (330, 110), 80)
                    verificacao_01[0][1] = 'zero'
                    alerta = False
                elif not verificacao_01[0][1] == ' ':
                     alerta = False
                
            elif (440 <= x < 660) and (y < 220):
                if verificacao_01[0][2] == ' ':
                    pygame.draw.circle(tela, (0, 0, 255), (550, 110), 80)
                    verificacao_01[0][2] = 'zero'
                    alerta = False

                elif not verificacao_01[0][2] == ' ':
                     alerta = False 
                    
            elif (x < 220) and (220 <= y < 440):
                if verificacao_01[1][0] == ' ':
                    pygame.draw.circle(tela, (0, 0, 255), (110, 330), 80)
                    verificacao_01[1][0] = 'zero'
                    alerta = False

                elif not verificacao_01[1][0] == ' ':
                     alerta = False
                
            elif (220 <= x < 440) and (220 <= y < 440):
                if verificacao_01[1][1] == ' ':
                    pygame.draw.circle(tela, (0, 0, 255), (330, 330), 80)
                    verificacao_01[1][1] = 'zero'
                    alerta = False

                elif not verificacao_01[1][1] == ' ':
                     alerta = False
            elif (440 <= x < 660) and ( 220 <= y < 440):
                if verificacao_01[1][2] == ' ':
                    pygame.draw.circle(tela, (0, 0, 255), (550, 330), 80)
                    verificacao_01[1][2] = 'zero'
                    alerta = False

                elif not verificacao_01[1][2] == ' ':
                     alerta = False
            elif (x < 220) and (440 <= y < 660):
                if verificacao_01[2][0] == ' ':
                    pygame.draw.circle(tela, (0, 0, 255), (110, 550), 80)
                    verificacao_01[2][0] = 'zero'
                    alerta = False
                    
                elif not verificacao_01[2][0] == ' ':
                     alerta = False
            elif (220 <= x < 440) and (440 <= y < 660):
                if verificacao_01[2][1] == ' ':
                    pygame.draw.circle(tela, (0, 0, 255), (330, 550), 80)
                    verificacao_01[2][1] = 'zero'
                    alerta = False

                elif not verificacao_01[2][1] == ' ':
                     alerta = False
            elif (440 <= x < 660) and (440 <= y < 660):
                if verificacao_01[2][2] == ' ':
                    pygame.draw.circle(tela, (0, 0, 255), (550, 550), 80)
                    verificacao_01[2][2] = 'zero'
                    alerta = False

                elif not verificacao_01[2][2] == ' ':
                     alerta = False

def placar(jogador_1, jogador_2, tela):
    pygame.init()

    cor_texto = (255, 255, 255)


    fonte = pygame.font.Font(None, 36)


    texto = fonte.render(f"{jogador_1[0]}: {jogador_1[1]}", True, cor_texto)
    texto1 = fonte.render(f"X                    {jogador_2[0]}: {jogador_2[1]}",True, cor_texto)

    posicao_texto = (90, 670)

    posicao_texto1 = (330, 670)

    

    tela.fill((0, 0, 0))
    
    tela.blit(texto, posicao_texto)
    tela.blit(texto1, posicao_texto1)

def tabuleiro(tela):  
    pygame.init()
    pygame.draw.line(tela, (255, 255, 255), (220, 0), (220, 660), 5)
    pygame.draw.line(tela, (255, 255, 255), (440, 0), (440, 660), 5)
    pygame.draw.line(tela, (255, 255, 255), (0, 220), (660, 220), 5)
    pygame.draw.line(tela, (255, 255, 255), (0, 440), (660, 440), 5)
    pygame.draw.line(tela, (255, 255, 255), (0, 661), (661, 661), 5)
    
if oi == 2:
  verificacao_01 = [[' ', ' ', ' '],
                    [' ', ' ', ' '], 
                    [' ', ' ', ' ']]

  cont = 0

  largura = 660 # -
  altura = 700 # |

  verificacao = True

  vintorias = [0, False]
  jogador_1 = ['Jogador 1', 0]
  jogador_2 = ['Jogador 2', 0]

  pygame.init()

  tela = pygame.display.set_mode((largura, altura))
  pygame.display.set_caption('jogo da velha 2.0')

  placar(jogador_1, jogador_2, tela) 

  while verificacao:    

    for event in pygame.event.get():

      if event.type == pygame.QUIT:
          pygame.quit() 
          exit()

      if event.type  == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:

            x, y = pygame.mouse.get_pos()
            
            if vintorias[1] == True:
                cont = 0
                vintorias[1] = False

            turnos(cont, verificacao_01, x, y, tela)


            vintorias = verificacao_de_vitoria(verificacao_01, jogador_1, jogador_2)

            if vintorias[0] == 'j2':

                jogador_1[1] += 1
                placar(jogador_1, jogador_2, tela)
                verificacao_01 = [[' ', ' ', ' '],
                                  [' ', ' ', ' '], 
                                  [' ', ' ', ' ']]

            elif vintorias[0] == 'j1':
                jogador_2[1] += 1
                placar(jogador_1, jogador_2, tela)
                verificacao_01 = [[' ', ' ', ' '],
                                  [' ', ' ', ' '], 
                                  [' ', ' ', ' ']]

            elif vintorias[0] == 'empate':
                placar(jogador_1, jogador_2, tela) 
                verificacao_01 = [[' ', ' ', ' '],
                                  [' ', ' ', ' '], 
                                  [' ', ' ', ' ']]   

            cont += 1
  
      tabuleiro(tela)
      pygame.display.update() 