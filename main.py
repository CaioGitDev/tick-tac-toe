import turtle

class Board:
  def __init__(self):
    self.screen = turtle.Screen()
    self.screen.title("Tic Tac Toe")
    self.screen.setup(width=800, height=800)
    self.screen.bgcolor("white")

     # Registrar a imagem "X" convertida para GIF
    self.screen.addshape("minion_X.gif")
    self.screen.addshape("minion_O.gif")

    self.drawer = turtle.Turtle()
    self.drawer.speed(0)
    self.drawer.hideturtle()
    self.draw_board()

  def draw_board(self):
    self.drawer.color("black") # cor da caneta
    self.drawer.pensize(5)

    # desenhar linhas verticais
    for x in [-100, 100]:
      self.drawer.penup()
      self.drawer.goto(x, 300)
      self.drawer.pendown()
      self.drawer.goto(x, -300)
    
    # desenhar linhas horizontais
    for y in [-100, 100]:
      self.drawer.penup()
      self.drawer.goto(-300, y)
      self.drawer.pendown()
      self.drawer.goto(300, y)

  def draw_x(self, x, y):
    self.drawer.penup()
    self.drawer.goto(x, y)
    self.drawer.pendown()
    self.drawer.color("blue")
    #self.drawer.setheading(45)
    self.drawer.shape("minion_X.gif")
    # shape size
    self.drawer.shapesize(1, 1, 1)
    self.drawer.stamp()
  
  def draw_o(self, x, y):
    self.drawer.penup()
    self.drawer.goto(x, y)
    self.drawer.pendown()
    self.drawer.color("red")
    self.drawer.shape("minion_O.gif")
    # shape size
    self.drawer.shapesize(1, 1, 1)
    self.drawer.stamp()

  def clear_board(self):
    self.drawer.clear()

  def draw_user_message(self, message):
    self.drawer.penup()
    self.drawer.goto(0, 0)
    self.drawer.pendown()
    self.drawer.write(message, align="center", font=("Arial", 36, "bold"))


# classe do jogo principal que controla o tabuleiro e as jogadas

class Game:
  def __init__(self):
    self.board = Board()

    # define uma matriz 3x3 com strings vazias
    # [["", "", ""], ["", "", ""], ["", "", ""]]
    self.positions = [["" for _ in range(3)] for _ in range(3)] 

    # define o jogador inicial como "X"
    self.current_player = "X"

    # adiciona um evento para quando o jogador clicar na tela
    self.board.screen.onclick(self.handle_click)
  
  def handle_click(self, x, y):
      # Converte as coordenadas x e y para a posição na matriz
      row = 2 - int((y + 300) // 200) 
      col = int((x + 300) // 200) 

      # Verifica se a posição está dentro do tabuleiro e vazia
      if 0 <= row <= 2 and 0 <= col <= 2 and self.positions[row][col] == "":
          # Calcula as coordenadas do centro da célula para desenhar a peça
          screen_x = (col - 1) * 200
          screen_y = (1 - row) * 200

          # Desenha a peça do jogador atual
          if self.current_player == "X":
              print(f"X played at {row}, {col}")
              self.board.draw_x(screen_x, screen_y)
          else:
              print(f"O played at {row}, {col}")
              self.board.draw_o(screen_x, screen_y)

          # Atualiza a posição na matriz
          self.positions[row][col] = self.current_player

          # Verifica se o jogador atual venceu
          if self.check_winner():
              print(f"Player {self.current_player} wins!")
              self.board.clear_board()  # Limpa o tabuleiro
              self.board.draw_user_message(f"Player {self.current_player} wins!")  # Exibe a mensagem de vitória
          elif self.check_tie():
              self.board.clear_board()
              self.board.draw_user_message(f"Houve um empate!")
          else:
              # Muda o jogador atual
              self.current_player = "O" if self.current_player == "X" else "X"

  def check_winner(self):
    # verifica se o jogador atual venceu
    # verifica linhas
    for row in self.positions:
      if row[0] == row[1] == row[2] != "":
        return True

    # verifica colunas
    for col in range(3):
      if self.positions[0][col] == self.positions[1][col] == self.positions[2][col] != "":
        return True

    # verifica diagonais
    if self.positions[0][0] == self.positions[1][1] == self.positions[2][2] != "":
      return True

    if self.positions[0][2] == self.positions[1][1] == self.positions[2][0] != "":
      return True

    return False
  
  def check_tie(self):
    # verifica se houve empate
    for row in self.positions:
      for col in row:
        if col == "":
          return False
    return True


Game()
turtle.mainloop() # mantem a janela aberta