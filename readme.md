# O Jogo do Galo

## Descrição do jogo

O Jogo do Galo é um jogo de tabuleiro para dois jogadores, X e O, que preenchem alternadamente os espaços de um tabuleiro 3x3. O jogador que conseguir colocar três das suas peças numa linha, coluna ou diagonal vence o jogo.
Neste jogo iremos alterar o X e o O por gifs animados.

## Objetivo do projeto

O objetivo deste projeto é desenvolver um jogo do galo em Python, utilizando a biblioteca turtle.

## Regras do jogo

1. O jogo é jogado num tabuleiro 3x3.
2. O jogador X começa o jogo.
3. Os jogadores alternam entre si.
4. O jogo termina quando um dos jogadores conseguir colocar três das suas peças numa linha, coluna ou diagonal.
5. Se todas as casas do tabuleiro estiverem preenchidas e nenhum jogador tiver conseguido vencer, o jogo termina em empate.

## O jogo será dividido em 2 classes principais: `Tabuleiro` e `Jogo`.

A classe `Tabuleiro` terá os seguintes métodos:
1. `__init__()`: inicializa o tabuleiro com os valores padão.
2. `draw_board()`: desenha o tabuleiro.
3. `draw_x()`: adiciona o gif do jogador X ao tabuleiro.
4. `draw_o()`: adiciona o gif do jogador O ao tabuleiro.
5. `clear_board()`: limpa o tabuleiro.
6. `draw_user_message()`: desenha uma mensagem para o utilizador.

Esta classe é responsavel por desenhar todos os elementos do jogo.

A classe `Jogo` terá os seguintes métodos:
1. `init()`: inicia o jogo, diz quem será o primeiro a jogar e cria uma matriz 3x3 para marcar onde foi jogado.
2. `handle_click()`: trata o click no tabuleiro e da as coordenadas de onde foi clicado na matriz que depois será convertido em coordenadas x,y.
3. `check_win()`: verifica se algum jogador ganhou.

## Descrição do Top-Down Design

1. Inicializar o jogo.
2. Desenhar o tabuleiro.
3. Esperar que o utilizador clique numa casa do tabuleiro.
4. Desenhar o gif do jogador correspondente na casa clicada.
5. Verificar se algum jogador ganhou.
6. Se algum jogador ganhou, desenhar uma mensagem a dizer quem ganhou.
7. Se ninguém ganhou, desenhar uma mensagem a dizer que o jogo terminou em empate.
9. Terminar

## Referências

1. [Documentação da biblioteca turtle](https://docs.python.org/3/library/turtle.html)
2. [Tutorial de Python Turtle Graphics](https://realpython.com/beginners-guide-python-turtle/)

