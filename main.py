import turtle

class Board:
  def __init__(self):
    self.screen = turtle.Screen()
    self.screen.title("Tic Tac Toe")
    self.screen.setup(width=800, height=800)
    self.screen.bgcolor("lightgray")

    self.screen.register_shape("minion_x.webp")

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
    self.drawer.goto(x - 60, y - 60)
    self.drawer.pendown()
    self.drawer.color("blue")
    self.drawer.setheading(45)
    self.drawer.shape("minion_x.webp")
    self.drawer.stamp()
  
  def draw_o(self, x, y):
    self.drawer.penup()
    self.drawer.goto(x, y - 60)
    self.drawer.pendown()
    self.drawer.color("red")
    self.drawer.shape("/assets/minion_o.webp")
    self.drawer.stamp()

  def clear_board(self):
    self.drawer.clear()
    self.draw_board()

  def draw_user_message(self, message):
    self.drawer.penup()
    self.drawer.goto(0, 0)
    self.drawer.pendown()
    self.drawer.write(message, align="center", font=("Arial", 36, "bold"))

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
    # converte as coordenadas x e y para a posição na matriz
    # x = -300, y = 300 -> positions[0][2]
    # x = 0, y = 0 -> positions[1][1]
    # x = 300, y = -300 -> positions[2][0]
    row = 2 - int((y + 300) // 200) 
    col = int((x + 300) // 200) 

    # verifica se a posição está vazia
    if 0 <= row <= 2 and 0 <= col <= 2 and self.positions[row][col] == "":
      # desenha a peça do jogador atual
      if self.current_player == "X":
        self.board.draw_x(col * 200, row * 200)
      else:
        self.board.draw_o(col * 200, row * 200)

      # atualiza a posição na matriz
      self.positions[row][col] = self.current_player

      # verifica se o jogador atual venceu
      if self.check_winner():
        print(f"Player {self.current_player} wins!")
        
        # limpar o tabuleiro
        self.board.clear_board()
        # escrever mensagem de vitória
        self.board.draw_user_message(f"Player {self.current_player} wins!")
        
      else:
        # muda o jogador atual
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


Game()
turtle.mainloop() # mantem a janela aberta