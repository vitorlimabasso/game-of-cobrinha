# Snake - Jogo da Cobrinha

## Descrição

Este projeto consiste na implementação do clássico jogo da cobrinha (Snake), desenvolvido em Python utilizando a biblioteca Pygame.

O objetivo do jogador é controlar a cobra pela tela, coletando alimentos para aumentar sua pontuação e tamanho. O jogo termina quando a cobra colide com as bordas da tela ou com o próprio corpo.

## Funcionalidades

- Movimentação da cobra utilizando as teclas direcionais do teclado;
- Geração aleatória de alimentos na tela;
- Crescimento da cobra ao coletar alimentos;
- Sistema de pontuação em tempo real;
- Detecção de colisão com paredes;
- Detecção de colisão com o próprio corpo;
- Tela de Game Over;
- Reinício da partida sem fechar o programa.

## Tecnologias Utilizadas

- Python 3
- Pygame

## Instalação

Instale a biblioteca Pygame utilizando o comando:

```bash
pip install pygame
```

## Execução

Execute o arquivo principal do projeto:

```bash
python snake.py
```

## Controles

| Tecla | Função |
|---------|---------|
| ↑ | Mover para cima |
| ↓ | Mover para baixo |
| ← | Mover para esquerda |
| → | Mover para direita |
| R | Reiniciar após Game Over |

## Regras do Jogo

1. Controle a cobra utilizando as setas do teclado.
2. Colete os alimentos para aumentar sua pontuação.
3. Cada alimento coletado faz a cobra crescer.
4. Evite colidir com as paredes da tela.
5. Evite colidir com o próprio corpo.
6. Ao ocorrer uma colisão, o jogo entra em estado de Game Over.
7. Pressione a tecla **R** para iniciar uma nova partida.

## Autor

Vitor Basso

Desenvolvido como atividade prática da disciplina de Programação utilizando Python e Pygame.