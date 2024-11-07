import turtle

# Classe para desenhar o tabuleiro e as peças
class Board:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Tic Tac Toe")
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("white")
        self.drawer = turtle.Turtle()
        self.drawer.speed(0)
        self.drawer.hideturtle()
        self.draw_board()

    def draw_board(self):
        self.drawer.color("black")
        self.drawer.pensize(5)
        
        # Linhas verticais
        for x in [-100, 100]:
            self.drawer.penup()
            self.drawer.goto(x, 300)
            self.drawer.pendown()
            self.drawer.goto(x, -300)
        
        # Linhas horizontais
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
        for _ in range(2):
            self.drawer.forward(120)
            self.drawer.backward(120)
            self.drawer.right(90)

    def draw_o(self, x, y):
        self.drawer.penup()
        self.drawer.goto(x, y - 60)
        self.drawer.pendown()
        self.drawer.color("red")
        self.drawer.setheading(0)
        self.drawer.circle(60)

# Classe para gerenciar o estado do jogo e verificar o vencedor
class Game:
    def __init__(self):
        self.board = Board()
        self.positions = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.board.screen.onclick(self.handle_click)

    def handle_click(self, x, y):
        col = int((x + 300) // 200)
        row = int((y + 300) // 200)

        if 0 <= row <= 2 and 0 <= col <= 2 and self.positions[row][col] == "":
            self.positions[row][col] = self.current_player
            screen_x, screen_y = col * 200 - 200, row * 200 - 200

            if self.current_player == "X":
                self.board.draw_x(screen_x, screen_y)
                self.current_player = "O"
            else:
                self.board.draw_o(screen_x, screen_y)
                self.current_player = "X"
            
            if self.check_winner():
                print(f"{self.positions[row][col]} venceu o jogo!")
                self.board.screen.bye()

    def check_winner(self):
        for i in range(3):
            # Checar linhas e colunas
            if (self.positions[i][0] == self.positions[i][1] == self.positions[i][2] != "" or
                self.positions[0][i] == self.positions[1][i] == self.positions[2][i] != ""):
                return True
            
        # Checar diagonais
        if (self.positions[0][0] == self.positions[1][1] == self.positions[2][2] != "" or
            self.positions[0][2] == self.positions[1][1] == self.positions[2][0] != ""):
            return True

        return False

# Inicializa o jogo
Game()
turtle.mainloop()
