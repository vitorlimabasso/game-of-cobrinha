import pygame
import random

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()

# Cores
ROXO = (184, 122, 255)
VERMELHO = (136, 0, 0)
VERDE = (0, 180, 0)
PRETO = (0, 0, 0)

# Pos inicial cobrosa
cobra = [[400, 300], [380, 300], [360, 300]]
direcao = "direita"

#RAMDOMIZA A POSIÇÃO DA COMIDA
comida_x = random.randint(0, 39) * 20
comida_y = random.randint(0, 29) * 20

pontos = 0
game_over = False
rodando = True

fonte = pygame.font.SysFont("arial", 30)

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                # NAO DEIXA A COBRA BATER NELA MESMA (VOLTA 180) 
                if event.key == pygame.K_LEFT and direcao != "direita":
                    direcao = "esquerda"
                elif event.key == pygame.K_RIGHT and direcao != "esquerda":
                    direcao = "direita"
                elif event.key == pygame.K_UP and direcao != "baixo":
                    direcao = "cima"
                elif event.key == pygame.K_DOWN and direcao != "cima":
                    direcao = "baixo"
            else:
                if event.key == pygame.K_r:
                    # Reinicia tudo
                    cobra = [[400, 300], [380, 300], [360, 300]]
                    direcao = "direita"
                    comida_x = random.randint(0, 39) * 20
                    comida_y = random.randint(0, 29) * 20
                    pontos = 0
                    game_over = False

    if not game_over:
        # posição da cabêçsssss
        cabeca_x = cobra[0][0]
        cabeca_y = cobra[0][1]

        # Calcula a nova cabêçsssss 
        if direcao == "direita":
            cabeca_x += 20
        elif direcao == "esquerda":
            cabeca_x -= 20
        elif direcao == "cima":
            cabeca_y -= 20
        elif direcao == "baixo":
            cabeca_y += 20

        nova_cabeca = [cabeca_x, cabeca_y]

        # colisao paredes
        if cabeca_x < 0 or cabeca_x >= 800 or cabeca_y < 0 or cabeca_y >= 600:
            game_over = True

        # VERIFICA SE ELA BATEU EM ALGO
        if nova_cabeca in cobra:
            game_over = True
        # COLOCA A NOVA CABEÇA NA FRENTE
        cobra.insert(0, nova_cabeca)

        # comeu?
        if cabeca_x == comida_x and cabeca_y == comida_y:
            pontos += 1
            comida_x = random.randint(0, 39) * 20
            comida_y = random.randint(0, 29) * 20
        else:

            # se não comeu nada nessa rodada tira o último pedaço para manter o tamanho
            cobra.pop() # Remove rabo

    # Desenho na tela
    tela.fill(ROXO)

    # Desenha a comida
    pygame.draw.rect(tela, VERDE, (comida_x, comida_y, 20, 20))

    # Desenha a cobra  no loop
    for pedaco in cobra:
        pygame.draw.rect(tela, VERMELHO, (pedaco[0], pedaco[1], 20, 20))

    # Placar
    txt_pontos = fonte.render(f"Pontos: {pontos}", True, PRETO)
    tela.blit(txt_pontos, (10, 10))

    # Game Over
    if game_over:
        txt_go = fonte.render("GAME OVER! Aperte R para reiniciar", True, PRETO)
        tela.blit(txt_go, (200, 280))

    pygame.display.flip()
    relogio.tick(10) # VELOCIDADE DA COBROSA

pygame.quit()   