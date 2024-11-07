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


## Descrição do Top-Down Design

O programa é dividido em 3 funções principais:
1. `desenha_tabuleiro()`: Esta função desenha o tabuleiro do jogo.
2. `jogada()`: Esta função permite ao jogador fazer uma jogada.
3. `verifica_vitoria()`: Esta função verifica se um dos jogadores venceu o jogo.

## Descrição do Bottom-Up Design

1. `desenha_tabuleiro()`: 
    1.1. Desenhar o tabuleiro.
    1.2. Desenhar as linhas horizontais.
    1.3. Desenhar as linhas verticais.
2. `jogada()`:
    2.1. Obter a posição da jogada.
    2.2. Verificar se a posição é válida.
    2.3. Colocar a peça do jogador na posição escolhida.
3. `verifica_vitoria()`:
    3.1. Verificar se algum jogador venceu na horizontal.
    3.2. Verificar se algum jogador venceu na vertical.
    3.3. Verificar se algum jogador venceu na diagonal.


## Referências

1. [Documentação da biblioteca turtle](https://docs.python.org/3/library/turtle.html)
2. [Tutorial de Python Turtle Graphics](https://realpython.com/beginners-guide-python-turtle/)

